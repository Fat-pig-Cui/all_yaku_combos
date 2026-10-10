#!/usr/bin/env python3
"""Check handwritten tables, legacy arithmetic scripts and the normalized export."""
import ast
from collections import Counter
import contextlib
import gzip
import hashlib
import io
import json
from pathlib import Path
import re

from expand_topics import ROOT, TOPICS, collect, eligible, expand_combinations

OPEN_TOPICS = {1: 0, 2: 2, 3: 3, 4: 4, 5: 6, 6: 7, 7: 9, 8: 10,
               9: 12, 10: 13, 11: 14, 12: 15, 13: 16}


def histogram(rows, factor=1):
    counts = Counter(r['han'] for r in rows)
    assert all(v % factor == 0 for v in counts.values())
    return [counts[h] // factor for h in range(21)]


def arrays(path):
    result = {}
    for node in ast.parse(path.read_text(encoding='utf-8')).body:
        if not isinstance(node, ast.Assign) or not isinstance(node.targets[0], ast.Name):
            continue
        try:
            value = ast.literal_eval(node.value)
        except (ValueError, TypeError):
            continue
        if isinstance(value, list) and len(value) == 21 and all(isinstance(n, int) for n in value):
            result[node.targets[0].id] = value
    return result


def check_document(path, base, full, tables):
    text = path.read_text(encoding='utf-8')
    checked = 0
    for match in re.finditer(r'(?m)^\| 番数[^\n]*\n(?:\|[^\n]*\n)+', text):
        block = match[0]
        prefix = text[:match.start()]
        headings = re.findall(r'^#{2,3} (.+)', prefix, re.M)
        heading = headings[-1] if headings else ''
        if '总计:' in heading:
            expected = full
        elif '## 条件役展开' not in prefix:
            expected = base
        else:
            context = '\n\n'.join(prefix.rsplit('\n\n', 2)[-2:])
            keys = re.findall(r'`(table(?:_\d+)?)`', context)
            assert keys, (path, context)
            expected = tables[keys[-1]]
        multiplied = '乘3' in block.splitlines()[0]
        difference = '差值' in block.splitlines()[0]
        for line in block.splitlines()[2:]:
            cells = [c.strip() for c in line.strip('|').split('|')]
            if cells[0].isdigit():
                han = int(cells[0])
                assert int(cells[1]) == expected[han], (path, line, expected[han])
                if multiplied:
                    assert int(cells[2]) == 3 * expected[han], (path, line)
                elif difference:
                    assert int(cells[2]) == base[han] - expected[han], (path, line)
            elif cells[0] == '总计':
                assert int(cells[1]) == sum(expected), (path, line)
                if multiplied:
                    assert int(cells[2]) == 3 * sum(expected), (path, line)
        checked += 1
    return checked


def check():
    base = collect()
    assert all(r['han'] == r['declared_han'] for r in base), 'Base row is in the wrong han section'
    records = expand_combinations(base)
    keys = {(r['closed'], tuple(r['yaku'])) for r in records}
    assert len(keys) == len(records), 'Duplicate complete combination'
    master = arrays(ROOT / 'cal_sum.py')
    for name, values in master.items():
        if not re.fullmatch(r'table_(?:2_)?\d+', name):
            continue
        closed = not name.startswith('table_2_')
        n = int(name.split('_')[-1])
        index = n - 1 if closed else OPEN_TOPICS[n]
        assert values == histogram([r for r in records if r['closed'] == closed and r['topic'] == TOPICS[index]]), name
    root_tables = list(re.finditer(r'(?m)^\| 番数[^\n]*\n(?:\|[^\n]*\n)+',
                                  (ROOT / 'README.md').read_text(encoding='utf-8')))
    assert len(root_tables) == 2
    for table, closed in zip(root_tables, (True, False)):
        values = histogram([r for r in records if r['closed'] == closed])
        for line in table[0].splitlines()[2:]:
            cells = [c.strip() for c in line.strip('|').split('|')]
            if cells[0].isdigit():
                assert int(cells[1]) == values[int(cells[0])], line
            elif cells[0] == '总计':
                assert int(cells[1]) == sum(values), line
    document_tables = 0
    for topic in TOPICS[1:]:
        directory = ROOT / topic
        script = directory / '辅助计算脚本.py'
        capture = io.StringIO()
        with contextlib.redirect_stdout(capture):
            exec(compile(script.read_text(encoding='utf-8'), str(script), 'exec'), {})
        printed = []
        for line in capture.getvalue().splitlines():
            if line.startswith('['):
                value = ast.literal_eval(line)
                if isinstance(value, list) and len(value) == 21 and all(isinstance(n, int) for n in value):
                    printed.append(value)
        factor = 3 if topic == '小三元专题' else 1
        assert printed[-1] == histogram([r for r in records if r['closed'] and r['topic'] == topic], factor), script
        files = [(True, directory / '门清.md'), (False, directory / '副露.md')]
        if not files[0][1].exists():
            files = [(True, directory / 'README.md')]
        for closed, path in files:
            selected = [r for r in base if r['closed'] == closed and r['topic'] == topic]
            a = histogram(selected, factor)
            full = histogram([r for r in records if r['closed'] == closed and r['topic'] == topic], factor)
            tables = arrays(script) if closed else {
                'table': a,
                'table_2': histogram([r for r in selected if eligible(r, ('chankan',))], factor),
                'table_3': histogram([r for r in selected if eligible(r, ('rinshan',))], factor)}
            document_tables += check_document(path, a, full, tables)
    summary = json.loads((ROOT / 'results/summary.json').read_text(encoding='utf-8'))
    for name, expected in summary['source_sha256'].items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, name
    archive = ROOT / 'results' / summary['archive']
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == summary['archive_sha256']
    exported = json.loads(gzip.decompress(archive.read_bytes()))['rows']
    assert exported == records, 'Export differs from current handwritten expansion'
    assert summary['combination_count'] == len(records)
    for mode, closed in [('closed', True), ('open', False)]:
        selected = [r for r in records if r['closed'] == closed]
        assert summary[mode]['count'] == len(selected)
        assert summary[mode]['han_histogram'] == {str(h): n for h, n in enumerate(histogram(selected)) if n}
    print(json.dumps({'combinations_checked': len(records), 'base_rows_checked': len(base),
                      'topic_scripts_checked': 16, 'document_tables_checked': document_tables,
                      'export_and_source_hashes_match': True}, ensure_ascii=False))


if __name__ == '__main__':
    check()

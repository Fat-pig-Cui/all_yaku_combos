#!/usr/bin/env python3
"""Normalize the handwritten base-yaku tables, without depending on another repo.

This expands dragon/wind abbreviations and restores implicit accompanying yaku.
It does not infer tile shapes or certify action legality.
"""
import argparse
from collections import Counter
import gzip
import hashlib
from itertools import combinations
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TOPICS = (
    '条件役专题', '七对子专题', '小三元专题', '无小三元的一般形混老头专题',
    '一般形断幺九专题', '无断幺的平和专题', '无断幺平和的一般形清一色专题',
    '无平和清一色的纯全带幺九专题', '只含混全和混色的二杯口专题',
    '无平和清一色的一气通贯专题', '无断幺平和纯全的三色同顺专题',
    '只含役牌双混的一杯口专题', '无混老断幺纯全的三色同刻专题',
    '只含役牌三暗杠混色的混全专题', '只含役牌混对对三暗的三杠专题',
    '只含役牌三暗混一色的对对专题', '其他部分',
)
SLUGS = dict(zip(
    ('平和 一杯 二杯 七对 断幺 混全 一气 三色 三刻 三杠 对对 三暗 小元 混老 纯全 混色 清色').split(),
    ('pinfu iipeikou ryanpeikou chiitoitsu tanyao chanta ittsuu sanshoku_doujun '
     'sanshoku_doukou sankantsu toitoi sanankou shousangen honroutou junchan honitsu chinitsu').split()))
HAN = dict(zip(SLUGS.values(), (1, 1, 3, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 6)))
HAN.update({s: 1 for s in ('haku', 'hatsu', 'chun', 'seat_wind', 'round_wind')})
HAN.update({s: 1 for s in ('riichi', 'ippatsu', 'chankan', 'rinshan', 'haitei', 'houtei', 'menzen_tsumo')})
HAN['double_riichi'] = 2
OPEN_HAN = dict(HAN, chanta=1, ittsuu=1, sanshoku_doujun=1, junchan=2, honitsu=2, chinitsu=5)


def expand_row(cells, closed):
    tokens = [c.lstrip('^') for c in cells]
    if len([t for t in tokens if t in SLUGS]) != len({t for t in tokens if t in SLUGS}):
        raise ValueError('Ordinary yaku must not appear twice in a row: ' + str(cells))
    core = {SLUGS[t] for t in tokens if t in SLUGS}
    dragons = tokens.count('三元')
    winds = tokens.count('四风')
    if 'shousangen' in core:
        dragons = 2
    if 'honroutou' in core and 'chiitoitsu' not in core:
        core.add('toitoi')
    if closed and core & {'toitoi', 'sankantsu'}:
        core.add('sanankou')
    for ds in combinations(('haku', 'hatsu', 'chun'), dragons):
        for ws in combinations(('seat_wind', 'round_wind'), winds):
            yield sorted(core | set(ds) | set(ws))


def collect():
    rows = []
    seen = {}
    for topic in TOPICS[1:]:
        directory = ROOT / topic
        files = [(True, directory / '门清.md'), (False, directory / '副露.md')]
        if not files[0][1].exists():
            files = [(True, directory / 'README.md')]
        for closed, path in files:
            active = False
            han = None
            for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
                if line.startswith('## 条件役展开'):
                    break
                match = re.match(r'^#{2,3} (?:\*\*)?(\d+)番', line)
                if match:
                    han = int(match[1])
                    active = True
                if not active or not line.startswith('|'):
                    continue
                cells = [c.strip() for c in line.strip().strip('|').split('|')]
                # Starred rows explicitly require an unlisted accompanying yaku;
                # ampersand rows are excluded sanma-only cases.
                if any(c.startswith(('*', '&')) for c in cells):
                    continue
                if not any(c.lstrip('^') in SLUGS or c in ('三元', '四风') for c in cells):
                    continue
                for yaku in expand_row(cells, closed):
                    key = closed, tuple(yaku)
                    if key in seen:
                        raise ValueError('Duplicate base row: ' + str(key) + ' at ' +
                                         str((str(path), number)) + ' first ' + str(seen[key]))
                    seen[key] = (str(path), number)
                    rows.append({'topic': topic, 'closed': closed, 'yaku': yaku,
                                 'han': sum((HAN if closed else OPEN_HAN)[s] for s in yaku),
                                 'declared_han': han,
                                 'source': path.relative_to(ROOT).as_posix(), 'line': number,
                                 'notes': [c for c in cells if c in ('双碰荣和', '无法枪杠')]})
    return rows


def condition_states(closed):
    if not closed:
        return [(), ('chankan',), ('rinshan',), ('haitei',), ('houtei',)]
    states = []
    for declaration in ((), ('riichi',), ('double_riichi',)):
        for ippatsu in (False, True):
            if ippatsu and not declaration:
                continue
            for event in ('none', 'chankan', 'rinshan', 'haitei', 'houtei'):
                for tsumo in (False, True):
                    if event in ('chankan', 'houtei') and tsumo:
                        continue
                    if event in ('rinshan', 'haitei') and not tsumo:
                        continue
                    if ippatsu and event in ('rinshan', 'houtei'):
                        continue
                    if declaration == ('double_riichi',) and (event == 'chankan' or (ippatsu and event == 'haitei')):
                        continue
                    states.append(tuple(sorted(declaration + (('ippatsu',) if ippatsu else ()) +
                                               (() if event == 'none' else (event,)) +
                                               (('menzen_tsumo',) if tsumo else ()))))
    return states


def eligible(row, condition):
    """Apply explicit topic restrictions; these rules are independent of a scorer.

    The exceptions below come from counting required sequences / winning-tile
    copies. They are documented with counterexamples in CORRECTIONS.md.
    """
    yaku = set(row['yaku'])
    c = set(condition)
    if not row['closed']:
        if 'chankan' in c and yaku & {'toitoi', 'sanankou'}:
            return False
        return not ('rinshan' in c and 'chinitsu' in yaku and yaku & {'ittsuu', 'junchan'})
    if {'double_riichi', 'ippatsu'} <= c and 'sankantsu' in yaku:
        return False
    special = bool(c & {'menzen_tsumo', 'chankan', 'rinshan', 'haitei'})
    if special and ('toitoi' in yaku or '双碰荣和' in row['notes'] or
                    ('sanshoku_doukou' in yaku and 'sanankou' not in yaku)):
        return False
    if 'chankan' in c:
        if yaku & {'chiitoitsu', 'ryanpeikou'} or '无法枪杠' in row['notes']:
            return False
        dragons = len(yaku & {'haku', 'hatsu', 'chun'})
        honor_groups = dragons + bool(yaku & {'seat_wind', 'round_wind'})
        if 'iipeikou' in yaku and honor_groups >= 2:
            return False
        if {'pinfu', 'chinitsu', 'junchan', 'iipeikou'} <= yaku:
            return False
    if 'rinshan' in c:
        if yaku & {'pinfu', 'chiitoitsu', 'ryanpeikou'}:
            return False
        if {'sanshoku_doujun', 'iipeikou'} <= yaku:
            return False
        if {'ittsuu', 'iipeikou'} <= yaku:
            return False
        if 'chinitsu' in yaku and yaku & {'ittsuu', 'junchan'}:
            return False
    return True


def expand_combinations(rows=None):
    rows = collect() if rows is None else rows
    rows = rows + [dict(topic=TOPICS[0], closed=closed, yaku=[], han=0,
                        source='条件役专题/README.md', line=1, notes=[])
                   for closed in (True, False)]
    result = []
    for row in rows:
        for c in condition_states(row['closed']):
            if not eligible(row, c) or not (row['yaku'] or c):
                continue
            yaku = sorted(set(row['yaku']) | set(c))
            result.append(dict(topic=row['topic'], closed=row['closed'], yaku=yaku,
                               han=sum((HAN if row['closed'] else OPEN_HAN)[s] for s in yaku),
                               source=row['source'], line=row['line']))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--combinations', action='store_true', help='Expand the condition states as well')
    parser.add_argument('--summary', type=Path)
    args = parser.parse_args()
    rows = expand_combinations() if args.combinations else collect()
    payload = json.dumps({'schema_version': 1, 'rows': rows}, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        if args.output.suffix == '.gz':
            args.output.write_bytes(gzip.compress(payload.encode('utf-8'), mtime=0))
        else:
            args.output.write_text(payload, encoding='utf-8')
        print(args.output)
    else:
        print(payload, end='')
    if args.summary:
        if not args.combinations or not args.output:
            parser.error('--summary requires --combinations and --output')
        sources = sorted({ROOT / r['source'] for r in rows} | {Path(__file__).resolve()})
        summary = {'schema_version': 1, 'method': 'handwritten_base_tables_and_explicit_condition_rules',
                   'scope': {'players': 4, 'dora': 0, 'natural_yakuman': False,
                             'counting_unit': 'closed_status_and_complete_selected_yaku_set',
                             'selection': 'maximum(base_points, raw_han, fu); retain exact ties'},
                   'combination_count': len(rows),
                   'archive': args.output.name,
                   'archive_sha256': hashlib.sha256(args.output.read_bytes()).hexdigest(),
                   'source_sha256': {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                                     for p in sources},
                   'topics': {}}
        for mode, closed in [('closed', True), ('open', False)]:
            selected = [r for r in rows if r['closed'] == closed]
            histogram = Counter(r['han'] for r in selected)
            summary[mode] = {'count': len(selected), 'han_histogram': dict(sorted(histogram.items()))}
        for topic in TOPICS:
            summary['topics'][topic] = {}
            for mode, closed in [('closed', True), ('open', False)]:
                selected = [r for r in rows if r['closed'] == closed and r['topic'] == topic]
                histogram = Counter(r['han'] for r in selected)
                summary['topics'][topic][mode] = {'count': len(selected), 'han_histogram': dict(sorted(histogram.items()))}
        args.summary.parent.mkdir(parents=True, exist_ok=True)
        args.summary.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(args.summary)


if __name__ == '__main__':
    main()

"""Regressions for the concrete combination omissions and impossible events."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from expand_topics import expand_combinations


class ExpansionRegressions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = expand_combinations()
        cls.keys = {(r['closed'], frozenset(r['yaku'])) for r in cls.rows}

    def test_no_duplicate_complete_combinations(self):
        self.assertEqual(len(self.rows), len(self.keys))

    def test_seven_pairs_simple_flush_is_never_selected(self):
        self.assertFalse(any({'chiitoitsu', 'chinitsu', 'tanyao'} <= y for _, y in self.keys))

    def test_iipeikou_chanta_honitsu_is_present(self):
        self.assertIn((True, frozenset(('iipeikou', 'chanta', 'honitsu'))), self.keys)

    def test_honroutou_flush_multiple_value_yaku_is_present(self):
        self.assertIn((True, frozenset(('honroutou', 'honitsu', 'haku', 'hatsu', 'toitoi', 'sanankou'))), self.keys)

    def test_missing_pinfu_chanta_sanshoku_is_present(self):
        self.assertIn((True, frozenset(('pinfu', 'chanta', 'sanshoku_doujun'))), self.keys)

    def test_four_sequences_cannot_rinshan(self):
        for closed, y in self.keys:
            if {'iipeikou', 'sanshoku_doujun'} <= y or {'iipeikou', 'ittsuu'} <= y:
                self.assertNotIn('rinshan', y)

    def test_iipeikou_with_another_kan_group_can_rinshan(self):
        self.assertIn((True, frozenset(('iipeikou', 'menzen_tsumo', 'rinshan'))), self.keys)

    def test_pure_flush_ittsuu_or_junchan_cannot_rinshan(self):
        for closed, y in self.keys:
            if 'chinitsu' in y and y & {'ittsuu', 'junchan'}:
                self.assertNotIn('rinshan', y)

    def test_pinfu_flush_junchan_iipeikou_cannot_chankan(self):
        for closed, y in self.keys:
            if {'pinfu', 'chinitsu', 'junchan', 'iipeikou'} <= y:
                self.assertNotIn('chankan', y)

    def test_sanshoku_doukou_tsumo_requires_sanankou_when_closed(self):
        for closed, y in self.keys:
            if closed and {'sanshoku_doukou', 'menzen_tsumo'} <= y:
                self.assertIn('sanankou', y)
        self.assertIn((True, frozenset(('sanshoku_doukou',))), self.keys)

    def test_open_sanankou_cannot_chankan(self):
        self.assertFalse(any(not c and {'sanankou', 'chankan'} <= y for c, y in self.keys))

    def test_open_three_kans_small_dragons_chankan_remains(self):
        y = ('chankan', 'haku', 'hatsu', 'shousangen', 'sankantsu', 'seat_wind', 'round_wind', 'honitsu', 'chanta')
        self.assertIn((False, frozenset(y)), self.keys)

    def test_double_riichi_chankan_is_excluded_but_ordinary_ippatsu_remains(self):
        self.assertFalse(any({'double_riichi', 'chankan'} <= y for _, y in self.keys))
        self.assertIn((True, frozenset(('riichi', 'ippatsu', 'chankan'))), self.keys)


if __name__ == '__main__':
    unittest.main()

import unittest

from days.day15 import Day15
from days.utils import FileReader


class TestDay15(unittest.TestCase):
    def test_determine_hash(self):
        self.assertEqual(Day15.determine_hash("HASH"), 52)
        self.assertEqual(Day15.determine_hash("rn"), 0)
        self.assertEqual(Day15.determine_hash("qp"), 1)
        self.assertEqual(Day15.determine_hash("ot"), 3)

    def test_part1(self):
        reader = FileReader("testdata/testdata_day15")
        day15 = Day15(reader.read_lines())
        self.assertEqual(day15.part1(), 1320)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day15")
        day15 = Day15(reader.read_lines())
        self.assertEqual(day15.part1(), 519041)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day15")
        day15 = Day15(reader.read_lines())
        self.assertEqual(day15.part2(), 145)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day15")
        day15 = Day15(reader.read_lines())
        self.assertEqual(day15.part2(), 260530)

import unittest

from days.day4 import Day4
from days.utils import FileReader


class TestDay4(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day4")
        day4 = Day4(reader.read_lines())
        self.assertEqual(day4.part1(), 13)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day4")
        day4 = Day4(reader.read_lines())
        self.assertEqual(day4.part1(), 23941)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day4")
        day4 = Day4(reader.read_lines())
        self.assertEqual(day4.part2(), 30)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day4")
        day4 = Day4(reader.read_lines())
        self.assertEqual(day4.part2(), 5571760)

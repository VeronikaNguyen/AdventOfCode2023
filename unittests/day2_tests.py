import unittest

from days.day2 import Day2
from days.utils import FileReader


class TestDay2(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day2")
        day2 = Day2(reader.read_lines())
        self.assertEqual(day2.part1(), 8)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day2")
        day2 = Day2(reader.read_lines())
        self.assertEqual(day2.part1(), 2285)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day2")
        day2 = Day2(reader.read_lines())
        self.assertEqual(day2.part2(), 2286)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day2")
        day2 = Day2(reader.read_lines())
        self.assertEqual(day2.part2(), 77021)

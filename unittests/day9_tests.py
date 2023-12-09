import unittest

from days.day9 import Day9
from days.utils import FileReader


class TestDay9(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day9")
        day9 = Day9(reader.read_lines())
        self.assertEqual(day9.part1(), 114)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day9")
        day9 = Day9(reader.read_lines())
        self.assertEqual(day9.part1(), 0)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day9")
        day9 = Day9(reader.read_lines())
        self.assertEqual(day9.part2(), 2)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day9")
        day9 = Day9(reader.read_lines())
        self.assertEqual(day9.part2(), 1112)

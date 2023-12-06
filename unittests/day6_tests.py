import unittest

from days.day6 import Day6
from days.utils import FileReader


class TestDay6(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day6")
        day6 = Day6(reader.read_lines())
        self.assertEqual(day6.part1(), 288)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day6")
        day6 = Day6(reader.read_lines())
        self.assertEqual(day6.part1(), 512295)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day6")
        day6 = Day6(reader.read_lines())
        self.assertEqual(day6.part2(), 71503)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day6")
        day6 = Day6(reader.read_lines())
        self.assertEqual(day6.part2(), 36530883)

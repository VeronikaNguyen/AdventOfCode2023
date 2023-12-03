import unittest

from days.day3 import Day3
from days.utils import FileReader


class TestDay3(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day3")
        day3 = Day3(reader.read_lines())
        self.assertEqual(day3.part1(), 4361)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day3")
        day3 = Day3(reader.read_lines())
        self.assertEqual(day3.part1(), 535235)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day3")
        day3 = Day3(reader.read_lines())
        self.assertEqual(day3.part2(), 467835)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day3")
        day2 = Day3(reader.read_lines())
        self.assertEqual(day2.part2(), 79844424)

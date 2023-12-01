import unittest

from days.day1 import Day1
from days.utils import FileReader


class TestDay1(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day1_part1")
        day1 = Day1(reader.read_lines())
        self.assertEqual(day1.part1(), 142)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day1")
        day1 = Day1(reader.read_lines())
        self.assertEqual(day1.part1(), 52974)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day1_part2")
        day1 = Day1(reader.read_lines())
        self.assertEqual(day1.part2(), 281)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day1")
        day1 = Day1(reader.read_lines())
        self.assertEqual(day1.part2(), 53340)

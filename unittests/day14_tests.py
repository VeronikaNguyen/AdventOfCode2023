import unittest

from days.day14 import Day14
from days.utils import FileReader


class TestDay14(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day14")
        day14 = Day14(reader.read_lines())
        self.assertEqual(day14.part1(), 136)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day14")
        day14 = Day14(reader.read_lines())
        self.assertEqual(day14.part1(), 108918)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day14")
        day14 = Day14(reader.read_lines())
        self.assertEqual(day14.part2(), 64)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day14")
        day14 = Day14(reader.read_lines())
        self.assertEqual(day14.part2(), 0)

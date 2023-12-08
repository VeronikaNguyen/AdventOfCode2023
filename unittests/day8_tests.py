import unittest

from days.day8 import Day8
from days.utils import FileReader


class TestDay8(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day8_part1_1")
        day8 = Day8(reader.read_lines())
        self.assertEqual(day8.part1(), 2)

        reader = FileReader("testdata/testdata_day8_part1_2")
        day8 = Day8(reader.read_lines())
        self.assertEqual(day8.part1(), 6)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day8")
        day8 = Day8(reader.read_lines())
        self.assertEqual(day8.part1(), 11309)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day8_part2")
        day8 = Day8(reader.read_lines())
        self.assertEqual(day8.part2(), 6)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day8")
        day8 = Day8(reader.read_lines())
        self.assertEqual(day8.part2(), 13740108158591)

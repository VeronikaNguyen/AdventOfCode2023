import unittest

from days.day16 import Day16
from days.utils import FileReader


class TestDay16(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day16")
        day16 = Day16(reader.read_lines())
        self.assertEqual(day16.part1(), 46)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day16")
        day16 = Day16(reader.read_lines())
        self.assertEqual(day16.part1(), 7415)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day16")
        day16 = Day16(reader.read_lines())
        self.assertEqual(day16.part2(), 51)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day16")
        day16 = Day16(reader.read_lines())
        self.assertEqual(day16.part2(), 7943)

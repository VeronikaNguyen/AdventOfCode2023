import unittest

from days.day7 import Day7
from days.utils import FileReader


class TestDay7(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day7")
        day7 = Day7(reader.read_lines())
        self.assertEqual(day7.part1(), 6440)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day7")
        day7 = Day7(reader.read_lines())
        self.assertEqual(day7.part1(), 247823654)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day7")
        day7 = Day7(reader.read_lines())
        self.assertEqual(day7.part2(), 5905)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day7")
        day7 = Day7(reader.read_lines())
        self.assertEqual(day7.part2(), 245461700)

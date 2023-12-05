import unittest

from days.day5 import Day5
from days.utils import FileReader


class TestDay5(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day5")
        day5 = Day5(reader.read_lines())
        self.assertEqual(day5.part1(), 35)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day5")
        day5 = Day5(reader.read_lines())
        self.assertEqual(day5.part1(), 309796150)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day5")
        day5 = Day5(reader.read_lines())
        self.assertEqual(day5.part2(), 46)

    # def test_part2_solution(self):
    #     reader = FileReader("testdata/data_day5")
    #     day5 = Day5(reader.read_lines())
    #     self.assertEqual(day5.part2(), 5571760)

import math

from days.part_enum import Part


class Day9:
    numbers_list: list[list[int]]

    def __init__(self, lines: list[str]):
        self.numbers_list = []
        self.read_lines(lines)

    def read_lines(self, lines: list[str]) -> None:
        for line in lines:
            numbers = []
            split_line = line.split()
            for number in split_line:
                numbers.append(int(number))
            self.numbers_list.append(numbers)

    def part1(self) -> int:
        last_diff_sum = 0
        for numbers in self.numbers_list:
            last_diff_sum += self.determine_extrapolated_values(numbers)[0]
        return last_diff_sum

    def part2(self):
        first_diff_sum = 0
        for numbers in self.numbers_list:
            first_diff_sum += self.determine_extrapolated_values(numbers)[1]
        return first_diff_sum

    @staticmethod
    def determine_extrapolated_values(numbers: list[int]) -> (int, int):
        difference = numbers
        first_difference = [numbers[0]]
        last_difference = [numbers[-1]]
        difference_not_null = True
        while difference_not_null:
            difference_not_null = False
            temp = []
            for idx in range(len(difference) - 1):
                diff = difference[idx + 1] - difference[idx]
                if diff != 0:
                    difference_not_null = True
                temp.append(diff)
            last_difference.append(temp[-1])
            first_difference.append(temp[0])
            difference = temp

        last_diff, first_diff = 0, 0
        for num in last_difference:
            last_diff += num

        for idx in range(len(first_difference) - 1, -1, -1):
            first_diff = first_difference[idx] - first_diff
        return last_diff, first_diff

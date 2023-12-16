import math

from days.part_enum import Part


class Day8:
    map: dict[str, tuple[str, str]]
    lr_instruction: str

    def __init__(self, lines: list[str]):
        self.map = {}
        self.lr_instruction = ""
        self.read_lines(lines)

    def read_lines(self, lines) -> None:
        self.lr_instruction = lines[0]

        for line in lines[2:]:
            split_line = line.split()
            self.map[split_line[0]] = (split_line[2][1: -1], split_line[3][:-1])

    def part1(self, loc: str) -> int:
        return self.count_steps(loc, Part.Part1)

    def part2(self) -> int:
        starts = []
        for key in self.map:
            if key[2] == "A":
                starts.append(key)
        steps = []
        for start in starts:
            steps.append(self.count_steps(start, Part.Part2))

        result = 1
        for step in steps:
            result = self.determine_least_common_multiple(result, step)
        return result

    def count_steps(self, loc: str, part: Part):
        steps = 0
        while not self.reached_end(loc, part):
            if self.lr_instruction[steps % len(self.lr_instruction)] == "L":
                loc = self.map[loc][0]
            else:
                loc = self.map[loc][1]
            steps += 1
        return steps

    @staticmethod
    def reached_end(loc: str, part: Part):
        if part == Part.Part1:
            return True if loc == "ZZZ" else False
        else:
            return True if loc[2] == "Z" else False

    @staticmethod
    def determine_least_common_multiple(num1: int, num2: int):
        return abs(num1 * num2) // math.gcd(num1, num2)

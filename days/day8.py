from collections import defaultdict
import math


class Day8:

    def __init__(self, lines: list[str]):
        self.map = {}
        self.lr_instruction = ""
        self.read_lines(lines)

    def read_lines(self, lines) -> None:
        self.lr_instruction = lines[0]

        for line in lines[2:]:
            split_line = line.split()
            self.map[split_line[0]] = (split_line[2][1: -1], split_line[3][:-1])
        return

    def part1(self) -> int:
        start = "AAA"
        steps = 0
        while start != "ZZZ":
            if self.lr_instruction[steps % len(self.lr_instruction)] == "L":
                start = self.map[start][0]
            else:
                start = self.map[start][1]
            steps += 1
        return steps

    def part2(self):
        steps = 0
        start = []
        for key in self.map:
            if key[2] == "A":
                start.append(key)
        results = []
        for s in start:
            results.append(self.helper(s))
        res = 1
        for s in results:
            res = self.lcm(s, res)
        return res

    def helper(self, start):
        steps = 0
        while start[2] != "Z":
            if self.lr_instruction[steps % len(self.lr_instruction)] == "L":
                start = self.map[start][0]
            else:
                start = self.map[start][1]
            steps += 1
        return steps

    def lcm(self, a, b):
        return abs(a * b) // math.gcd(a, b)

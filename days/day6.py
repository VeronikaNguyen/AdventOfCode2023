from days.part_enum import Part


class Day6:
    lines: list[str]
    time: list[int]
    distance: list[int]

    def __init__(self, lines: list[str]):
        self.lines = lines
        self.time = []
        self.distance = []

    def read_lines(self, part: Part) -> None:
        if part == Part.Part1:
            for idx in range(len(self.lines[0].split())):
                self.time = [int(num) for num in self.lines[0].split()[1:]]
                self.distance = [int(num) for num in self.lines[1].split()[1:]]
        elif part == Part.Part2:
            self.time = [int("".join(self.lines[0].split()[1:]))]
            self.distance = [int("".join(self.lines[1].split()[1:]))]

    def part1(self) -> int:
        self.read_lines(Part.Part1)
        return self.determine_sum_of_ways_to_win()

    def part2(self) -> int:
        self.read_lines(Part.Part2)
        return self.determine_sum_of_ways_to_win()

    def determine_sum_of_ways_to_win(self) -> int:
        res = 1
        for idx, time in enumerate(self.time):
            ways_to_win = 0
            for hold_time in range(time):
                if (time - hold_time) * hold_time > self.distance[idx]:
                    ways_to_win += 1
            res *= ways_to_win
        return res

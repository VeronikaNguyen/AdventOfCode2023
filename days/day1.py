class Day1:
    lines: list
    number_map: dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    max_number_length: int = max(len(key) for key in number_map)

    def __init__(self, lines: list):
        self.lines = lines

    def part1(self) -> int:
        return self.combine_first_and_last_number(1)

    def part2(self) -> int:
        return self.combine_first_and_last_number(2)

    def combine_first_and_last_number(self, part: int) -> int:
        result = 0
        for line in self.lines:
            first_number = self.read_first_number_in_line(line, part)
            second_number = self.read_last_number_in_line(line, part)
            result += first_number * 10 + second_number
        return result

    @staticmethod
    def read_first_number_in_line(line: str, part: int) -> int:
        for idx, character in enumerate(line):
            if character.isdigit():
                number = int(character)
                return number
            window = line[max(0, idx - 5): idx + 1]
            if part == 2:
                for key in Day1.number_map:
                    if key in window:
                        number = Day1.number_map[key]
                        return number

    @staticmethod
    def read_last_number_in_line(line: str, part: int) -> int:
        for idx in range(len(line) - 1, -1, -1):
            character = line[idx]
            if character.isdigit():
                number = int(character)
                return number
            window = line[idx: min(len(line), idx + 6)]
            if part == 2:
                for key in Day1.number_map:
                    if key in window:
                        number = Day1.number_map[key]
                        return number

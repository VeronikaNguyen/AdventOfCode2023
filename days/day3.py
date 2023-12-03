from collections import defaultdict
import numpy as np


class Day3:
    matrix: np.array  # input matrix containing numbers -> digit: >=0, no symbol: -1, gear symbol: -2, other symbols: -3
    part_number_matrix: np.array  # matrix marking digits which are adjacent to symbols
    gear_map: defaultdict[tuple[int, int], set]  # maps each gear, tuple of indices, to a set of number indices
    gear_matrix: np.array  # matrix marking gear symbols and counting how many parts are numbers are adjacent to them
    number_matrix: np.array  # maps each digit to a number index
    number_map: defaultdict[int, int]  # maps each number index to a number

    def __init__(self, lines: list[str]):
        self.matrix = np.zeros(shape=(len(lines), len(lines[0])), dtype=int)
        self.read_lines(lines)

        self.part_number_matrix = np.zeros_like(self.matrix, dtype=bool)
        self.gear_matrix = np.zeros_like(self.matrix, dtype=int)
        self.gear_map = defaultdict(set)
        self.number_matrix = np.zeros_like(self.matrix, dtype=int)
        self.number_map = defaultdict(int)

    def read_lines(self, lines: list[str]):
        for i, line in enumerate(lines):
            for j, character in enumerate(line):
                if character.isdigit():
                    self.matrix[i, j] = int(character)
                elif character == ".":
                    self.matrix[i, j] = -1          # no symbol
                elif character == "*":
                    self.matrix[i, j] = -2          # gear symbol
                else:
                    self.matrix[i, j] = -3          # symbol except gear symbol

    def part1(self) -> int:
        self.init_part_number_matrix()
        self.init_number_matrix_and_map()
        result = 0
        seen_numbers = set()
        for (i, j), value in np.ndenumerate(self.matrix):
            if value >= 0:
                if self.part_number_matrix[i, j] and self.number_matrix[i, j] not in seen_numbers:
                    seen_numbers.add(self.number_matrix[i, j])
                    result += self.number_map[int(self.number_matrix[i, j])]
        return result

    def part2(self) -> int:
        self.init_number_matrix_and_map()
        self.init_gear_matrix_and_map()
        result = 0
        for (i, j), value in np.ndenumerate(self.gear_matrix):
            if value == 2:
                product = 1
                for number in self.gear_map[i, j]:
                    product *= self.number_map[number]
                result += product
        return result

    def init_number_matrix_and_map(self) -> None:
        number_idx = 1
        number = 0
        belongs_to_number = False
        for (i, j), value in np.ndenumerate(self.matrix):
            if value >= 0:
                self.number_matrix[i, j] = number_idx
                if belongs_to_number:
                    number = number * 10 + value
                else:
                    number = value
                    belongs_to_number = True
            else:
                self.number_map[number_idx] = number
                belongs_to_number = False
                number = 0
                number_idx += 1

    def init_part_number_matrix(self) -> None:
        for (i, j), value in np.ndenumerate(self.matrix):
            if value <= -2:
                for x in range(max(i - 1, 0), min(i + 2, self.matrix.shape[0])):
                    for y in range(max(j - 1, 0), min(j + 2, self.matrix.shape[1])):
                        self.part_number_matrix[x, y] = True

    def init_gear_matrix_and_map(self) -> None:
        for (i, j), value in np.ndenumerate(self.matrix):
            if value == -2:
                for x in range(max(i - 1, 0), min(i + 2, self.matrix.shape[0])):
                    for y in range(max(j - 1, 0), min(j + 2, self.matrix.shape[1])):
                        if self.number_matrix[x, y] > 0 and self.number_matrix[x, y] not in self.gear_map[(i, j)]:
                            self.gear_matrix[i, j] += 1
                            self.gear_map[(i, j)].add(self.number_matrix[x, y])

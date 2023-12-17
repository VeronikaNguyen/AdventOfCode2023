from collections import defaultdict
import numpy as np


class Day14:
    def __init__(self, lines: list[str]):
        self.matrix = np.zeros(shape=(len(lines), len(lines[0])), dtype=int)
        self.read_lines(lines)

    def read_lines(self, lines: list[str]) -> None:
        for x, line in enumerate(lines):
            for y, character in enumerate(line):
                if character == 'O':
                    self.matrix[x, y] = 1
                elif character == '#':
                    self.matrix[x, y] = 2
                else:
                    self.matrix[x, y] = 0

    def part1(self) -> int:
        self.tilt_matrix()
        return self.compute_load()

    def part2(self) -> int:
        num_cycles, cycle_length = 1000000000, 1
        seen_matrices = dict()
        for cycle in range(1, num_cycles):
            self.tilt_matrix_per_cycle()
            if self.matrix.tobytes() in seen_matrices:
                cycle_length = cycle - seen_matrices[self.matrix.tobytes()]
                break
            seen_matrices[self.matrix.tobytes()] = cycle
        for iterations in range((num_cycles - seen_matrices[self.matrix.tobytes()]) % cycle_length):
            self.tilt_matrix_per_cycle()
        return self.compute_load()

    def tilt_matrix(self) -> None:
        tilted_matrix = np.zeros_like(self.matrix)
        for y in range(self.matrix.shape[1]):
            rock_map = defaultdict(int)
            cube_map = {0: -1}
            cube_idx = 0
            for x in range(self.matrix.shape[0]):
                if self.matrix[x, y] == 1:
                    rock_map[cube_idx] += 1
                elif self.matrix[x, y] == 2:
                    cube_idx += 1
                    cube_map[cube_idx] = x
                    tilted_matrix[x, y] = 2

            for cube_idx in rock_map:
                for rock in range(rock_map[cube_idx]):
                    tilted_matrix[cube_map[cube_idx] + 1 + rock, y] = 1
        self.matrix = tilted_matrix

    def compute_load(self) -> int:
        result = 0
        for y in range(self.matrix.shape[1]):
            for x in range(self.matrix.shape[0]):
                if self.matrix[x, y] == 1:
                    result += self.matrix.shape[0] - x
        return result

    def tilt_matrix_per_cycle(self) -> None:
        self.tilt_matrix()                  # north
        self.matrix = np.rot90(self.matrix, 3)
        self.tilt_matrix()                  # west
        self.matrix = np.rot90(self.matrix, 3)
        self.tilt_matrix()                  # south
        self.matrix = np.rot90(self.matrix, 3)
        self.tilt_matrix()                  # east
        self.matrix = np.rot90(self.matrix, 3)

from collections import defaultdict

from days.part_enum import Part


class Day5:
    keys: defaultdict[int, set[tuple]]
    maps_keys: defaultdict[int, list[tuple]]
    maps_values: defaultdict[int, list[tuple]]

    def __init__(self, lines: list[str]):
        self.keys = defaultdict(set)
        self.map_keys = defaultdict(list)
        self.map_values = defaultdict(list)
        self.lines = lines

    def read_lines(self, part: Part) -> None:
        map_idx = -1
        for line in self.lines:
            split_line = line.split()
            if len(split_line) == 0:
                map_idx += 1
            elif map_idx == -1:      # read seed values and write it into keys[0]
                if part == Part.Part1:
                    for idx in range(1, len(split_line)):
                        self.keys[0].add((int(split_line[idx]), int(split_line[idx])))
                elif part == Part.Part2:
                    for idx in range(1, len(split_line), 2):
                        self.keys[0].add((int(split_line[idx]), int(split_line[idx]) + int(split_line[idx + 1]) - 1))
            elif len(split_line) == 3:
                self.map_keys[map_idx].append((int(split_line[1]), int(split_line[1]) + int(split_line[2]) - 1))
                self.map_values[map_idx].append((int(split_line[0]), int(split_line[0]) + int(split_line[2]) - 1))

    def part1(self) -> int:
        self.read_lines(Part.Part1)
        return self.compute_mapping_solution()

    def part2(self) -> int:
        self.read_lines(Part.Part2)
        return self.compute_mapping_solution()

    def compute_mapping_solution(self) -> int:
        for map_idx in range(len(self.map_keys)):
            for idx, map_key in enumerate(self.map_keys[map_idx]):
                seen_keys = set()
                while len(self.keys[map_idx]) > 0:
                    key = list(self.keys[map_idx])[0]
                    if map_key[0] <= key[0] and key[1] <= map_key[1]:
                        self.keys[map_idx + 1].add((
                            self.map_values[map_idx][idx][0] + key[0] - map_key[0],
                            self.map_values[map_idx][idx][0] + key[1] - map_key[0]
                        ))
                    elif key[0] <= map_key[0] and map_key[1] <= key[1]:
                        self.keys[map_idx + 1].add((
                            self.map_values[map_idx][idx][0],
                            self.map_values[map_idx][idx][1]
                        ))
                        if key[0] < map_key[0]:
                            seen_keys.add((
                                key[0], map_key[1] - 1
                            ))
                        if map_key[1] < key[1]:
                            seen_keys.add((
                                map_key[1] + 1, key[1]
                            ))
                    elif key[0] <= map_key[1] < key[1]:
                        self.keys[map_idx + 1].add((
                            self.map_values[map_idx][idx][0] + key[0] - map_key[0],
                            self.map_values[map_idx][idx][1]
                        ))
                        seen_keys.add((
                            map_key[1] + 1, key[1]
                        ))
                    elif key[0] < map_key[0] <= key[1]:
                        self.keys[map_idx + 1].add((
                            self.map_values[map_idx][idx][0],
                            self.map_values[map_idx][idx][0] + key[1] - map_key[0]
                        ))
                        seen_keys.add((
                            key[0], map_key[1] - 1
                        ))
                    else:
                        seen_keys.add(key)
                    self.keys[map_idx].remove(key)
                for key in seen_keys:
                    self.keys[map_idx].add(key)
            for key in self.keys[map_idx]:
                self.keys[map_idx + 1].add(key)
        print(sorted([tup[0] for tup in list(self.keys[len(self.keys) - 1])]))
        return min([tup[0] for tup in list(self.keys[len(self.keys) - 1])])

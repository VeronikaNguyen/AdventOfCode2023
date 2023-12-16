from collections import defaultdict


class Day15:
    instructions: list[str]
    boxes: defaultdict[int, list[tuple[str, int]]]
    hashmap: defaultdict[str, tuple[int, int]]

    def __init__(self, lines: list[str]):
        self.read_lines(lines)
        self.boxes = defaultdict(list)
        self.hashmap = defaultdict(lambda: (-1, -1))

    def read_lines(self, lines: list[str]) -> None:
        self.instructions = lines[0].split(',')

    def part1(self) -> int:
        result = 0
        for instruction in self.instructions:
            result += self.determine_hash(instruction)
        return result

    def part2(self) -> int:
        for instruction in self.instructions:
            if instruction[-1] == '-':
                label = instruction[:-1]
                if self.hashmap[label] != (-1, -1):
                    self.boxes[self.hashmap[label][0]].pop(self.hashmap[label][1])
                    for element in self.boxes[self.hashmap[label][0]][self.hashmap[label][1]:]:
                        self.hashmap[element[0]] = (self.hashmap[element[0]][0], self.hashmap[element[0]][1] - 1)
                    self.hashmap[label] = (-1, -1)
            else:
                label_number = instruction.split('=')
                label, number = label_number[0], int(label_number[1])
                if self.hashmap[label] != (-1, -1):
                    self.boxes[self.hashmap[label][0]][self.hashmap[label][1]] = (label, number)
                else:
                    self.hashmap[label] = (self.determine_hash(label), len(self.boxes[self.determine_hash(label)]))
                    self.boxes[self.determine_hash(label)].append((label, number))
        result = 0
        for box_idx in self.boxes:
            for slot, instruction in enumerate(self.boxes[box_idx]):
                result += (slot + 1) * (box_idx + 1) * instruction[1]
        return result

    @staticmethod
    def determine_hash(string: str) -> int:
        current_value = 0
        for char in string:
            current_value += ord(char)
            current_value *= 17
            current_value = current_value % 256
        return current_value

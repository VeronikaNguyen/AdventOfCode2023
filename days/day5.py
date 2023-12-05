from collections import defaultdict

class Day5:

    def __init__(self, lines: list[str]):
        self.lines = lines
        self.seeds = defaultdict(list)
        self.soil = defaultdict(list)
        self.intersections = defaultdict(list)
        self.intersections_map = defaultdict(list)

    def part1(self) -> int:
        counter = 0
        seen = set()
        for l in self.lines:
            line = l.split()
            if len(line) == 0:
                counter += 1
                if counter >= 2:
                    for seed in self.soil[counter - 2]:
                        if seed not in seen:
                            self.soil[counter - 1].append(seed)
                    seen = set()
            elif counter == 0:
                for word in line[1:]:
                    self.soil[0].append(int(word))
            elif len(line) == 3:
                ls = [int(num) for num in line]
                for seed in self.soil[counter - 1]:
                    if ls[1] <= seed <= ls[1] + ls[2]:
                        seen.add(seed)
                        self.soil[counter].append(ls[0] + seed - ls[1])

        return min([num for num in self.soil[7]])

    def part2(self) -> int:
        counter = 0
        for l in self.lines:
            line = l.split()
            if len(line) == 0:
                counter += 1
            elif counter == 0:
                isStart = True
                startNumber = 0
                for word in line[1:]:
                    if isStart:
                        startNumber = int(word)
                        isStart = False
                    else:
                        self.seeds[0].append(tuple([startNumber, startNumber + int(word) - 1]))
                        self.soil[0].append(tuple([startNumber, startNumber + int(word) - 1]))
                        isStart = True
            elif len(line) == 3:
                ls = [int(num) for num in line]
                self.intersections[counter].append(tuple([ls[1], ls[1] + ls[2] - 1]))
                self.intersections_map[counter].append(tuple([ls[0], ls[0] + ls[2] - 1]))

        counter = 0
        for idx in range(1, 8):
            for intersections_idx, value in enumerate(self.intersections[idx]):
                t0, t1 = value      # interval start and end values
                for s0, s1 in self.soil[counter]:
                    if t0 <= s0 and s1 <= t1:
                        start = self.intersections_map[idx][intersections_idx][0] + s0 - t0
                        end = self.intersections_map[idx][intersections_idx][0] + s1 - t0
                        self.seeds[idx].append(tuple([start, end]))
                    elif t0 <= s0 and s1 > t1:
                        start = self.intersections_map[idx][intersections_idx][0] + s0 - t0
                        end = self.intersections_map[idx][intersections_idx][1]
                        self.seeds[idx].append(tuple([start, end]))

                        start = s1 + 1
                        end = t1
                        self.soil[counter + 1].append(tuple([start, end]))
                    elif s1 >= t1 and s0 < t0:
                        start = self.intersections_map[idx][intersections_idx][0]
                        end = self.intersections_map[idx][intersections_idx][0] + s1 - t0
                        self.seeds[idx].append(tuple([start, end]))

                        start = s0
                        end = t0 - 1
                        self.soil[counter + 1].append(tuple([start, end]))
                    elif t0 >= s0 and s1 >= t1:
                        start = self.intersections_map[idx][intersections_idx][0]
                        end = self.intersections_map[idx][intersections_idx][1]
                        self.seeds[idx].append(tuple([start, end]))

                        if s1 > t1:
                            start = s1 + 1
                            end = t1
                            self.soil[counter + 1].append(tuple([start, end]))
                        if t0 > s0:
                            start = s0
                            end = t0 - 1
                            self.soil[counter + 1].append(tuple([start, end]))
                    else:
                        self.soil[counter + 1].append(tuple([s0, s1]))
                    counter += 1
            for value in self.soil[counter]:
                self.soil[counter + 1].append(value)
            for value in self.seeds[idx]:
                self.soil[counter + 1].append(value)
            counter += 1

        return 1
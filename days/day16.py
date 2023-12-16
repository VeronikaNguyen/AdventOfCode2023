
class Day16:
    contraption: list[str]

    def __init__(self, lines: list[str]):
        self.contraption = []
        self.x_len, self.y_len = len(lines), len(lines[0])
        self.read_lines(lines)

    def read_lines(self, lines: list[str]) -> None:
        for line in lines:
            self.contraption.append(line)

    def part1(self) -> int:
        if self.contraption[0][0] == '|' or self.contraption[0][0] == '\\':
            beams = [(0, 0, 'd')]
        elif self.contraption[0][0] == '/':
            beams = [(0, 0, 'u')]
        else:
            beams = [(0, 0, 'r')]
        return self.compute_energized_tiles(beams)

    def part2(self) -> int:
        max_energized_tiles = 0
        for x in range(self.x_len):
            if self.contraption[x][0] == '|':
                beams = [(x, 0, 'd'), (x, 0, 'u')]
            elif self.contraption[x][0] == '\\':
                beams = [(x, 0, 'd')]
            elif self.contraption[x][0] == '/':
                beams = [(x, 0, 'u')]
            else:
                beams = [(x, 0, 'r')]
            max_energized_tiles = max(self.compute_energized_tiles(beams), max_energized_tiles)

            if self.contraption[x][self.y_len - 1] == '|':
                beams = [(x, self.y_len - 1, 'd'), (x, self.y_len - 1, 'u')]
            elif self.contraption[x][self.y_len - 1] == '\\':
                beams = [(x, self.y_len - 1, 'u')]
            elif self.contraption[x][self.y_len - 1] == '/':
                beams = [(x, self.y_len - 1, 'd')]
            else:
                beams = [(x, self.y_len - 1, 'r')]
            max_energized_tiles = max(self.compute_energized_tiles(beams), max_energized_tiles)

        for y in range(self.y_len):
            if self.contraption[0][y] == '-':
                beams = [(0, y, 'l'), (0, y, 'r')]
            elif self.contraption[0][y] == '\\':
                beams = [(0, y, 'r')]
            elif self.contraption[0][y] == '/':
                beams = [(0, y, 'l')]
            else:
                beams = [(0, y, 'd')]
            max_energized_tiles = max(self.compute_energized_tiles(beams), max_energized_tiles)

            if self.contraption[self.x_len - 1][y] == '-':
                beams = [(self.x_len - 1, y, 'l'), (self.x_len - 1, y, 'r')]
            elif self.contraption[self.x_len - 1][y] == '\\':
                beams = [(self.x_len - 1, y, 'r')]
            elif self.contraption[self.x_len - 1][y] == '/':
                beams = [(self.x_len - 1, y, 'l')]
            else:
                beams = [(self.x_len - 1, y, 'd')]
            max_energized_tiles = max(self.compute_energized_tiles(beams), max_energized_tiles)
        return max_energized_tiles

    def compute_energized_tiles(self, beams: list[tuple[int, int, str]]) -> int:
        seen_beams = set()
        while len(beams) > 0:
            beam = beams.pop(0)
            if beam not in seen_beams:
                seen_beams.add(beam)
                if beam[2] == 'r' and beam[1] < self.y_len - 1:
                    if self.contraption[beam[0]][beam[1] + 1] == '.' or self.contraption[beam[0]][beam[1] + 1] == '-':
                        beams.append((beam[0], beam[1] + 1, 'r'))
                    elif self.contraption[beam[0]][beam[1] + 1] == '|':
                        beams.append((beam[0], beam[1] + 1, 'u'))
                        beams.append((beam[0], beam[1] + 1, 'd'))
                    elif self.contraption[beam[0]][beam[1] + 1] == '/':
                        beams.append((beam[0], beam[1] + 1, 'u'))
                    elif self.contraption[beam[0]][beam[1] + 1] == '\\':
                        beams.append((beam[0], beam[1] + 1, 'd'))
                elif beam[2] == 'l' and beam[1] > 0:
                    if self.contraption[beam[0]][beam[1] - 1] == '.' or self.contraption[beam[0]][beam[1] - 1] == '-':
                        beams.append((beam[0], beam[1] - 1, 'l'))
                    elif self.contraption[beam[0]][beam[1] - 1] == '|':
                        beams.append((beam[0], beam[1] - 1, 'u'))
                        beams.append((beam[0], beam[1] - 1, 'd'))
                    elif self.contraption[beam[0]][beam[1] - 1] == '/':
                        beams.append((beam[0], beam[1] - 1, 'd'))
                    elif self.contraption[beam[0]][beam[1] - 1] == '\\':
                        beams.append((beam[0], beam[1] - 1, 'u'))
                elif beam[2] == 'd' and beam[0] < self.x_len - 1:
                    if self.contraption[beam[0] + 1][beam[1]] == '.' or self.contraption[beam[0] + 1][beam[1]] == '|':
                        beams.append((beam[0] + 1, beam[1], 'd'))
                    elif self.contraption[beam[0] + 1][beam[1]] == '-':
                        beams.append((beam[0] + 1, beam[1], 'l'))
                        beams.append((beam[0] + 1, beam[1], 'r'))
                    elif self.contraption[beam[0] + 1][beam[1]] == '/':
                        beams.append((beam[0] + 1, beam[1], 'l'))
                    elif self.contraption[beam[0] + 1][beam[1]] == '\\':
                        beams.append((beam[0] + 1, beam[1], 'r'))
                elif beam[2] == 'u' and beam[0] > 0:
                    if self.contraption[beam[0] - 1][beam[1]] == '.' or self.contraption[beam[0] - 1][beam[1]] == '|':
                        beams.append((beam[0] - 1, beam[1], 'u'))
                    elif self.contraption[beam[0] - 1][beam[1]] == '-':
                        beams.append((beam[0] - 1, beam[1], 'l'))
                        beams.append((beam[0] - 1, beam[1], 'r'))
                    elif self.contraption[beam[0] - 1][beam[1]] == '/':
                        beams.append((beam[0] - 1, beam[1], 'r'))
                    elif self.contraption[beam[0] - 1][beam[1]] == '\\':
                        beams.append((beam[0] - 1, beam[1], 'l'))
        energized_tiles = {(beam[0], beam[1]) for beam in seen_beams}
        return len(energized_tiles)

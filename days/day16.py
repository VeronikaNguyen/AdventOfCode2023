
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
        seen_beams = set()
        if self.contraption[0][0] == '|' or self.contraption[0][0] == '\\':
            beams = [(0, 0, 'd')]
        elif self.contraption[0][0] == '/':
            beams = [(0, 0, 'u')]
        else:
            beams = [(0, 0, 'r')]
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

    def part2(self) -> int:
        return 1

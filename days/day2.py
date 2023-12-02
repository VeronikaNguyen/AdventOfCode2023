import dataclasses
import re


@dataclasses.dataclass
class Game:
    number: int
    red: int
    green: int
    blue: int


class Day2:
    games: list[Game]

    def __init__(self, lines: list[str]):
        self.games = []
        self.read_lines(lines)

    def read_lines(self, lines: list[str]):
        for line in lines:
            game_number = re.match(r"Game (?P<game_number>\d+):", line).group("game_number")
            colour_map = {"red": 0,  "blue": 0, "green": 0}
            for number, colour in re.findall(r"(?P<cubes_number>\d+) (green|blue|red)", line):
                colour_map[colour] = max(int(number), colour_map[colour])
            self.games.append(Game(int(game_number), colour_map["red"], colour_map["green"], colour_map["blue"]))

    def part1(self) -> int:
        valid_games = 0
        bag = Game(0, 12, 13, 14)
        for game in self.games:
            if bag.red >= game.red and bag.green >= game.green and bag.blue >= game.blue:
                valid_games += game.number
        return valid_games

    def part2(self) -> int:
        power_sum = 0
        for game in self.games:
            power_sum += game.red * game.green * game.blue
        return power_sum



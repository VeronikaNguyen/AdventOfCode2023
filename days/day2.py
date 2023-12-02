class Day2:
    lines: list

    def __init__(self, lines: list):
        self.lines = lines

    def part1(self) -> int:
        bag = {
            "red": 12,
            "green": 13,
            "blue": 14
        }
        impossible_games = 0
        games = 0
        for idx, line in enumerate(self.lines):
            games += idx + 1
            line = line.replace(",", "")
            line = line.replace(";", "")
            is_number = True
            number = 0
            for word in line.split(" ")[2:]:
                if is_number:
                    number = int(word)
                    is_number = False
                else:
                    is_number = True
                    if bag[word] < number:
                        impossible_games += idx + 1
                        break
        return games - impossible_games

    def part2(self) -> int:
        power_sum = 0
        for idx, line in enumerate(self.lines):
            bag = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            line = line.replace(",", "")
            line = line.replace(";", "")
            is_number = True
            number = 0
            for word in line.split(" ")[2:]:
                if is_number:
                    number = int(word)
                    is_number = False
                else:
                    is_number = True
                    if bag[word] < number:
                        bag[word] = number
            power = 1
            for key in bag:
                power *= bag[key]
            power_sum += power
        return power_sum

    def part(self) -> int:
        result = 0
        impossible_games = 0
        games = 0
        for idx, line in enumerate(self.lines):
            games += idx + 1
            line = line.replace(",", "")
            line = line.replace(";", "")
            is_number = True
            number = 0
            for word in line.split(" ")[2:]:
                if is_number:
                    number = int(word)
                    is_number = False
                else:
                    is_number = True
                    if self.bag[word] < number:
                        impossible_games += idx + 1
                        break
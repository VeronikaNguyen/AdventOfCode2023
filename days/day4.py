from collections import defaultdict
import dataclasses


@dataclasses.dataclass
class Card:
    number: int
    matches: int


class Day4:
    lines: list[str]
    cards: list[Card]

    def __init__(self, lines: list[str]):
        self.lines = lines
        self.cards = []
        self.read_lines()

    def read_lines(self) -> None:
        for line in self.lines:
            matches = 0
            is_winning_number = True
            winning_numbers = set()
            card_number = int(line.split()[1][:-1])
            for word in line.split()[2:]:
                if word == "|":
                    is_winning_number = False
                elif is_winning_number:
                    winning_numbers.add(int(word))
                elif int(word) in winning_numbers:
                    matches += 1
            self.cards.append(Card(card_number, matches))

    def part1(self) -> int:
        result = 0
        for card in self.cards:
            if card.matches > 0:
                result += 2 ** (card.matches - 1)
        return result

    def part2(self) -> int:
        result = 0
        win_copies = defaultdict(lambda: 1)
        for card in self.cards:
            if card.number not in win_copies.keys():
                win_copies[card.number] = 1
            for i in range(card.matches):
                win_copies[card.number + i + 1] += win_copies[card.number]
        for key in win_copies:
            result += win_copies[key]
        return result

from collections import defaultdict

from days.part_enum import Part


class Day7:
    card_order: list[str]
    card_strength: dict[str, int]
    hand: list[str]
    bid: dict[str, int]

    def __init__(self, lines: list[str]):
        self.card_order = []
        self.card_strength = {}
        self.hand = []
        self.bid = {}
        self.read_lines(lines)

    def read_lines(self, lines: list[str]) -> None:
        for line in lines:
            self.hand.append(line.split()[0])
            self.bid[line.split()[0]] = int(line.split()[1])

    def part1(self) -> int:
        self.card_order = [str(num) for num in range(2, 10)] + ["T", "J", "Q", "K", "A"]
        self.card_strength = {card: idx for idx, card in enumerate(self.card_order)}
        return self.compute_total_winnings(Part.Part1)

    def part2(self) -> int:
        self.card_order = ["J"] + [str(num) for num in range(2, 10)] + ["T", "Q", "K", "A"]
        self.card_strength = {card: idx for idx, card in enumerate(self.card_order)}
        return self.compute_total_winnings(Part.Part2)

    def compute_total_winnings(self, part: Part) -> int:
        ordered_hand = []
        ordered = False
        for hand in self.hand:
            for idx, o_hand in enumerate(ordered_hand):
                if self.determine_value_of_hand(hand, part) < self.determine_value_of_hand(o_hand, part):
                    ordered_hand.insert(idx, hand)
                    ordered = True
                    break
                if self.determine_value_of_hand(hand, part) == self.determine_value_of_hand(o_hand, part):
                    if self.compare_two_equal_value_hands(hand, o_hand) == 2:
                        ordered_hand.insert(idx, hand)
                        ordered = True
                        break
            if not ordered:
                ordered_hand.append(hand)
            ordered = False
        result = 0
        for rank, hand in enumerate(ordered_hand):
            result += (rank + 1) * self.bid[hand]
        return result

    @staticmethod
    def determine_value_of_hand(hand: str, part: Part) -> int:
        num_J = 0
        if part == Part.Part2:
            for card in hand:
                if card == "J":
                    num_J += 1

        cards = defaultdict(lambda: 0)
        for card in hand:
            cards[card] += 1

        keys = cards.keys()
        if len(keys) == 1:
            return 8                # five of a kind
        elif len(keys) == 2:
            for key in keys:
                if cards[key] == 4 and num_J == 0:
                    return 7        # four of a kind
                elif cards[key] == 4 and num_J == 1:
                    return 8        # five of a kind
            else:
                if num_J == 0:
                    return 6        # full house
                else:
                    return 8        # five of a kind
        elif len(keys) == 3:
            for key in keys:
                if cards[key] == 3 and num_J == 0:
                    return 5        # three of a kind
                elif cards[key] == 3 and num_J == 1:
                    return 7        # four of a kind
                elif cards[key] == 3 and num_J == 3:
                    return 7        # four of a kind
            else:
                if num_J == 0:
                    return 4        # two pair
                elif num_J == 1:
                    return 6        # full house
                if num_J == 2:
                    return 7        # four of a kind
        elif len(keys) == 4:
            if num_J == 0:
                return 3            # one pair
            elif num_J == 1:
                return 5            # three of a kind
            elif num_J == 2:
                return 5            # three of a kind
        else:
            if num_J == 0:
                return 2            # high card
            else:
                return 3            # one pair

    def compare_two_equal_value_hands(self, hand_one: str, hand_two: str) -> int:
        for idx, h1 in enumerate(hand_one):
            h2 = hand_two[idx]
            if h1 != h2:
                if self.card_strength[h1] > self.card_strength[h2]:
                    return 1
                else:
                    return 2

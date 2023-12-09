from collections import Counter

hands = []
bets = []

possible_hands = [
    "high card",
    "one pair",
    "two pair",
    "three of a kind",
    "full house",
    "four of a kind",
    "five of a kind",
]

possible_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def determine_hand(hand, part2=False):
    keys = Counter(hand).keys()
    values = Counter(hand).values()

    if part2:
        if "J" in hand:
            values = list(values)
            idx_max_value = values.index(max(values))
            num_j = values[list(keys).index("J")]
            if list(keys).index("J") != idx_max_value:
                values[idx_max_value] += num_j
                values[list(keys).index("J")] -= num_j
            elif (
                list(keys).index("J") == idx_max_value
                and len(y := [i for i, x in enumerate(values) if x == num_j]) > 1
            ):
                values[y[1]] += num_j
                values[list(keys).index("J")] -= num_j
            elif list(keys).index("J") == idx_max_value and len(values) > 1:
                values[
                    [values.index(x) for x in sorted(values, reverse=True)][1]
                ] += num_j
                values[list(keys).index("J")] -= num_j

    # check double pairs
    indices = [i for i, x in enumerate(values) if x == 2]

    if 5 in values:
        return "five of a kind"
    elif 4 in values:
        return "four of a kind"
    elif 3 in values and 2 in values:
        return "full house"
    elif 3 in values:
        return "three of a kind"
    elif len(indices) == 2:
        return "two pair"
    elif 2 in values:
        return "one pair"
    else:
        return "high card"


def collect_hand_types(data, hand_type):
    keys = []
    for k, v in data.items():
        if v["hand_type"] == hand_type:
            keys.append(k)
    return keys


def determine_order_within_handtype(cards, card_order):
    cards_tup = []
    for card in cards:
        numeric_card = tuple(card_order.index(str(i)) for i in card)
        cards_tup.append((numeric_card, card))

    ordered_cards = sorted(cards_tup, key=lambda x: x[0])
    return [i[1] for i in ordered_cards]


def determine_rank(data, all_hands=possible_hands, all_cards=possible_cards):
    ranked_keys = []
    for item in all_hands:
        hands = collect_hand_types(data, item)
        order_hands = determine_order_within_handtype(hands, all_cards)
        ranked_keys.extend(order_hands)

    for idx, hand in enumerate(ranked_keys):
        data[hand]["rank"] = idx + 1

    return data


def calc_winnings(data):
    money = 0
    for i in data:
        money += data[i]["rank"] * data[i]["bet"]

    return money


with open("input/day07.txt") as f:
    for line in f:
        a, b = line.split()
        hands.append(a)
        bets.append(int(b))

data = {}
for idx, hand in enumerate(hands):
    temp = {}
    temp["hand_type"] = determine_hand(hand)
    temp["bet"] = bets[idx]

    data[hand] = temp

data = determine_rank(data)
print(f"Day 7 part 1 {calc_winnings(data)}")

card_order2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

data2 = {}
for idx, hand in enumerate(hands):
    temp = {}
    temp["hand_type"] = determine_hand(hand, part2=True)
    temp["bet"] = bets[idx]

    # if "J" in hand:
    #     print("here")

    data2[hand] = temp

data2 = determine_rank(data2, all_cards=card_order2)
print(f"Day 7 part 2 {calc_winnings(data2)}")

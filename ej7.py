DATA_PATH = 'data/ej7.txt'
from collections import Counter

CARDS = 'AKQJT98765432J'
CARDS_VALUES = {card: value for value, card in enumerate(CARDS)}

def get_hand_type(hand):
    c = Counter(hand)
    values = c.values()
    if 5 in values:
        return 0
    if 4 in values:
        return 1
    if 3 in values:
        if 2 in values:
            return 2
        return 3
    if len([v for v in values if v==2]) == 2:
        return 4
    if 2 in values:
        return 5
    return 6

def get_hand_typev2(hand):
    c = Counter(hand)
    jokers = c.pop('J', 0)
    values = c.values()
    if not values:
        return 0
    if max(values) + jokers == 5:
        return 0
    if max(values) + jokers == 4:
        return 1
    if max(values) + jokers == 3:
        if len([v for v in values if v>=2]) == 2:
            return 2
        return 3
    if (len([v for v in values if v==2]) + jokers) == 2:
        return 4
    if max(values) + jokers == 2:
        return 5
    return 6

def get_cards_values(hand):
    res = 0
    for card in hand:
        res *= 13
        res += CARDS_VALUES[card]
    return res

def get_hand_value(hand):
    return 13**5 * get_hand_type(hand) + get_cards_values(hand)

def get_cards_valuesv2(hand):
    res = 0
    for card in hand:
        res *= 14
        res += CARDS_VALUES[card]
    return res

def get_hand_valuev2(hand):
    return 14**5 * get_hand_typev2(hand) + get_cards_valuesv2(hand)

def ej1():
    with open(DATA_PATH) as file:
        hands, bids = list(zip(*[line.split(" ") for line in file.read().splitlines()]))

    hand_values = [get_hand_value(hand) for hand in hands]
    
    sorted_hands = sorted([(hand_value, bid) for hand_value, bid in zip(hand_values, bids)], reverse=True)
    score = sum(int(hand[1])*(rank+1) for rank, hand in enumerate(sorted_hands))
    print(score)

def ej2():
    with open(DATA_PATH) as file:
        hands, bids = list(zip(*[line.split(" ") for line in file.read().splitlines()]))

    hand_values = [get_hand_valuev2(hand) for hand in hands]
    
    sorted_hands = sorted([(hand_value, bid) for hand_value, bid in zip(hand_values, bids)], reverse=True)
    score = sum(int(hand[1])*(rank+1) for rank, hand in enumerate(sorted_hands))
    print(score)

if __name__ == "__main__":
    ej1()
    ej2()

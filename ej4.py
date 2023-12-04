DATA_PATH = 'data/ej4.txt'
import re
from collections import defaultdict


def split_id_game(line):
    line = line.split(":")
    id = int(line[0][5:])
    return id, line[1]

def process_game(game):
    winning_ns, playing_ns = game.split("|")
    winning_ns = [int(n) for n in re.findall(r'\b\d+\b', winning_ns)]
    playing_ns = [int(n) for n in re.findall(r'\b\d+\b', playing_ns)]

    return winning_ns, playing_ns

def compute_points_ej1(winning_ns, playing_ns):
    winning_ns = set(winning_ns)
    count = sum(1 if n in winning_ns else 0 for n in playing_ns)
    return 2**(count-1) if count > 0 else 0

def compute_points_ej2(winning_ns, playing_ns):
    winning_ns = set(winning_ns)
    count = sum(1 if n in winning_ns else 0 for n in playing_ns)
    return count

def ej1():

    with open(DATA_PATH) as file:
        res = 0
        for line in file.read().splitlines():
            _, game = split_id_game(line)
            winning_ns, playing_ns = process_game(game)
            res += compute_points_ej1(winning_ns, playing_ns)
    print(res)


def ej2():

    with open(DATA_PATH) as file:
        res = 0
        n_cards = defaultdict(lambda: 1)
        res = 0
        for line in file.read().splitlines():
            id, game = split_id_game(line)
            mul = n_cards[id]
            winning_ns, playing_ns = process_game(game)
            points = compute_points_ej2(winning_ns, playing_ns)
            for i in range(id, id+points):
                n_cards[i+1] = n_cards[i+1] + mul
            res += mul
    print(res)


if __name__ == "__main__":
    ej1()
    ej2()
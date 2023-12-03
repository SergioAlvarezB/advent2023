import functools
import re


DATA_PATH = 'data/ej2.txt'

COLORS = ['red', 'green', 'blue']
MAX_COLORS = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def process_round(round):
    color_count = {color: 0 for color in COLORS}
    round = re.sub(r',|\n', '', round).split(" ")
    for n, color in zip(round[1::2], round[2::2]):
        color_count[color] = int(n)

    return color_count

def split_id_game(line):
    line = line.split(":")
    id = int(line[0][5:])
    return id, line[1]


def process_game(game):
    for round in game.split(";"):
        color_count = process_round(round)
        if any(color_count[color] > MAX_COLORS[color] for color in COLORS):
            return False
    return True
        

def process_game_ej2(game):
    min_colors = {color: 0 for color in COLORS}
    res = 1
    for round in game.split(";"):
        color_count = process_round(round)
        for color in COLORS:
            min_colors[color] = max(min_colors[color], color_count[color])
    return functools.reduce(lambda a, b: a*b, min_colors.values())

def ej1():
    with open(DATA_PATH) as file:
        res = 0
        for line in file:
            id, game = split_id_game(line)
            is_possible = process_game(game)
            if is_possible:
                res += id
    print(res)

def ej2():
    with open(DATA_PATH) as file:
        res = 0
        for line in file:
            _, game = split_id_game(line)
            res += process_game_ej2(game)
    print(res)


if __name__ == "__main__":
    ej1()
    ej2()

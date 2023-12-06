DATA_PATH = 'data/ej6.txt'
import re
import math

def get_numbers(string):
    return [float(n) for n in re.findall(r'\b\d+\b', string)]

def get_numbers_concat(string):
    return float(''.join([n for n in re.findall(r'\b\d+\b', string)]))

def compute_limits(t, d):
    t2 = t/2.0
    sq = math.sqrt(t**2 - 4.0*d)/2.0

    return math.ceil(t2 - sq + 1e-7), math.floor(t2 + sq - 1e-7)

def compute_race_score(t, d):
    print(t, d)
    l, h = compute_limits(t, d)
    print(l, h)
    return max(0, h - l + 1)

def ej1():
    with open(DATA_PATH) as file:
        times, distances = [get_numbers(line) for line in file.read().splitlines()]

    print(times)
    res = 1
    for t, d in zip (times, distances):
        res *= compute_race_score(t, d)

    print(res)

def ej2():
    with open(DATA_PATH) as file:
        time, distance = [get_numbers_concat(line) for line in file.read().splitlines()]

    print(time)
    res = compute_race_score(time, distance)

    print(res)

    
if __name__ == "__main__":
    ej1()
    ej2()

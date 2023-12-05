DATA_PATH = 'data/ej5.txt'
import re
import itertools


def get_numbers(string):
    return [int(n) for n in re.findall(r'\b\d+\b', string)]


def parse_input(file):
    return file.read().split("\n\n")


def get_mapping(raw_map):
    mapping = {
        "ranges": [],
        "delta": [],
        "splits": set(),
    }
    for line in raw_map:
        dest, source, range_len =  get_numbers(line)
        mapping["ranges"].append((source, source+range_len))
        mapping['delta'].append(dest-source)
        mapping['splits'] |= set([source, source+range_len])
    return mapping

def apply_map(n, mapp):
    for rang, delta in zip(mapp['ranges'], mapp['delta']):
        if rang[0] <= n < rang[1]:
            n += delta
            break
    return n

def apply_map_to_range(init_rang, mapp):
    l, h = init_rang
    intervals = sorted([l] + [s for s in mapp['splits'] if l < s < h] + [h])
    new_intervals = []
    for _l, _h in zip(intervals[0:], intervals[1:]):
        delta = 0
        for rang, _delta in zip(mapp['ranges'], mapp['delta']):
            if rang[0] <= _l < rang[1]:
                delta = _delta
        new_intervals.append((_l + delta, _h + delta))
    return new_intervals

def map_seed(seed, mappings):
    n = seed
    for mapp in mappings:
        n = apply_map(n, mapp)
    return n

def map_ranges(ranges, mappings):
    for mapp in mappings:
        new_ranges = []
        for rang in ranges:
            new_ranges.extend(apply_map_to_range(rang, mapp))
        ranges = new_ranges

    return ranges


def ej1():
    with open(DATA_PATH) as file:
        inputs = parse_input(file)

    seeds = get_numbers(inputs[0])
    mappings = []
    for raw_map in inputs[1:]:
        mappings.append(get_mapping(raw_map.splitlines()[1:]))

    print(min(map_seed(seed, mappings) for seed in seeds))

def ej2():
    with open(DATA_PATH) as file:
        inputs = parse_input(file)

    seed_ranges = get_numbers(inputs[0])
    seed_ranges = [(l, l+d) for l, d in zip(seed_ranges[::2], seed_ranges[1::2])]
    mappings = []
    for raw_map in inputs[1:]:
        mappings.append(get_mapping(raw_map.splitlines()[1:]))

    ranges = map_ranges(seed_ranges, mappings)
    print(min(rang[0] for rang in ranges))
    

if __name__ == "__main__":
    ej1()
    ej2()

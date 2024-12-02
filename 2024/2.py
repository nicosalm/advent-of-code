""" Advent Of Code 2024 : 2 """

from aoctools import *

def s(levels):
    nums = [int(x) for x in levels]

    diffs = []
    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        diffs.append(diff)

    return all(d > 0 for d in diffs) or all(d < 0 for d in diffs)

def d(levels):
    if s(levels):
        return True

    for i in range(len(levels)):
        d_levels = levels[:i] + levels[i+1:]
        if s(d_levels):
            return True

    return False

def part1(data):
    s_count = 0
    for line in data:
        if s(line.split()):
            s_count += 1
    return s_count

def part2(data):
    s_count = 0
    for line in data:
        if d(line.split()):
            s_count += 1
    return s_count

def main(aocd: AOCD):
    data = aocd.slist

    aocd.p1(part1(data))
    aocd.p2(part2(data))

if __name__ == '__main__':
    aocd = AOCD(2024, 2)
    main(aocd)

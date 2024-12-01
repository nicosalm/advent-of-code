from aoctools import *


def part1(left, right):
    sorted_left = sorted(left)
    sorted_right = sorted(right)

    total = 0
    for l, r in zip(sorted_left, sorted_right):
        total += abs(l - r)

    return total


def part2(left, right):
    total = 0
    for num in left:
        total += num * right.count(num)

    return total


def main(aocd: AOCD):
    data = aocd.slist
    left = []
    right = []

    for line in data:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    aocd.p1(part1(left, right))
    aocd.p2(part2(left, right))


if __name__ == '__main__':
    aocd = AOCD(2024, 1)
    main(aocd)

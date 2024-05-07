# day 1

def floors(string):
    _floor = 0
    for i, char in enumerate(string):
        if char == '(':
            _floor += 1
        elif char == ')':
            _floor -= 1
        if _floor < 0:
            return i + 1
    return None

import sys
directions = sys.stdin.read().strip()
print(floors(directions))

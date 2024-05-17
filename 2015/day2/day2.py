
# given l,h, w of each present. 
# want to order exactly as much wrapping paper as needed

def paper(dimensions):
    l, w, h = map(int, dimensions.split("x"))
    lw, wh, hl = l * w, w * h, h * l
    surface_area = 2 * lw + 2 * wh + 2 * hl
    min_side = min(lw, wh, hl)

    return surface_area + min_side

def ribbon(dimensions):
    l, w, h = map(int, dimensions.split("x"))
    perimeters = [2 * (l + w), 2 * (w + h), 2 * (h + l)]
    smallest_perimeter = min(perimeters)
    volume = l * w * h

    return smallest_perimeter + volume

def total(presents, calc_function):
    _total = 0
    for present in presents.splitlines():
        dimensions = present.strip()
        if dimensions:
            _total += calc_function(dimensions)
    return _total

import sys
presents = sys.stdin.read().strip()

print(total(presents, paper))
print(total(presents, ribbon))

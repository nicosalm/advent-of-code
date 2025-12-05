raw = [line.strip() for line in open("i.txt")]
# ['3-5', '10-14', '16-20', '12-18', '', '1', '5', '8', '11', '17', '32']

separator_idx = raw.index("")
ranges = [[int(x), int(y)] for x, y in (i.split("-") for i in raw[:separator_idx])]
ingredients = raw[separator_idx+1:]

# too many intervals
# must merge them
# then binsearch?

def merge_overlap(arr):
    n = len(arr)
    arr.sort()
    res = []

    # checking for all possible overlaps
    for i in range(n):
        start = arr[i][0]
        end = arr[i][1]

        # skipping already merged intervals
        if res and res[-1][1] >= end:
            continue

        # find the end of the merged range
        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
        res.append([start, end])

    return res

print(merge_overlap(ranges))

def sum_present(ingredients, intervals):
    total = 0
    for ingredient in ingredients:

        found = False

        for interval in intervals:
            front, back = interval[0], interval[1]
            if front <= int(ingredient) <= back:
                found = True

        if found:
            total += 1
    return total

print(sum_present(ingredients, ranges))

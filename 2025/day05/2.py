raw = [line.strip() for line in open("i.txt")]

separator_idx = raw.index("")
intervals = [[int(x), int(y)] for x, y in (i.split("-") for i in raw[:separator_idx])]
ingredients = raw[separator_idx+1:]

def merge_overlap(arr):
    n = len(arr)
    arr.sort()
    res = []

    for i in range(n):
        start = arr[i][0]
        end = arr[i][1]

        if res and res[-1][1] >= end:
            continue

        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
        res.append([start, end])

    return res

def sum_intervals(merged_intervals):
    total = 0
    for i in merged_intervals:
        high, low = i[1], i[0]
        total += high - low+1
        return total

print(sum_intervals(merge_overlap(intervals)))

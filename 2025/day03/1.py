lines = open("i.txt").read().splitlines()

jolts = 0

for line in lines:
    biggest = max(list(line))
    biggest_idx = line.index(biggest)

    if biggest_idx == len(line) - 1:
        second = max(line[:biggest_idx])
        value = int(second + biggest)
    else:
        value = int(biggest + max(line[biggest_idx+1:]))

    jolts += value

print(jolts)

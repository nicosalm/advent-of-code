lines = open("i.txt").read().splitlines()

jolts = 0

for seq in lines:
    k = 12
    i = 0
    n = len(seq)
    out = ""

    while k > 0:
        end = n - k + 1
        window = seq[i:end]
        max_val = max(window)
        j = window.index(max_val)

        out += max_val
        i += j + 1
        k -= 1

    jolts += int(out)

print(jolts)

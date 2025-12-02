lines = [line.strip() for line in open("i.txt").read().split(",")]

scamsum = 0
for line in lines:
    start, end = line.split("-")
    for i in range(int(start), int(end)+1):
        s = str(i)

        # repeat smaller substr multiple times and see if it matches s, if yes then scam
        if any(s[:div] * (len(s) // div) == s
            for div in range(1, len(s) // 2 + 1)
            if len(s) % div == 0):
            scamsum += i

print(scamsum)

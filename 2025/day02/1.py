lines = [line.strip() for line in open("i.txt").read().split(",")]

scamsum = 0
for line in lines:
    start, end = line.split("-")
    for i in range(int(start), int(end)+1):
        s = str(i)

        midpoint = len(s) // 2
        if len(s) % 2 == 0 and s[:midpoint] == s[midpoint:]:
            scamsum += i

print(scamsum)

lines = open("i.txt").read().splitlines()

n = 50

# lol bet you didn't think i'd do it this way
z = sum(
    (n := (n + (int(l[1:]) if l[0] == "R" else -int(l[1:]))) % 100) == 0
    for l in lines
)

print(z)

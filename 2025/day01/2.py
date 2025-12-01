lines = open("i.txt").read().splitlines()

n = 50

# yeah... we kept it going
z = sum(
    (n := (n + d) % 100) == 0
    for l in lines
    for d in [(1 if l[0] == "R" else -1)]
    for _ in range(int(l[1:]))
)

print(z)

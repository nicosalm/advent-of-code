raw = [line.split() for line in open("i.txt")]

def transpose(grid): return list(zip(*grid))

tuples = transpose(raw)
grand_total = 0

for tuple in tuples:
    operator = tuple[len(tuple)-1]
    values = [int(i) for i in tuple[:len(tuple)-1]]
    total = 0 if operator == "+" else 1

    for i in values:
        if operator == "*":
            total *= i
        if operator == "+":
            total += i
    grand_total += total

print(grand_total)

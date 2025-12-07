raw = [line.rstrip("\n") for line in open("i.txt")]
operators = raw[-1].split()
lines = raw[:-1]
max_len = max(len(line) for line in lines)

columns = []
for idx in range(max_len):
    column = []
    for line in lines:
        if idx < len(line):
            if line[idx].isdigit():
                column.append(int(line[idx]))
            else:
                column.append(" ")
        else:
            column.append(" ")
    columns.append(column)

columns.reverse()
operators.reverse()

groups = []
current_group = []

for column in columns:
    if all(c == " " for c in column):
        if current_group:
            groups.append(current_group)
            current_group = []
    else:
        digits = "".join(str(c) for c in column if c != " ")
        if digits:
            current_group.append(int(digits))

if current_group:
    groups.append(current_group)

grand_total = 0
for idx, group in enumerate(groups):
    operator = operators[idx]
    print(operator)
    total = 0 if operator == "+" else 1
    for value in group:
        if operator == "*":
            total *= value
        if operator == "+":
            total += value
    print(total)
    grand_total += total

print(grand_total)

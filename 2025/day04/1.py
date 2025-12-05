grid = [list(line.strip()) for line in open("i.txt")]
dirs = [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]

accessible = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '@':
            adj_rolls = sum(1 for dr, dc in dirs
                              if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]) and grid[r + dr][c + dc] == '@')
            if adj_rolls < 4:
                accessible += 1

print(accessible)

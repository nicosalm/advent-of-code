grid = [list(line.strip()) for line in open("i.txt")]
dirs = [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]

def get_accessible(grid):
    accessible = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # if there's a paper at locaton
            if grid[r][c] == '@':
                # look at adjacent grid spaces
                adj_rolls = sum(1 for dr, dc in dirs
                                  if 0 <= r + dr < len(grid)
                                    and 0 <= c + dc < len(grid[0])
                                    and grid[r + dr][c + dc] == '@')

                # check if there's 4 adjacent rolls
                if adj_rolls < 4:
                    accessible.append((r, c))

    return accessible

def remove_accessible(grid):
    accessible = get_accessible(grid)
    if not accessible:
        return 0

    for r, c in accessible:
        grid[r][c] = 'x'

    return len(accessible)

total = 0
while True:
    count = remove_accessible(grid)
    if count == 0:
        break
    total += count

print(total)

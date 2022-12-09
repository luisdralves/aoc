
grid = []
grid_visible = []

def get_max(seq):
    if seq == []:
        return -1
    return max(seq)

with open('8.txt', 'r') as file:
    while (line := file.readline().rstrip()):
        grid.append([int(ch) for ch in line])
        grid_visible.append([False for ch in line])

for (i, line) in enumerate(grid):
    for (j, height) in enumerate(line):
        column = list([line_it[j] for line_it in grid])
        if height > get_max(line[:j]) or height > get_max(line[j+1:]):
            grid_visible[i][j] = True
        if height > get_max(column[:i]) or height > get_max(column[i+1:]):
            grid_visible[i][j] = True

total = 0
for xs in grid_visible:
    to_print = []
    for x in xs:
        if x:
            to_print.append('X')
            total += 1
        else:
            to_print.append('O')

    print(''.join(to_print))

print(total)
    
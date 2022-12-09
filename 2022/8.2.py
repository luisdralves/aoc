
grid = []
grid_scores = []

def get_max(seq):
    if seq == []:
        return -1
    return max(seq)

with open('8.txt', 'r') as file:
    while (line := file.readline().rstrip()):
        grid.append([int(ch) for ch in line])
        grid_scores.append([-1 for ch in line])

for (i, line) in enumerate(grid):
    for (j, height) in enumerate(line):
        column = list([line_it[j] for line_it in grid])
        sights=[reversed(line[:j]), line[j+1:], reversed(column[:i]), column[i+1:]]
        total_visible = []
        for sight in sights:
            visible = 0
            for tree in sight:
                visible += 1
                if tree >= height:
                    break
            total_visible.append(visible)
        grid_scores[i][j] = total_visible[0] * total_visible[1] * total_visible[2] * total_visible[3]


print(max([max(line) for line in grid_scores]))
    
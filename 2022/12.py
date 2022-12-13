
import pprint
pp = pprint.PrettyPrinter(indent=2)
heightmap = []
start = (0, 0)
aa = []
end = (0, 0)

with open('12.txt', 'r') as file:
    while (line := file.readline().rstrip()):
        heightmap.append(list([ch for ch in line]))

for x, line in enumerate(heightmap):
    for y, ch in enumerate(line):
        if ch == 'S':
            start = (x, y)
        elif ch == 'a':
            aa.append((x, y))
        elif ch == 'E':
            end = (x, y)


def normalize_height(pos):
    x, y = pos
    height = heightmap[x][y]
    return 'a' if height == 'S' else 'z' if height == 'E' else height

def next(node_queue, visited):
    node = node_queue[0]
    del node_queue[0]
    x, y, depth = node
    if (x,y) not in visited:
        visited.add((x, y))
        height = heightmap[x][y]
        if height == 'E':
            print(depth)
            node_queue = []
        else:
            height = normalize_height((x, y))
            possible_moves = []
            if x > 0:
                possible_moves.append((x-1, y, depth+1))
            if x < len(heightmap)-1:
                possible_moves.append((x+1, y, depth+1))
            if y > 0:
                possible_moves.append((x, y-1, depth+1))
            if y < len(heightmap[0])-1:
                possible_moves.append((x, y+1, depth+1))
            possible_moves = list(filter(
                lambda pos:
                    ord(normalize_height((pos[0], pos[1]))) <= ord(height)+1
                    and (pos[0], pos[1]) not in visited,
                possible_moves
            ))
            node_queue += possible_moves

def solve(starts):
    node_queue = [(*start, 0) for start in starts]
    visited = set()

    while len(node_queue) > 0:
        next(node_queue, visited)

solve([start])
solve([start, *aa])

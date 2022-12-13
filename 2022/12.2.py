
import pprint
pp = pprint.PrettyPrinter(indent=2)
heightmap = []
end = (0, 0)
i = 0

with open('12.txt', 'r') as file:
    while (line := file.readline().rstrip()):
        heightmap.append(list([ch for ch in line]))
        if 'E' in line:
            end = (i, line.index('E'))
        i += 1

def normalized_height(pos):
    x, y = pos
    height = heightmap[x][y]
    return 'a' if height == 'S' else 'z' if height == 'E' else height

node_queue = []
for x, line in enumerate(heightmap):
    for y, ch in enumerate(line):
        if ch in ['S', 'a']:
            node_queue.append((x,y,0))

visited = set()


def analyze_node(node):
    global node_queue
    global visited
    x, y, depth = node
    visited.add((x, y))
    height = heightmap[x][y]
    if height == 'E':
        print(depth)
        assert False
    else:
        height = normalized_height((x, y))
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
                ord(normalized_height((pos[0], pos[1]))) <= ord(height)+1
                and (pos[0], pos[1]) not in visited,
            possible_moves
        ))
        node_queue += possible_moves


while len(node_queue) > 0:
    node = node_queue[0]
    del node_queue[0]
    if (node[0], node[1]) not in visited:
        analyze_node(node)

print('queue is empty :(')

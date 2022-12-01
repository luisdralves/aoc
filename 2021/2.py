
depth = 0
horizontal = 0

with open('2.txt', 'r') as file:
    while (line := file.readline()):
        direction, size = line.split(' ')
        if direction == 'forward':
            horizontal += int(size)
        if direction == 'up':
            depth -= int(size)
        if direction == 'down':
            depth += int(size)

print(depth, horizontal, depth*horizontal)

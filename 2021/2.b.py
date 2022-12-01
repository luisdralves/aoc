
aim = 0
depth = 0
horizontal = 0

with open('2.txt', 'r') as file:
    while (line := file.readline()):
        direction, size = line.split(' ')
        if direction == 'forward':
            horizontal += int(size)
            depth += aim * int(size)
        if direction == 'up':
            aim -= int(size)
        if direction == 'down':
            aim += int(size)

print(aim, depth, horizontal, depth*horizontal)

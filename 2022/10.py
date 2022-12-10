
x = 1
cycles = [x]
screen = []

def draw_pixel():
    cycle = (len(cycles) - 1) % 40
    if cycle == 0:
        screen.append([])
    if x-1 <= cycle <= x+1:
        screen[-1].append('#')
    else:
        screen[-1].append('.')

with open('10.txt', 'r') as file:
    while (line := file.readline().rstrip()):
        command = line.split(' ')
        if command[0] == 'noop':
            draw_pixel()
            cycles.append(x)
        if command[0] == 'addx':
            draw_pixel()
            cycles.append(x)
            draw_pixel()
            cycles.append(x)
            x += int(command[1])

strength = 0

for i in [20, 60, 100, 140, 180, 220]:
    strength += (i*cycles[i])

print(strength)

for line in screen:
    print(' '.join(line))

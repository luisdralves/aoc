
maxx = 1000
maxy = 200
sando=(500,0)
airch = '░'
sandch = '▒'
rockch = '▓'
print_width = 200

cave = [[airch for _ in range(maxx)] for _ in range(maxy)]

def print_map():
    for y, row in enumerate(cave):
        print(''.join(row[sando[0]-print_width//2:sando[0]+print_width//2])+'  '+str(y))

deepest = 0

with open('14.txt', 'r') as file:
    while (line := file.readline().rstrip()):
        points = line.split(' -> ')
        for pointa, pointb in zip(points, points[1:]):
            xa,ya,xb,yb = [int(value) for value in [*pointa.split(','), *pointb.split(',')]]
            if ya > deepest:
                deepest = ya
            if yb > deepest:
                deepest = yb
            if xa-xb == 0:
                for y in range(min(ya, yb), max(ya, yb)+1):
                    cave[y][xa] = rockch
            elif ya-yb == 0:
                for x in range(min(xa, xb), max(xa, xb)+1):
                    cave[ya][x] = rockch
            else:
                print('unexpected!!')

for x in range(len(cave[0])):
    cave[deepest+2][x] = rockch
cave = cave[:deepest+3]

can_print_p1 = True
def next_sand(i):
    global cave
    global can_print_p1
    sandx, sandy = sando
    if cave[sandy+1][sandx] == sandch and cave[sandy+1][sandx-1] == sandch and cave[sandy+1][sandx+1] == sandch:
        return False
    while True:
        did_fall = False
        for x in [sandx, sandx-1, sandx+1]:
            if cave[sandy+1][x]==airch:
                cave[sandy][sandx] = airch
                cave[sandy+1][x]=sandch
                sandy = sandy+1
                sandx = x
                did_fall = True
                break
        if not did_fall:
            break
    if sandy > deepest and can_print_p1:
        print(i)
        can_print_p1 = False
    return True

i = 0
while True:
    if not next_sand(i):
        print(i+1)
        break
    i+=1

print_map()

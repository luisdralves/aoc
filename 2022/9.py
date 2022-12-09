
directions = {
    'U':(0,-1),
    'D':(0,1),
    'L':(-1, 0),
    'R':(1, 0),
}

def scalar(diff):
    if diff == 0:
        return 0
    return diff//abs(diff)

def solve(n):
    visited = {(0,0)}
    ps = [(0,0) for _ in range(n)]

    with open('9.txt', 'r') as file:
        while (line := file.readline().rstrip()):
            direction, steps_str = line.split(' ')
            steps = int(steps_str)
            for _ in range(steps):
                xh, yh = ps[0]
                xd, yd = directions[direction]
                ps[0] = (xh+xd, yh + yd)

                for i, p in enumerate(ps):
                    if i == 0:
                        continue

                    xh, yh = ps[i-1]
                    xt, yt = p
                    xdiff = scalar(xh - xt)
                    ydiff = scalar(yh - yt)

                    if abs(xh - xt) > 1 or abs(yh - yt) > 1:
                        ps[i] = (xt+xdiff, yt+ydiff)
                        if i == n-1:
                            visited.add(ps[i])

    return len(visited)

print('part 1:', solve(2))
print('part 2:', solve(10))

from copy import deepcopy
from functools import cmp_to_key

left = None
right = None
packets = [[[2]], [[6]]]

def cast_list(value):
    return value if isinstance(value, list) else [value]

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right

    cast_left = cast_list(deepcopy(left))
    cast_right = cast_list(deepcopy(right))
    diff = 0
    while diff == 0:
        if len(cast_left) == 0 or len(cast_right) == 0:
            if  len(cast_right) > 0:
                diff = -1
            elif len(cast_left) > 0:
                diff = 1
            else:
                diff = 0
                break
        else:
            comp_left = cast_left[0]
            comp_right = cast_right[0]
            del cast_left[0]
            del cast_right[0]
            diff = compare(comp_left, comp_right)
    return diff


with open('13.txt', 'r') as file:
    while (line := file.readline()):
        if line == '\n':
            left = None
            right = None
        elif left is None:
            left = eval(line.rstrip())
        else:
            right = eval(line.rstrip())
            packets.append(left)
            packets.append(right)

sorted_packets = sorted(packets, key=cmp_to_key(compare))

for i, packet in enumerate(sorted_packets):
    print(f'packet {i+1}', packet)


print((sorted_packets.index(packets[0])+1) *( sorted_packets.index(packets[1])+1))

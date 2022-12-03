
import math

p_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
p = [*p_string]

total = 0

with open('3.txt', 'r') as file:
    while (line := file.readline().rstrip()):
        half = math.floor(len(line)/2)
        compartments = (line[:half],line[half:])
        common = ''
        for char in compartments[0]:
            if char in compartments[1]:
                common = char
                break
        total+=p.index(common)+1

print(total)

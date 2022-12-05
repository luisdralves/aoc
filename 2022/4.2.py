
total = 0

with open('4.txt', 'r') as file:
    while (line := file.readline().rstrip()):
        first, second = line.split(',')
        first_start, first_end = map(lambda x: int(x), first.split('-'))
        second_start, second_end = map(lambda x: int(x), second.split('-'))
        if second_start <= first_start <= second_end or second_start <= first_end <= second_end or first_start <= second_start <= first_end or first_start <= second_end <= first_end:
            total += 1

print(total)

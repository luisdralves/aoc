
count = 0
previous_value = -1

with open('1.txt', 'r') as file:
    while (line := file.readline()):
        if previous_value == -1:
            previous_value = int(line)
            continue
        value = int(line)
        if value > previous_value:
            count += 1
        previous_value = value
        
print(count)


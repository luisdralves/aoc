
count = 0
previous_values = []

with open('1.txt', 'r') as file:
    while (line := file.readline()):
        if len(previous_values) < 3:
            previous_values.append(int(line))
            continue
        current_values = previous_values[1:]
        current_values.append(int(line))
        print(previous_values, current_values)
        if sum(current_values) > sum(previous_values):
            count += 1
        previous_values = current_values
        
print(count)


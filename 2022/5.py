
stacks = []

with open('5.txt', 'r') as file:
    line = file.readline().rstrip()
    stack_lines = []
    while not ' 1   2' in line:
        stack_lines.append(line)
        line = file.readline().rstrip()
    stacks_len = int(line[-1])
    stacks = [[]] * stacks_len

    for stack_line in stack_lines:
        for index, char in enumerate(stack_line):
            if char.isupper():
                stack_index = (index+3)//4 - 1
                stacks[stack_index] = [char, *stacks[stack_index]]

    line = file.readline().rstrip()

    while (line := file.readline().rstrip()):
        numbers_string = ''.join(i for i in line if i.isdigit() or i == ' ')
        n, origin, to = map(lambda x: int(x), numbers_string.split('  '))
        for i in range(n):
            crate = stacks[origin - 1].pop()
            stacks[to - 1].append(crate)

print(stacks)
print(''.join([*map(lambda stack: stack[-1], stacks)]))

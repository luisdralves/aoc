currentElfArray = []
elfCalories = []

with open('1.txt', 'r') as elf_file:
    while (line := elf_file.readline()):
        if line == "\n":
            currentElfCalories = sum(currentElfArray)
            elfCalories.append(currentElfCalories)
            currentElfArray = []
        else:
            currentElfArray.append(int(line))

elfCalories.sort(reverse=True)
print(elfCalories[:3])
print(sum(elfCalories[:3]))

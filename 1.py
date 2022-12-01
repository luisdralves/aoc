currentElfArray = []
maxElfCalories = 0

with open('1.txt', 'r') as elf_file:
    while (line := elf_file.readline()):
        if line == "\n":
            currentElfCalories = sum(currentElfArray)
            if currentElfCalories > maxElfCalories:
                maxElfCalories = currentElfCalories
            currentElfArray = []
        else:
            currentElfArray.append(int(line))

print(maxElfCalories)

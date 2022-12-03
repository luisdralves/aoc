
p_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
p = [*p_string]

total = 0

with open('3.txt', 'r') as file:
    while (lines := (file.readline().rstrip(),file.readline().rstrip(),file.readline().rstrip())):
        if lines[0] == '':
            break
        common = ''
        for char in lines[0]:
            if char in lines[1] and char in lines[2]:
                common = char
                break
        total+=p.index(common)+1

print(total)

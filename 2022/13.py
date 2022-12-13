
left = None
right = None
i = 0
total = 0

def cast_list(value):
    return value if isinstance(value, list) else [value]

def compare(left, right, d):
    print(' '*d, '- Compare ', left, ' vs ', right)
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    else:
        cast_left = cast_list(left)
        cast_right = cast_list(right)
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
                diff = compare(comp_left, comp_right, d+1)
        return diff
        

with open('13.txt', 'r') as file:
    while (line := file.readline()):
        if line == '\n':
            left = None
            right = None
            print('new')
        elif left is None:
            i+=1
            left = eval(line.rstrip())
        else:
            right = eval(line.rstrip())
            #print(left)
            #print(right)
            diff = compare(left, right, 0)
            print(diff)
            if diff < 0:
                total += i
            if diff == 0:
                print('warning!!')
        
print(total)
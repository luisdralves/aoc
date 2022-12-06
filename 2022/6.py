
ans = 0

with open('6.txt', 'r') as file:
    line = file.readline().rstrip()
    recents = []
    for i, ch in enumerate(line):
        if len(recents) < 14:
            recents.append(ch)
            continue
        recents = recents[1:]+[ch]
        uniqs = list(dict.fromkeys(recents))
        if len(uniqs) == len(recents):
            ans = i+1
            break

print(ans)
        
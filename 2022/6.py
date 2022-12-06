
ans = 0
recents_target_size = 14

with open('6.txt', 'r') as file:
    line = file.readline().rstrip()
    recents = []
    for i, ch in enumerate(line):
        if len(recents) < recents_target_size:
            recents.append(ch)
            continue
        recents = recents[1:]+[ch]
        if len(recents) == len(set(recents)):
            ans = i+1
            break

print(ans)
        
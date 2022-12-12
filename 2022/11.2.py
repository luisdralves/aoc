
import pprint
from tqdm import tqdm

pp = pprint.PrettyPrinter(indent=2)
monkeys = []

with open('11.txt', 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        if line.split(' ')[0] == 'Monkey':
            monkey = {}

            next_line = lines[i+1].rstrip()
            start_items_str = next_line.split(': ')[1].split(', ')
            monkey["start_items"] = list([int(item) for item in start_items_str])

            next_line = lines[i+2].rstrip()
            monkey["operation"] = next_line.split('= ')[1]

            next_line = lines[i+3].rstrip()
            monkey["test_div"] = int(next_line.split('by ')[1])

            next_line = lines[i+4].rstrip()
            monkey["on_true"] = int(next_line.split('monkey ')[1])

            next_line = lines[i+5].rstrip()
            monkey["on_false"] = int(next_line.split('monkey ')[1])

            monkey["inspected"] = 0

            monkeys.append(monkey)

pp.pprint(monkeys)
print()

common = 1
for monkey in monkeys:
    common *= monkey["test_div"]


for _ in tqdm(range(10000)):
    for monkey in monkeys:
        for old in monkey["start_items"]:
            monkey["inspected"] += 1
            new = eval(monkey["operation"]) % common
            if new % monkey["test_div"] == 0:
                monkeys[monkey["on_true"]]["start_items"].append(new)
            else:
                monkeys[monkey["on_false"]]["start_items"].append(new)
        monkey["start_items"] = []

inspections = [monkey["inspected"] for monkey in monkeys]
inspections.sort()
print(inspections)
print(inspections[-1]*inspections[-2])

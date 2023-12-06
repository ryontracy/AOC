with open('input.txt') as f:
    lines = f.readlines()

cals = []
for line in lines:
    linenums = [s for s in line if s.isdigit()]
    cal = int(linenums[0] + linenums[-1])
    cals.append(cal)

answer = sum(cals)
print(answer)
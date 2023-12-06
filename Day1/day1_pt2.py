with open('input1.txt') as f:
    lines = f.readlines()

numberdict = {'one':1 , 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
cals = []
for line in lines:
    linenums = []
    for i in range(len(line)):
        s = line[i]
        if s.isdigit():
            linenums.append(int(s))
        else:
            for ns in numberdict.keys():
                if line[i:].startswith(ns):
                    linenums.append(numberdict[ns])
    print(linenums)
    cal = int(str(linenums[0]) + str(linenums[-1]))
    cals.append(cal)

print(cals)
answer = sum(cals)
print(answer)
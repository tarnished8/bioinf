string = input()
d = {"A": 0,
     "C": 1,
     "G": 2,
     "T": 3}
p = {0: "A",
     1: "C",
     2: "G",
     3: "T"}
last = []
first = ['$']
counts = [0, 0, 0, 0]
for x in string:
    if x == '$':
        last.append(x)
    else:
        counts[d[x]] += 1
        last.append(x + str(counts[d[x]]))
for i in range(4):
    for j in range(1, counts[i] + 1):
        first.append(p[i] + str(j))
symb = first[0]
ans = [symb]
for i in range(len(string) - 1):
    symb = first[last.index(symb)]
    ans.append(symb)
ans.pop(0)
print(''.join([x[0] for x in ans]) + '$')
string = input()
_ = input()
alphabet = [x for x in input().split()]
_ = input()
states = [x for x in input().split()]
_ = input()
d_alph = dict((i, j) for j, i in enumerate(alphabet))
_ = input()
transition = {}
for i in range(len(states)):
    x = input().strip("\t").split()
    transition[x[0]] = [float(y) for y in x[1:]]
_ = input()
emission = {}
_ = input()
for i in range(len(states)):
    x = input().strip("\t").split()
    emission[x[0]] = [float(y) for y in x[1:]]
s = [[0 for i in range(len(string))] for j in range(len(states))]
for i in range(len(states)):
    s[i][0] = emission[states[i]][d_alph[string[0]]] * (1 / len(states))
for i in range(1, len(string)):
    for j in range(len(states)):
        s[j][i] = sum([s[k][i - 1] * transition[states[k]][j] * emission[states[j]][d_alph[string[i]]] for k in range(len(states))])
print(sum([s[i][-1] for i in range(len(states))]))

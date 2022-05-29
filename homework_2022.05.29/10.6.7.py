string = input()
_ = input()
alphabet = [x for x in input().split()]
_ = input()
states = [x for x in input().split()]
_ = input()
d_alph = dict((i, j) for j, i in enumerate(alphabet))
d_states = dict((i, j) for j, i in enumerate(states))
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
s_parent = [[-1 for i in range(len(string))] for j in range(len(states))]
for i in range(len(states)):
    s[i][0] = emission[states[i]][d_alph[string[0]]] * (1 / len(states))
    s_parent[i][0] = 's'
for i in range(1, len(string)):
    for j in range(len(states)):
        m = 0
        for k in range(len(states)):
            cur = s[k][i - 1] * transition[states[k]][j] * emission[states[j]][d_alph[string[i]]]
            if cur > m:
                m = cur
                symb = states[k]
        s[j][i] = m
        s_parent[j][i] = symb
ans = []
m = 0
for i in range(len(states)):
    cur = s[i][-1]
    if cur > m:
        m = cur
        symb = states[i]
ans.append(symb)
for j in range(len(string) - 1, 0, -1):
    cur = ans[-1]
    ans.append(s_parent[d_states[cur]][j])
#print(s)
#print(s_parent)
print(''.join(reversed(ans)))
#print(max([s[i][-1] for i in range(len(states))]))

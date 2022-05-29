path = input()
_ = input()
states = [x for x in input().split()]
_ = input()
d = dict((i, j) for j, i in enumerate(states))
_ = input()
transition = {}
for i in range(len(states)):
    x = input().strip("\t").split()
    transition[x[0]] = [float(y) for y in x[1:]]
prob = 1 / len(states)
for j in range(len(path) - 1):
    prob *= transition[path[j]][d[path[j + 1]]]
print(prob)

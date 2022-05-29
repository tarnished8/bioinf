string = input()
_ = input()
alphabet = [x for x in input().split()]
_ = input()
path = input()
_ = input()
states = [x for x in input().split()]
_ = input()
d = dict((i, j) for j, i in enumerate(alphabet))
_ = input()
emission = {}
for i in range(len(states)):
    x = input().strip("\t").split()
    emission[x[0]] = [float(y) for y in x[1:]]
prob = 1
for j in range(len(path)):
    prob *= emission[path[j]][d[string[j]]]
print(prob)

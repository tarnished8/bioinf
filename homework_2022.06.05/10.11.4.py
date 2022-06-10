f = open("input.txt", "r")
string = f.readline().strip("\n")
_ = f.readline()
alph = f.readline().strip("\n").split()
_ = f.readline()
path = f.readline().strip("\n")
_ = f.readline()
states = f.readline().strip("\n").split()
emission = [[0.0 for x in range(len(alph))] for y in range(len(states))]
transition = [[0.0 for x in range(len(states))] for y in range(len(states))]
d_alph = dict((i, j) for j, i in enumerate(alph))
d_states = dict((i, j) for j, i in enumerate(states))
for i in range(len(string) - 1):
    symb = string[i]
    state = path[i]
    state_next = path[i + 1]
    emission[d_states[state]][d_alph[symb]] += 1
    transition[d_states[state]][d_states[state_next]] += 1
emission[d_states[path[-1]]][d_alph[string[-1]]] += 1
for x in states:
    n = path.count(x)
    m = n - int(x == path[-1])
    if n != 0:
        for i in range(len(alph)):
            emission[d_states[x]][i] = round(emission[d_states[x]][i] / n, 3)
    else:
        for i in range(len(alph)):
            emission[d_states[x]][i] = round(1 / len(alph), 3)
    if m != 0:
        for i in range(len(states)):
            transition[d_states[x]][i] = round(transition[d_states[x]][i] / m, 3)
    else:
        for i in range(len(states)):
            transition[d_states[x]][i] = round(1 / len(states), 3)
print("", end=" ")
print(*[x for x in states])
for i in range(len(states)):
    print(states[i], end=" ")
    print(*transition[i])
print("--------")
print("", end=" ")
print(*[x for x in alph])
for i in range(len(states)):
    print(states[i], end=" ")
    print(*emission[i])

f = open("input.txt", "r")
thr, sigma = f.readline().strip("\n").split()
thr = float(thr)
sigma = float(sigma)
_ = f.readline()
alph = f.readline().strip("\n").split()
_ = f.readline()
strings = [x for x in f.readlines()]
alignment = [[y for y in x.strip('\n')] for x in strings]
states = ["S"]
emission = [[0.0 for x in range(len(alph))]]
for col in range(len(alignment[0])):
    cur_col = [x[col] for x in alignment]
    if cur_col.count("-") / len(cur_col) > thr:
        if states[-1] == "I":
            states.append("I")
            cur_col += prev_col
            em = [cur_col.count(x) / (len(cur_col) - cur_col.count("-")) for x in alph]
            emission.pop(-1)
            emission.append(em)
        else:
            states.append("I")
            em = [cur_col.count(x) / (len(cur_col) - cur_col.count("-")) for x in alph]
            emission.append(em)
    else:
        if states[-1] == "S":
            em = [0.0 for x in range(len(alph))]
            emission.append(em)
        if states[-1] == "M":
            emission.append([0.0 for x in range(len(alph))])
        states.append("M")
        em = [cur_col.count(x) / (len(cur_col) - cur_col.count("-")) for x in alph]
        emission.append(em)
        emission.append([0.0 for x in range(len(alph))])
    prev_col = cur_col
if states[-1] == "M":
    emission.append([0.0 for x in range(len(alph))])
emission.append([0.0 for x in range(len(alph))])
print(emission)
states_fin = ["S", "I0"]
c = 1
m = states.count("M")
for i in range(m):
    states_fin.append("M" + str(c))
    states_fin.append("D" + str(c))
    states_fin.append("I" + str(c))
    c += 1
states_fin.append("E")
print(states_fin)
transition = [[0.0 for x in range(len(states_fin))] for y in range(len(states_fin))]
paths = []
states_count = {x: 0 for x in states_fin}
for s in alignment:
    path = ["S"]
    c = 1
    for i in range(len(s)):
        a = s[i]
        cur_state = states[i + 1]
        if cur_state == "M" and a == "-":
            transition[states_fin.index(path[-1])][states_fin.index("D" + str(c))] += 1
            path.append("D" + str(c))
            states_count["D" + str(c)] += 1
            c += 1
        if cur_state == "M" and a != "-":
            transition[states_fin.index(path[-1])][states_fin.index("M" + str(c))] += 1
            path.append("M" + str(c))
            states_count["M" + str(c)] += 1
            c += 1
        if cur_state == "I" and a == "-":
            continue
        if cur_state == "I" and a != "-":
            transition[states_fin.index(path[-1])][states_fin.index("I" + str(c - 1))] += 1
            states_count["I" + str(c - 1)] += 1
            path.append("I" + str(c - 1))
    transition[states_fin.index(path[-1])][states_fin.index("E")] += 1
    states_count["E"] += 1
    path.append("E")
    paths.append(path)
states_count["S"] = states_count["E"]
for x in range(len(transition)):
    if states_count[states_fin[x]] != 0:
        for y in range(len(transition[x])):
            transition[x][y] = transition[x][y] / states_count[states_fin[x]]
for x in range(2):
    s = 0
    for y in range(1, 4):
        transition[x][y] += sigma
        s += transition[x][y]
    for y in range(1, 4):
        transition[x][y] = round(transition[x][y] / s, 3)
for x in range(len(transition) - 4, len(transition) - 1):
    s = 0
    for y in range(len(transition) - 2, len(transition)):
        transition[x][y] += sigma
        s += transition[x][y]
    for y in range(len(transition) - 2, len(transition)):
        transition[x][y] = round(transition[x][y] / s, 3)
for z in range(m - 1):
    for x in range(3):
        s = 0
        for y in range(3):
            transition[2 + 3 * z + x][4 + 3 * z + y] += sigma
            s += transition[2 + 3 * z + x][4 + 3 * z + y]
        for y in range(3):
            transition[2 + 3 * z + x][4 + 3 * z + y] = round(transition[2 + 3 * z + x][4 + 3 * z + y] / s, 3)
for x in range(len(emission) - 1):
    if x % 3 != 0:
        s = 0
        for y in range(len(alph)):
            emission[x][y] += sigma
            s += emission[x][y]
        for y in range(len(alph)):
            emission[x][y] = round(emission[x][y] / s, 3)
print("", end=" ")
print(*[x for x in states_fin])
for i in range(len(states_fin)):
    print(states_fin[i], end=" ")
    print(*transition[i])
print("--------")
print("", end=" ")
print(*[x for x in alph])
for i in range(len(states_fin)):
    print(states_fin[i], end=" ")
    print(*emission[i])
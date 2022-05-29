f = open("input.txt", "r")
thr = float(f.readline())
_ = f.readline()
alph = f.readline().strip("\n").split("\t")
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
for i in range(states.count("M")):
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
            states_count["D" +str(c)] += 1
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

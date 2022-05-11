def children(node, tree):
    ans = []
    for v in tree:
        if v[0] == node:
            ans.append(v[1])
    return ans


def ripes(tags, tree):
    ans = []
    for v in range(len(tags) // 2 + 1, len(tags)):
        if tags[v] == 0 and tags[children(v, tree)[0]] == 1 and tags[children(v, tree)[1]] == 1:
            ans.append(v)
    return ans


def ham_dist(a, b):
    mis = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            mis = mis + 1
    return mis


alphabet = "ACDEFGHIKLMNPQRSTVWY"
weights = []
f = open("input.txt", 'r')
f1 = open("BLOSUM62", 'r')
n = int(f.readline())
for i in range(20):
    weights.append([int(x) for x in f1.readline().strip("\n").split()])
tree = []
strings = []
score = 0
for i in range(n):
    a, b = f.readline().strip("\n").split("->")
    tree.append([int(a), i])
    strings.append(b)
labels = strings + ['' for i in range(n - 1)]
for i in range(n - 2):
    a, b = f.readline().strip("\n").split("->")
    tree.append([int(a), int(b)])
for cur_index in range(len(strings[0])):
    tag = [1 for i in range(n)] + [0 for j in range(n - 1)]
    character = [strings[i][cur_index] for i in range(n)] + ['F' for i in range(n - 1)]
    s = [[0] * 20 for i in range(2 * n - 1)]
    for v in range(n):
        for k in range(20):
            if character[v] != alphabet[k]:
                s[v][k] = -99999999
    while ripes(tag, tree):
        node = ripes(tag, tree)[0]
        tag[node] = 1
        for k in range(20):
            s[node][k] = max([s[children(node, tree)[0]][i] + weights[i][k] for i in range(20)]) + max([s[children(node, tree)[1]][j] + weights[j][k] for j in range(20)])
        if node == 2 * n - 2:
            a = 0
            for k in range(20):
                if s[node][k] > a:
                    a = s[node][k]
                    symbol = alphabet[k]
            score += a
print(score)

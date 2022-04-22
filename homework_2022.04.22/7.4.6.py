def limb_length(n, j, dist):
    return int(min([dist[i][j] + dist[j][k] - dist[i][k] for i in range(n) if i != j for k in range(n) if k != j]) / 2)


def path(start, finish, adj):
    visited = [False for i in range(10*len(adj))]
    visited[start] = True
    cur = start
    stack = [start]
    while True:
        pos = [x for x in adj[cur] if not visited[x]]
        if not pos:
            stack.pop()
            cur = stack[-1]
        else:
            cur = pos[0]
            stack.append(cur)
            if cur == finish:
                return stack
            visited[cur] = True


def tree_to_adj(tree):
    adj = {}
    for x in tree:
        if x[0] in adj:
            adj[x[0]].append(x[1])
        else:
            adj[x[0]] = [x[1]]
        if x[1] in adj:
            adj[x[1]].append(x[0])
        else:
            adj[x[1]] = [x[0]]
    return adj


def additive_philogeny(dist):
    global n1
    n = len(dist)
    if n == 2:
        tree = [[0, 1, dist[0][1]], [1, 0, dist[1][0]]]
        return tree
    ll = limb_length(n, n - 1, dist)
    for j in range(n - 1):
        dist[j][n - 1] -= ll
        dist[n - 1][j] = dist[j][n - 1]
    for i in range(n - 1):
        for j in range(n - 1):
            if dist[i][j] == dist[i][n - 1] + dist[n - 1][j]:
                c, d = i, j
    x = dist[c][n - 1]
    dist = [y[:-1] for y in dist[:-1]]
    tree = additive_philogeny(dist)
    adj = tree_to_adj(tree)
    path1 = path(c, d, adj)
    dist_from_c = 0
    for i in range(len(path1) - 1):
        for z in tree:
            if z[0] == path1[i] and z[1] == path1[i + 1]:
                cur_0 = z[0]
                cur_1 = z[1]
                cur_2 = z[2]
        dist_from_c += cur_2
        if x == dist_from_c:
            tree.append([path1[i + 1], n - 1, ll])
            tree.append([n - 1, path1[i + 1], ll])
            break
        if dist_from_c > x:
            tree.remove([cur_0, cur_1, cur_2])
            tree.remove([cur_1, cur_0, cur_2])
            tree.append([path1[i], n1, x - (dist_from_c - cur_2)])
            tree.append([n1, path1[i], x - (dist_from_c - cur_2)])
            tree.append([path1[i + 1], n1, dist_from_c - x])
            tree.append([n1, path1[i + 1], dist_from_c - x])
            tree.append([n1, n - 1, ll])
            tree.append([n - 1, n1, ll])
            break
    n1 += 1
    return tree


f = open("input.txt", 'r')
n1 = int(f.readline())
dist = [[int(x) for x in line.split(" ")] for line in f.readlines()]
tree = additive_philogeny(dist)
for x in sorted(tree):
    print(str(x[0]) + "->" + str(x[1]) + ":" + str(x[2]))






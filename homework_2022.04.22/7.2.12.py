def path(start, finish, adj):
    visited = [False for i in range(len(adj))]
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


f = open("input.txt", 'r')
n = int(f.readline())
dist = [[0 for i in range(10 * n)] for j in range(10 * n)]
ans = [[0 for i in range(n)] for j in range(n)]
adj = {0: []}
for x in f.readlines():
    d, c = x.split(":")
    a, b = d.split("->")
    a, b, c = int(a), int(b), int(c)
    if a in adj:
        adj[a].append(b)
    else:
        adj[a] = [b]
    dist[a][b] = c
for i in range(n):
    for j in range(i + 1, n):
        cur_path = path(i, j, adj)
        for k in range(len(cur_path) - 1):
            ans[i][j] += dist[cur_path[k]][cur_path[k + 1]]
        ans[j][i] = ans[i][j]
for x in ans:
    print(*x)


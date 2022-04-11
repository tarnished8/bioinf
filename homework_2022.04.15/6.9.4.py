def chromosome_to_cycle(chromosome):
    chr = [x for x in chromosome[1:-1].split(")(")]
    final = []
    for x in chr:
        cur = [int(y) for y in x.split(" ")]
        nodes = []
        for z in cur:
            if z > 0:
                nodes.append(2 * z - 1)
                nodes.append(2 * z)
            else:
                nodes.append(2 * abs(z))
                nodes.append(2 * abs(z) - 1)
        nodes = nodes[-1:] + nodes[:-1]
        final = final + nodes
    return final


def dfs(adj, start):
    global visited
    if visited[start - 1]:
        return
    global cycles
    visited[start - 1] = True
    cur = start
    while True:
        pos = [x for x in adj[cur] if not visited[x - 1]]
        if not pos:
            cycles += 1
            break
        next_cur = pos[0]
        visited[next_cur - 1] = True
        cur = next_cur


chromosome1 = input()
chromosome2 = input()
adj1 = chromosome_to_cycle(chromosome1)
adj2 = chromosome_to_cycle(chromosome2)
n = len(adj1)
adj = {j + 1: [] for j in range(n)}
for i in range(int(n / 2)):
    adj[adj1[2 * i]].append(adj1[2 * i + 1])
    adj[adj1[2 * i + 1]].append(adj1[2 * i])
    adj[adj2[2 * i]].append(adj2[2 * i + 1])
    adj[adj2[2 * i + 1]].append(adj2[2 * i])
print(adj)
cycles = 0
visited = [False for i in range(n)]
for i in range(1, n + 1):
    dfs(adj, i)
print(int(n / 2) - cycles)





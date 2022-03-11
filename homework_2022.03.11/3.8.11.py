import random


chars = "01"


def all_k_mers(cur, k, k_mers):
    if k == 0:
        k_mers.append(cur)
    else:
        for i in range(2):
            cur1 = cur + chars[i]
            all_k_mers(cur1, k-1, k_mers)

def print_adjacency(node, edges):
    r.write(node + ":")
    for x in edges:
        r.write(" " + x)
    r.write("\n")


def de_brujin(patterns):
    vertices = []
    edges = [[] for i in range(99*len(patterns))]
    for pattern in patterns:
        if pattern[:-1] not in vertices:
            vertices.append(pattern[:-1])
        if pattern[1:] not in vertices:
            vertices.append(pattern[1:])
        edges[vertices.index(pattern[:-1])].append(pattern[1:])
    for j in vertices:
        if edges[vertices.index(j)]:
            print_adjacency(j, edges[vertices.index(j)])


f = open("text.txt", "r+")
r = open("ans.txt", "r+")
k = int(input())
strings = []
all_k_mers("", k, strings)
patterns = strings
de_brujin(patterns)

r.seek(0)
ne = []
for line in r:
    ne.append(line.rstrip('\n ').split(": "))
edges = []
vertices = []
for x in ne:
    vertices.append(x[0])
    edges.append(x[1].split(" "))
start = random.choice(vertices)
stack = [start]
ans = []
while True:
    if start in vertices and edges[vertices.index(start)]:
        next = random.choice(edges[vertices.index(start)])
        stack.append(next)
        edges[vertices.index(start)].remove(next)
        start = next
    else:
        stack.pop()
        ans.append(start)
        if stack:
            start = stack[-1]
        else:
            break
for j in reversed(ans[:-1]):
    print(j[-1], end="")

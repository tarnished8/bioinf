import random


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


f = open("text.txt", "r")
r = open("ans.txt", "r+")
k = int(f.readline())
patterns = f.read().split(" ")
de_brujin(patterns)

r.seek(0)
ne = []
for line in r:
    ne.append(line.rstrip('\n ').split(": "))
edges = []
vertices = []
for x in ne:
    vertices.append(x[0])
    edges.append([y for y in x if x.index(y) != 0])
start = 0
count = {v: 0 for v in vertices}
for i in edges:
    for j in i:
        if j in count.keys():
            count[j] = count[j] + 1
for j in range(len(vertices)):
    if len(edges[j]) > count[vertices[j]]:
        start = vertices[j]
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
print(ans[-1][:-1], end="")
for j in reversed(ans):
        print(j[-1], end="")

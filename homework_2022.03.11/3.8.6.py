import random

f = open("text.txt", "r")
ne = []
for line in f:
    ne.append(line.rstrip('\n ').split(": "))
edges = []
vertices = []
for x in ne:
    vertices.append(int(x[0]))
    edges.insert(int(x[0]), [int(y) for y in x[1] if y != " "])
start = 0
count = [0 for i in range(2*len(edges))]
for i in edges:
    for j in i:
        count[j] += 1
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
for j in reversed(ans):
    print(j, end=" ")

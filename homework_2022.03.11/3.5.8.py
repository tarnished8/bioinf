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
r = open("ans.txt", "w")
patterns = f.read().split(" ")
de_brujin(patterns)

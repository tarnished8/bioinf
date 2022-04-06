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


spectrum = [int(x) for x in input().split(" ")]
convolution = []
a = []
k = int(input())
N = int(input())
M = int(input())
n = len(spectrum)
for i in range(1, n):
    for j in range(i):
        if spectrum[i] - spectrum[j] != 0:
            convolution.append(abs(spectrum[i] - spectrum[j]))
while len(a) < N or convolution:
    cur = max(convolution, key=convolution.count)
    if cur < 201 and cur > 56:
        a.append(cur)
        convolution.remove(cur)
while convolution:
    cur = max(convolution, key=convolution.count)
    if cur == a[-1]:
        if cur < 201 and cur > 56
            a.append(cur)
            convolution.remove(cur)
    else:
        break

k_mers = [] #  не доделал

de_brujin(k_mers)

#  https://github.com/tarnished8/bioinf/blob/main/homework_2022.03.11/3.5.8.py
#  https://github.com/tarnished8/bioinf/blob/main/homework_2022.04.01/4.9.4.py




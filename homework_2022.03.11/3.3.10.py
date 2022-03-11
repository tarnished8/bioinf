def print_adjacency(node, edges):
    print(node + ": ", end="")
    for x in edges:
        print(x, end=" ")
    print()


sample = input().split()
for i in sample:
    ans = [x for x in sample if x[:len(x)-1] == i[1:]]
    if ans:
        print_adjacency(i, ans)

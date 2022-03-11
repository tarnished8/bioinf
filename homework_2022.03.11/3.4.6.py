def print_adjacency(node, edges):
    print(node + ": ", end=" ")
    for x in edges:
        print(x, end=" ")
    print()


k = int(input())
text = input()
set_sample = set([text[i:i+k-1] for i in range(len(text)-k+1)])
for i in set_sample:
    ans = []
    for j in range(len(text)-k+1):
        if text[j:j+k-1] == i:
            ans.append(text[j+1:j+k])
    if ans:
        print_adjacency(i, ans)

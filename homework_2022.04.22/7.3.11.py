f = open("input.txt", 'r')
n = int(f.readline())
j = int(f.readline())
dist = [[int(x) for x in line.split(" ")] for line in f.readlines()]
ans = int(min([dist[i][j] + dist[j][k] - dist[i][k] for i in range(n) if i != j for k in range(n) if k != j]) / 2)
print(ans)

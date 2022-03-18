def manhattan_tourist(n, m, down, right):
    s = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        s[i][0] = s[i-1][0] + down[i-1][0]
    for j in range(1, m + 1):
        s[0][j] = s[0][j-1] + right[0][j-1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i-1][j] + down[i-1][j], s[i][j-1] + right[i][j-1])
    return s[n][m]


n, m = input().split(" ")
n = int(n)
m = int(m)
down = [[0 for i in range(m + 1)] for j in range(n)]
right = [[0 for i in range(m)] for j in range(n + 1)]
for i in range(n):
    down[i] = [int(x) for x in input().split(" ")]
esc = input()
for i in range(n+1):
    right[i] = [int(x) for x in input().split(" ")]
print(manhattan_tourist(n, m, down, right))




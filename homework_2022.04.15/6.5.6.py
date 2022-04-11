permutation = [0]
for x in input().split(" "):
    permutation.append(int(x))
permutation.append(len(permutation))
ans = 0
for i in range(len(permutation) - 1):
    if permutation[i + 1] - permutation[i] != 1:
        ans += 1
print(ans)

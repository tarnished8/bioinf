string = input()
matrix = []
for i in range(len(string)):
    matrix.append(string[-(i+1):] + string[:-(i+1)])
matrix.sort()
ans = []
for x in matrix:
    ans.append(x[-1])
print(''.join(ans))
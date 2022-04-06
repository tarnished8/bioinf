import sys


def lcs_backtrack(s1, s2, match, mismatch, indel):
    s = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    count = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)] #  вместо backtrack ведём массив count, который считает количество максимальных путей
    count[0][0] = 1
    for i in range(len(s1)):
        s[i + 1][0] = (i + 1) * indel
        count[i + 1][0] = 1
    for j in range(len(s2)):
        s[0][j + 1] = (j + 1) * indel
        count[0][j + 1] = 1
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                s[i][j] = max(s[i - 1][j] + indel, s[i][j - 1] + indel, s[i - 1][j - 1] + match)
            else:
                s[i][j] = max(s[i - 1][j] + indel, s[i][j - 1] + indel, s[i - 1][j - 1] + mismatch)
            if s[i][j] == s[i - 1][j] + indel:
                count[i][j] += count[i - 1][j]
            if s[i][j] == s[i][j - 1] + indel:
                count[i][j] += count[i][j - 1]
            if s[i][j] == s[i - 1][j - 1] + match and s1[i - 1] == s2[j - 1]:
                count[i][j] += count[i - 1][j - 1]
            elif s[i][j] == s[i - 1][j - 1] + mismatch:
                count[i][j] += count[i - 1][j - 1]
    return count[-1][-1]

#  не восстанавливаем строки

sys.setrecursionlimit(2000)
match = 1
mismatch = -1
indel = -1
s1 = input()
s2 = input()
print(lcs_backtrack(s1, s2, match, mismatch, indel))

# based on https://github.com/tarnished8/bioinf/blob/main/homework_2022.03.18/5.10.3.py


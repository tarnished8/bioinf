import sys


def lcs_backtrack(s1, s2):
    s = [[0 for i in range(len(s2))] for j in range(len(s1))]
    backtrack = [[-1 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            match = 0
            if s1[i - 1] == s2[j - 1]:
                match = 1
            s[i][j] = max(s[i - 1][j], s[i][j - 1], s[i - 1][j - 1] + match)
            if s[i][j] == s[i - 1][j]:
                backtrack[i][j] = 0
            elif s[i][j] == s[i][j - 1]:
                backtrack[i][j] = 1
            elif s[i][j] == s[i - 1][j - 1] + match:
                backtrack[i][j] = 2
    return backtrack


def output_lcs(backtrack, s1, i, j):
    if i == 0 or j == 0:
        return ""
    if backtrack[i][j] == 0:
        return output_lcs(backtrack, s1, i - 1, j)
    if backtrack[i][j] == 1:
        return output_lcs(backtrack, s1, i, j - 1)
    else:
        return output_lcs(backtrack, s1, i - 1, j - 1) + s1[i - 1]


sys.setrecursionlimit(2000)
s1 = input()
s2 = input()
backtrack = lcs_backtrack(s1, s2)
print(output_lcs(backtrack, s1, len(s1), len(s2)))

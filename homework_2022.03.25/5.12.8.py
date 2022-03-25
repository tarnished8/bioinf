import sys


def lcs_backtrack(s1, s2, match, mismatch, opening, extension):
    lower = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    upper = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    middle = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    backtrack = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    for i in range(len(s1)):
        lower[i + 1][0] = - i * extension - opening
        upper[i + 1][0] = - i * extension - opening
        middle[i + 1][0] = - i * extension - opening
    for j in range(len(s2)):
        lower[0][j + 1] = - j * extension - opening
        upper[0][j + 1] = - j * extension - opening
        middle[0][j + 1] = - j * extension - opening
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                cur = match
            else:
                cur = -mismatch
            lower[i][j] = max(lower[i - 1][j] - extension, middle[i - 1][j] - opening)
            upper[i][j] = max(middle[i][j - 1] - opening, upper[i][j - 1] - extension)
            middle[i][j] = max(lower[i][j], upper[i][j], middle[i - 1][j - 1] + cur)
            if middle[i][j] == lower[i][j]:
                backtrack[i][j] = 0
            elif middle[i][j] == upper[i][j]:
                backtrack[i][j] = 1
            elif middle[i][j] == middle[i - 1][j - 1] + match:
                backtrack[i][j] = 2
            else:
                backtrack[i][j] = 3
    print(middle[i][j])
    return backtrack


def output_lcs(backtrack, s1, s2, i, j, str1, str2):
    if i == 0:
        for l in range(j):
            str1 += "-"
            str2 += s2[l]
        ans = [str1[::-1], str2[::-1]]
        return ans
    if j == 0:
        for l in range(i):
            str1 += s1[l]
            str2 += "-"
        ans = [str1[::-1], str2[::-1]]
        return ans
    if backtrack[i][j] == 0:
        str1 += s1[i-1]
        str2 += "-"
        return output_lcs(backtrack, s1, s2, i - 1, j, str1, str2)
    if backtrack[i][j] == 1:
        str1 += '-'
        str2 += s2[j-1]
        return output_lcs(backtrack, s1, s2, i, j - 1, str1, str2)
    else:
        str1 += s1[i-1]
        str2 += s2[j-1]
        return output_lcs(backtrack, s1, s2, i - 1, j - 1, str1, str2)


sys.setrecursionlimit(2000)
match, mismatch, opening, extension = [int(i) for i in input().split(" ")]
s1 = input()
s2 = input()
backtrack = lcs_backtrack(s1, s2, match, mismatch, opening, extension)
ans = output_lcs(backtrack, s1, s2, len(s1), len(s2), "", "")
for x in ans:
    print(x)

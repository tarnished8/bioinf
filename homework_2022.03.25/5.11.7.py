import sys


def lcs_backtrack(s1, s2, match, mismatch, indel):
    s = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    backtrack = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    for j in range(len(s2)):
        s[0][j + 1] = - (j + 1) * indel
        backtrack[0][j+1] = 1
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                cur = match
            else:
                cur = -mismatch
            if i != len(s1):
                s[i][j] = max(s[i - 1][j] - indel, s[i][j - 1] - indel, s[i - 1][j - 1] + cur)
                if s[i][j] == s[i - 1][j] - indel:
                    backtrack[i][j] = 0
                elif s[i][j] == s[i][j - 1] - indel:
                    backtrack[i][j] = 1
                elif s[i][j] == s[i - 1][j - 1] + match:
                    backtrack[i][j] = 2
                elif s[i][j] == s[i - 1][j - 1] - mismatch:
                    backtrack[i][j] = 3
            else:
                s[i][j] = max(s[i - 1][j] - indel, s[i][j - 1], s[i - 1][j - 1] + cur)
                if s[i][j] == s[i - 1][j] - indel:
                    backtrack[i][j] = 0
                elif s[i][j] == s[i][j - 1]:
                    backtrack[i][j] = 1
                elif s[i][j] == s[i - 1][j - 1] + match:
                    backtrack[i][j] = 2
                elif s[i][j] == s[i - 1][j - 1] - mismatch:
                    backtrack[i][j] = 3
    print(s[i][j])
    return backtrack


def output_lcs(backtrack, s1, s2, i, j, str1, str2):
    if i == 0:
        if len(s1) < len(s2):
            for l in range(j-1, -1, -1):
                str1 += "-"
                str2 += s2[l]
        ans = [str1[::-1], str2[::-1]]
        return ans
    if j == 0:
        ans = [str1[::-1], str2[::-1]]
        return ans
    if backtrack[i][j] == 0:
        str1 += s1[i-1]
        str2 += "-"
        return output_lcs(backtrack, s1, s2, i - 1, j, str1, str2)
    if backtrack[i][j] == 1:
        if i != len(s1):
            str1 += '-'
            str2 += s2[j-1]
            return output_lcs(backtrack, s1, s2, i, j - 1, str1, str2)
        else:
            return output_lcs(backtrack, s1, s2, i, j - 1, str1, str2)
    else:
        str1 += s1[i-1]
        str2 += s2[j-1]
        return output_lcs(backtrack, s1, s2, i - 1, j - 1, str1, str2)


sys.setrecursionlimit(2000)
match, mismatch, indel = [int(i) for i in input().split(" ")]
s1 = input()
s2 = input()
backtrack = lcs_backtrack(s1, s2, match, mismatch, indel)
ans = output_lcs(backtrack, s1, s2, len(s1), len(s2), "", "")
for x in ans:
    print(x)

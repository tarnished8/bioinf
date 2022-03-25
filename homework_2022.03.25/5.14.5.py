import sys


def lcs_backtrack(s1, s2, s3):
    s = [[[0 for k in range(len(s3) + 1)] for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    backtrack = [[[0 for k in range(len(s3) + 1)] for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    for i in range(len(s1)):
        backtrack[i + 1][0][0] = 0
    for j in range(len(s2)):
        backtrack[0][j + 1][0] = 1
    for k in range(len(s3)):
        backtrack[0][0][k + 1] = 2
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            for k in range(1, len(s3) + 1):
                if s1[i - 1] == s2[j - 1] == s3[k - 1]:
                    cur = 1
                else:
                    cur = 0
                s[i][j][k] = max(s[i - 1][j][k], s[i][j - 1][k], s[i - 1][j - 1][k], s[i][j - 1][k - 1], s[i - 1][j][k - 1], s[i - 1][j - 1][k - 1] + cur)
                if s[i][j][k] == s[i - 1][j][k]:
                    backtrack[i][j][k] = 0
                elif s[i][j][k] == s[i][j - 1][k]:
                    backtrack[i][j][k] = 1
                elif s[i][j][k] == s[i][j][k - 1]:
                    backtrack[i][j][k] = 2
                elif s[i][j][k] == s[i - 1][j - 1][k]:
                    backtrack[i][j][k] = 3
                elif s[i][j][k] == s[i][j - 1][k - 1]:
                    backtrack[i][j][k] = 4
                elif s[i][j][k] == s[i - 1][j][k - 1]:
                    backtrack[i][j][k] = 5
                elif s[i][j][k] == s[i - 1][j - 1][k - 1]:
                    backtrack[i][j][k] = 6
                else:
                    backtrack[i][j][k] = 7
    print(s[i][j][k])
    return backtrack


def output_lcs(backtrack, s1, s2, s3, i, j, k, str1, str2, str3):
    if i == j == k == 0:
        ans = [str1[::-1], str2[::-1], str3[::-1]]
        return ans
    elif backtrack[i][j][k] == 0:
        str1 += s1[i - 1]
        str2 += '-'
        str3 += '-'
        return output_lcs(backtrack, s1, s2, s3, i - 1, j, k, str1, str2, str3)
    if backtrack[i][j][k] == 1:
        str1 += '-'
        str2 += s2[j - 1]
        str3 += '-'
        return output_lcs(backtrack, s1, s2, s3, i, j - 1, k, str1, str2, str3)
    if backtrack[i][j][k] == 2:
        str1 += '-'
        str2 += '-'
        str3 += s3[k - 1]
        return output_lcs(backtrack, s1, s2, s3, i, j, k - 1, str1, str2, str3)
    if backtrack[i][j][k] == 3:
        str1 += s1[i - 1]
        str2 += s2[j - 1]
        str3 += '-'
        return output_lcs(backtrack, s1, s2, s3, i - 1, j - 1, k, str1, str2, str3)
    if backtrack[i][j][k] == 4:
        str1 += '-'
        str2 += s2[j - 1]
        str3 += s3[k - 1]
        return output_lcs(backtrack, s1, s2, s3, i, j - 1, k - 1, str1, str2, str3)
    if backtrack[i][j][k] == 5:
        str1 += s1[i - 1]
        str2 += '-'
        str3 += s3[k - 1]
        return output_lcs(backtrack, s1, s2, s3, i - 1, j, k - 1, str1, str2, str3)
    else:
        str1 += s1[i - 1]
        str2 += s2[j - 1]
        str3 += s3[k - 1]
        return output_lcs(backtrack, s1, s2, s3, i - 1, j - 1, k - 1, str1, str2, str3)


sys.setrecursionlimit(2000)
s1 = input()
s2 = input()
s3 = input()
backtrack = lcs_backtrack(s1, s2, s3)
ans = output_lcs(backtrack, s1, s2, s3, len(s1), len(s2), len(s3), "", "", "")
for x in ans:
    print(x)
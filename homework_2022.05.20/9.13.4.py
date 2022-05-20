def count(symb, n, string):
    return sum([1 for s in string[:n] if s == symb])


def first_occurence(string1):
    string = ''.join(sorted([x for x in string1]))
    dict = {
        "$": string.find("$"),
        "A": string.find("A"),
        "C": string.find("C"),
        "G": string.find("G"),
        "T": string.find("T")
    }
    return dict


def bw_matching(first_occurence, last, pattern, suffix_array):
    top = 0
    bottom = len(last) - 1
    while top <= bottom:
        if pattern:
            symb = pattern[-1]
            pattern = pattern[:-1]
            if symb in last[top:bottom+1]:
                top = first_occurence[symb] + count(symb, top, last)
                bottom = first_occurence[symb] + count(symb, bottom + 1, last) - 1
            else:
                return -1
        else:
            return list(suffix_array[top:bottom + 1])


def bwt(string):
    matrix = []
    for i in range(len(string)):
        matrix.append(string[-(i + 1):] + string[:-(i + 1)])
    matrix.sort()
    ans = []
    for x in matrix:
        ans.append(x[-1])
    return ''.join(ans)


string = input() + "$"
patterns = input().split()
first_occurence = first_occurence(string)
matrix = []
for i in range(len(string)):
    matrix.append(string[-(i+1):] + string[:-(i+1)])
matrix.sort()
ans = []
for x in matrix:
    ans.append(x[-1])
string = ''.join(ans)
suffix_array = []
for m in matrix:
    suffix_array.append(len(string) - m.find("$") - 1)
for x in patterns:
    ans = bw_matching(first_occurence, string, x, suffix_array)
    if ans != -1:
        print(x + ":", end=" ")
        print(*sorted(ans))
    else:
        print(x + ":")

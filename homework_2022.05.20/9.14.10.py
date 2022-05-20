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


def bw_matching(pattern):
    global first_occurence
    global string
    global suffix_array
    top = 0
    bottom = len(string) - 1
    while top <= bottom:
        if pattern:
            symb = pattern[-1]
            pattern = pattern[:-1]
            if symb in string[top:bottom+1]:
                top = first_occurence[symb] + count(symb, top, string)
                bottom = first_occurence[symb] + count(symb, bottom + 1, string) - 1
            else:
                return []
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


def pattern_split(pattern, d):
    l = len(pattern)
    m = int(l / (d + 1))
    c = [j for j in range(0, l - m + 1, m)]
    c.append(l)
    split = [[pattern[c[i - 1]:c[i]], c[i - 1]] for i in range(1, len(c))]
    return split


def is_approximately_matching(string, pattern, pos, d):
    mis_count = 0
    for i in range(len(pattern)):
        symb = pattern[i]
        if symb != string[pos + i]:
            mis_count += 1
            if mis_count > d:
                return False
    return True


def approximate_matches(pattern, string, d):
    positions = []
    p_split = pattern_split(pattern, d)
    for x in p_split:
        seed = x[0]
        string_pos = x[1]
        possible_pos = bw_matching(seed)
        for pos in possible_pos:
            pattern_pos = pos - string_pos
            if pattern_pos < 0 or pattern_pos + len(pattern) > len(string):
                continue
            if is_approximately_matching(string, pattern, pattern_pos, d):
                positions.append(pattern_pos)
    return set(positions)


string1 = input()
patterns = input().split()
d = int(input())
string = string1 + "$"
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
    ans = approximate_matches(x, string1, d)
    if ans:
        print(x + ":", end=" ")
        print(*sorted(ans))
    else:
        print(x + ":")

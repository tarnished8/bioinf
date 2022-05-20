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


def bw_matching(first_occurence, last, pattern):
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
                return 0
        else:
            return bottom - top + 1


string = input()
patterns = input().split()
first_occurence = first_occurence(string)
for x in patterns:
    print(bw_matching(first_occurence, string, x), end=" ")

chars = "ACGT"


def ham_dist(a, b):
    mis = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            mis = mis + 1
    return mis


def neighbors(pattern, d):
    if d == 0:
        return [pattern]
    temp = neighbors(pattern[1:], d-1)
    ans = [char + t for t in temp for char in chars]
    if d < len(pattern):
        temp = neighbors(pattern[1:], d)
        ans += [pattern[0] + t for t in temp]
    return list(set(ans))


def motif_enumeration(dna: list, k, d):
    patterns = []
    subs = []
    for j in range(len(dna)):
        subs.append([dna[j][i:i+k] for i in range(len(dna[j]) - k + 1)])
    for i in range(len(dna[0]) - k + 1):
        for k_mer in neighbors(dna[0][i:i+k], d):
            for j in range(1, len(dna)):
                for sub in subs[j]:
                    if ham_dist(k_mer, sub) <= d:
                        break
                else:
                    break
            else:
                patterns.append(k_mer)
    return list(set(patterns))


k = int(input())
d = int(input())
dna = input().split()
for word in motif_enumeration(dna, k, d):
    print(word + " ")

chars = "ACGT"


def all_k_mers(cur, k, k_mers):
    if k == 0:
        k_mers.append(cur)
    else:
        for i in range(4):
            cur1 = cur + chars[i]
            all_k_mers(cur1, k-1, k_mers)


def ham_dist(a, b):
    mis = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            mis = mis + 1
    return mis


def distance_between_pattern_and_strings(pattern, dna):
    k = len(pattern)
    dist = 0
    for text in dna:
        ham_distance = 999999999999999999999999
        for i in range(len(text) - k + 1):
            if ham_dist(pattern, text[i:i+k]) < ham_distance:
                ham_distance = ham_dist(pattern, text[i:i+k])
        dist += ham_distance
    return dist


def median_string(dna, k):
    dist = 999999999999999999999999
    k_mers = []
    all_k_mers("", k, k_mers)
    for pattern in k_mers:
        if distance_between_pattern_and_strings(pattern, dna) < dist:
            dist = distance_between_pattern_and_strings(pattern, dna)
            median = pattern
    return median


k = int(input())
dna = input().split()
print(median_string(dna, k))


def ham_dist(a, b):
    mis = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            mis = mis + 1
    return mis


print(ham_dist(input(), input()))

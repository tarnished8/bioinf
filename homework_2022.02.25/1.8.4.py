def ham_dist(a, b):
    mis = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            mis = mis + 1
    return(mis)


pattern = input()
text = input()
d = int(input())
for i in range(len(text) - len(pattern) + 1):
    if ham_dist(pattern, text[i:i+len(pattern)]) <= d:
        print(str(i) + " ")

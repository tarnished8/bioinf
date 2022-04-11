def print_permutation(a):
    b = []
    for x in a:
        if x > 0:
            b.append("+" + str(x))
        else:
            b.append(str(x))
    print(*b)


permutation = [int(x) for x in input().split(" ")]
w = open("output.txt", "w")
for i in range(1, len(permutation) + 1):
    if permutation[i-1] != i:
        abs_permutation = [abs(x) for x in permutation]
        pos = abs_permutation.index(abs(i))
        permutation[i-1:pos+1] = [-x for x in permutation[i-1:pos+1]][::-1]
        print_permutation(permutation)
    if permutation[i-1] == -i:
        permutation[i-1] = i
        print_permutation(permutation)


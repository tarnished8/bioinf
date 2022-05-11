# https://github.com/tarnished8/bioinf/blob/main/homework_2022.04.15/6.4.4.py


def print_permutation(a):
    b = []
    for x in a:
        if x > 0:
            b.append("+" + str(x))
        else:
            b.append(str(x))
    print(*b)

# сравниваем теперь не с i, а с permutation_fin[i-1]
permutation = [int(x) for x in input().split(" ")]
permutation_fin = [int(x) for x in input().split(" ")]
w = open("output.txt", "w")
for i in range(1, len(permutation) + 1):
    if permutation[i-1] != permutation_fin[i-1]:
        abs_permutation = [abs(x) for x in permutation]
        pos = abs_permutation.index(abs(permutation_fin[i-1]))
        permutation[i-1:pos+1] = [-x for x in permutation[i-1:pos+1]][::-1]
        print_permutation(permutation)
    if permutation[i-1] == -permutation_fin[i-1]:
        permutation[i-1] = permutation_fin[i-1]
        print_permutation(permutation)
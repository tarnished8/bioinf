def reverse_complimentary(genome):
    gene = list(genome)
    gene.reverse()
    for i in range(len(gene)):
        if gene[i] == 'C':
            gene[i] = 'G'
        elif gene[i] == 'G':
            gene[i] = 'C'
        elif gene[i] == 'A':
            gene[i] = 'T'
        elif gene[i] == 'T':
            gene[i] = 'A'
    return ''.join(gene)


k = int(input())
genome1 = input()
genome2 = input()
for i in range(len(genome1) - k + 1):
    cur = genome1[i:i+k]
    for j in range(len(genome2) - k + 1):
        if cur == genome2[j:j+k] or cur == reverse_complimentary(genome2[j:j+k]):
            print("(" + str(i) + ", " + str(j) + ")")


gene = list(input())
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
f = open('text.txt', 'w')
f.write("".join(gene))

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


f = open('RNA_codon_table_1.txt', 'r')
codons = {}
for x in f:
    a, b = x.strip('\n').split(" ")
    codons[a] = b
text = input()
peptide = input()
patterns = [""]
final_patterns = []
for x in peptide:
    patterns = [y + z for y in patterns for z in codons.keys() if codons[z] == x]
for x in patterns:
    x = x.replace("U", "T")
    final_patterns.append(x)
    final_patterns.append(reverse_complimentary(x))
for i in range(len(text) - 3 * len(peptide) + 1):
    x = text[i:i+3*len(peptide)]
    if x in final_patterns:
        print(x)


f = open('integer_mass_table.txt', 'r')
masses = {}
for x in f:
    a, b = x.strip('\n').split(" ")
    masses[a] = int(b)
peptide = input()
n = len(peptide)
prefix_masses = [0]
for s in peptide:
    prefix_masses.append(prefix_masses[-1] + masses[s])
peptide_mass = prefix_masses[-1]
cyclospectrum = [0]
for i in range(n):
    for j in range(i + 1, n + 1):
        cyclospectrum.append(prefix_masses[j] - prefix_masses[i])
        if i != 0 and j < n:
            cyclospectrum.append(peptide_mass - (prefix_masses[j] - prefix_masses[i]))
cyclospectrum.sort()
for x in cyclospectrum:
    print(x, end=" ")

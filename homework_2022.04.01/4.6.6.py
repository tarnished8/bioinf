def peptide_spectrum(peptide):
    f = open('integer_mass_table.txt', 'r')
    masses = {}
    for x in f:
        a, b = x.strip('\n').split(" ")
        masses[a] = int(b)
    peptide = [int(x) for x in peptide.split("-")]
    n = len(peptide)
    prefix_masses = [0]
    for s in peptide:
        prefix_masses.append(prefix_masses[-1] + s)
    spectrum1 = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            spectrum1.append(prefix_masses[j] - prefix_masses[i])
    spectrum1.sort()
    return spectrum1


def cyclospectrum(peptide):
    f = open('integer_mass_table.txt', 'r')
    masses = {}
    for x in f:
        a, b = x.strip('\n').split(" ")
        masses[a] = int(b)
    peptide = [int(x) for x in peptide.split("-")]
    n = len(peptide)
    prefix_masses = [0]
    for s in peptide:
        prefix_masses.append(prefix_masses[-1] + s)
    peptide_mass = prefix_masses[-1]
    cyclospectrum1 = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            cyclospectrum1.append(prefix_masses[j] - prefix_masses[i])
            if i != 0 and j < n:
                cyclospectrum1.append(peptide_mass - (prefix_masses[j] - prefix_masses[i]))
    cyclospectrum1.sort()
    return cyclospectrum1


def is_not_consistent(spectrum1, spectrum2):
    for x in spectrum1:
        if spectrum1.count(x) > spectrum2.count(x):
            return True
    return False


def mass(peptide):
    return sum([int(x) for x in peptide[1:].split("-")])


def cyclopeptide_sequencing(spectrum, masses):
    candidates = [[''], []]
    final_candidates = []
    a = 1
    while candidates[(a + 1) % 2]:
        candidates[a] = [x + "-" + y for x in candidates[(a + 1) % 2] for y in masses.values()]
        for i in range(len(candidates[a])):
            peptide = candidates[a][i]
            if mass(peptide) == spectrum[-1]:
                if cyclospectrum(peptide[1:]) == spectrum and peptide[1:] not in final_candidates:
                    final_candidates.append(peptide[1:])
                candidates[a][i] = 'asd'
            elif is_not_consistent(peptide_spectrum(peptide[1:]), spectrum):
                candidates[a][i] = 'asd'
        candidates[a] = set([x for x in candidates[a] if x != "asd"])
        a = (a + 1) % 2
    return final_candidates


f = open('integer_mass_table.txt', 'r')
masses = {}
for x in f:
    a, b = x.strip('\n').split(" ")
    masses[a] = b
spectrum = [int(x) for x in input().split(" ")]
for x in cyclopeptide_sequencing(spectrum, masses):
    print(x, end=" ")










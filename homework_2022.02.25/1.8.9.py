chars = "ACGT"


def neighbors(pattern, d):
    if d == 0:
        return [pattern]
    temp = neighbors(pattern[1:], d-1)
    ans = [char + t for t in temp for char in chars]
    if d < len(pattern):
        temp = neighbors(pattern[1:], d)
        ans += [pattern[0] + t for t in temp]
    return list(set(ans))


text = input()
k = int(input())
d = int(input())
patterns = []
freqmap = {}
for i in range(len(text) - k + 1):
    pattern = text[i:i+k]
    neighborhood = neighbors(pattern, d)
    for j in range(len(neighborhood)):
        if neighborhood[j] not in freqmap:
            freqmap[neighborhood[j]] = 1
        else:
            freqmap[neighborhood[j]] += 1
M = max(freqmap.values())
for pattern in freqmap.keys():
    if freqmap[pattern] == M:
        patterns.append(pattern)
print(patterns)

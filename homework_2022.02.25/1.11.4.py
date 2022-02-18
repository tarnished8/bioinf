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


f = open("text.txt", "w")
for x in neighbors(input(), 2):
    f.write(x + '\n')

def most_probable(text, k, profile):
    char_values = {
        "A": 0,
        "C": 1,
        "G": 2,
        "T": 3
    }
    max = 0
    for i in range(len(text) - k):
        cur = text[i:i+k]
        score = 1
        for j in range(k):
            score = score * profile[int(char_values.get(cur[j]))][j]
        if score > max:
            max = score
            ans = cur
    return ans


f = open("text.txt", "r")
text = f.readline()
k = int(f.readline())
profile = []
for j in range(4):
    line = f.readline()
    profile.append([float(x) for x in line.split(' ')])
print(most_probable(text, k, profile))
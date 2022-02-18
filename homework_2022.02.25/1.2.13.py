def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count = count + 1
    return count


arr = []
M = 0
text = input()
l = int(input())
for j in range(len(text) - l + 1):
    cur = pattern_count(text, text[j:j+l])
    if cur == M and text[j:j+l] not in arr:
        arr.append(text[j:j+l])
    if cur > M:
        M = cur
        arr.clear()
        arr.append(text[j:j+l])
print(arr)

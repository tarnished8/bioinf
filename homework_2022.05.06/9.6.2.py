text = input()
suffixes = []
for i in range(len(text)):
    suffixes.append(text[i:])
for x in sorted(suffixes):
    print(len(text) - len(x), end=" ")
    

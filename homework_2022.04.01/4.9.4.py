spectrum = [int(x) for x in input().split(" ")]
n = len(spectrum)
for i in range(1, n):
    for j in range(i):
        if spectrum[i] - spectrum[j] != 0:
            print(abs(spectrum[i] - spectrum[j]), end=" ")

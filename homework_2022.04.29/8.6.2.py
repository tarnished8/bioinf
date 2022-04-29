def distance(p1, p2, m):
    dist = sum([(p1[i] - p2[i]) ** 2 for i in range(m)])
    return dist ** (1/2)


f = open("input.txt", "r")
k, m = f.readline().split()
k = int(k)
m = int(m)
data = []
for line in f.readlines():
    data.append([])
    for x in line.split():
        data[-1].append(float(x))
centers = [data[0]]
while len(centers) < k:
    maximum = 0
    cur = centers[-1]
    for point in data:
        dist_cent = 0
        minimum = 9999999999
        for center in centers:
            if distance(point, center, m) < minimum:
                minimum = distance(point, center, m)
        dist_cent = minimum
        if dist_cent > maximum:
            cur = point
            maximum = dist_cent
    centers.append(cur)
for center in centers:
    print(*center)

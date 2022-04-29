def dist_between_clusters(cl1, cl2, dist):
    distance = 0
    for x in cl1:
        for y in cl2:
            distance += dist[x][y]
    return distance / (len(cl1) * len(cl2))


f = open("input.txt", 'r')
n = int(f.readline())
dist = [[float(x) for x in line.split(" ")] for line in f.readlines()]
clusters = [[i] for i in range(n)]

for i in range(n - 1):
    min_dist = 99999999
    for j in range(len(clusters)):
        for k in range(j + 1, len(clusters)):
            if dist_between_clusters(clusters[j], clusters[k], dist) < min_dist:
                min_dist = dist_between_clusters(clusters[j], clusters[k], dist)
                j1 = j
                k1 = k
    clusters.append(clusters[j1] + clusters[k1])
    clusters.pop(j1)
    clusters.pop(k1 - 1)
    ans = [x + 1 for x in clusters[-1]]
    print(*ans)

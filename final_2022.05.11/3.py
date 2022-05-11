# https://github.com/tarnished8/bioinf/blob/main/homework_2022.04.29/8.8.3.py


import random


def center_of_mass(points, m):
    l = len(points)
    ans = [0 for i in range(m)]
    for j in range(l):
        for k in range(m):
            ans[k] += points[j][k]
    for i in range(m):
        ans[i] = ans[i] / l
    return ans


def distance(p1, p2, m):
    dist = sum([(p1[i] - p2[i]) ** 2 for i in range(m)])
    return dist ** (1/2)


def centers_to_clusters(data, centers, m):
    clusters_marks = [-1 for i in range(len(data))]
    for i in range(len(data)):
        point = data[i]
        min = 999999
        for center in centers:
            if distance(point, center, m) < min:
                min = distance(point, center, m)
                cur_center = center
        clusters_marks[i] = centers.index(cur_center)
    return clusters_marks


def clusters_to_centers(data, clusters_marks, m):
    centers = []
    for i in range(k):
        cur_cluster = []
        for j in range(len(data)):
            if clusters_marks[j] == i:
                cur_cluster.append(data[j])
        centers.append(center_of_mass(cur_cluster, m))
    return centers


def dist_point_cent(point, centers, m):
    min = 999999
    for center in centers:
        if distance(point, center, m) < min:
            min = distance(point, center, m)
    return min


# просто добавили такую функцию
def initializer(data, k, m):
    centers = [data[-1]]
    while len(centers) < k:
        distances = []
        for i in range(len(data)):
            point = data[i]
            distances.append(dist_point_cent(point, centers, m))
        distances = [x ** 2 for x in distances]
        new = random.choices(data, distances, k=1)[0]
        centers.append(new)
    return centers


f = open("input.txt", "r")
k, m = f.readline().split()
k = int(k)
m = int(m)
data = []
for line in f.readlines():
    data.append([])
    for x in line.split():
        data[-1].append(float(x))
centers = initializer(data, k, m)
old_centers = []
while centers != old_centers:
    old_centers = centers
    clusters_marks = centers_to_clusters(data, centers, m)
    centers = clusters_to_centers(data, clusters_marks, m)

for center in centers:
    for i in range(len(center)):
        center[i] = round(center[i], 3)
    print(*center)

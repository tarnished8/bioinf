def longest_path(start, finish, graph):
    s = [0 for i in range(finish + 1)]
    pred = [-1 for i in range(finish + 1)]
    for i in range(finish + 1):
        pred[i] = -1
        for str in graph:
            if str[1] == i:
                cur = s[str[0]] + str[2]
                if cur > s[i]:
                    s[i] = cur
                    pred[i] = str[0]
    ans = [finish]
    print(s[-1])
    j = -1
    while j != start:
        ans.append(pred[j])
        j = pred[j]
    for i in reversed(ans):
        print(i, end=" ")


f = open("text.txt", "r")
start, finish = f.readline().split(" ")
start = int(start)
finish = int(finish)
graph = []
for line in f:
    graph.append([int(x) for x in line.strip("\n").split(" ")])
longest_path(start, finish, graph)


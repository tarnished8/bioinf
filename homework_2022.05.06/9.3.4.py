def trie(data):
    trie = []
    count = 1
    for string in data:
        cur_node = 0
        for i in range(len(string)):
            cur_symb = string[i]
            for edge in trie:
                if edge[0] == cur_node and edge[2] == cur_symb:
                    cur_node = edge[1]
                    break
            else:
                new_node = count
                trie.append([cur_node, new_node, cur_symb])
                cur_node = new_node
                count += 1
    return trie


data = [x for x in input().split()]
for x in trie(data):
    print(*x)
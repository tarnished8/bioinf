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


def path(start, finish, adj):
    visited = [False for i in range(10*len(adj))]
    visited[start] = True
    cur = start
    stack = [start]
    while True:
        pos = [x for x in adj[cur] if not visited[x]]
        if not pos:
            stack.pop()
            cur = stack[-1]
        else:
            cur = pos[0]
            stack.append(cur)
            if cur == finish:
                return stack
            visited[cur] = True


def prefix_trie_matching(text, trie):
    symb = text[0]
    not_leaves = [x[0] for x in trie]
    adj = [[] for i in range(100*trie[-1][1])]
    for x in trie:
        adj[x[0]].append(x[1])
    v = 0
    i = 0
    while True:
        if v not in not_leaves:
            v_path = path(0, v, adj)
            string = ""
            for j in range(len(v_path) - 1):
                for x in trie:
                    if x[0] == v_path[j] and x[1] == v_path[j+1]:
                        string += x[2]
            return string
        else:
            for x in trie:
                if x[0] == v and x[2] == symb:
                    v = x[1]
                    i += 1
                    if i < len(text):
                        symb = text[i]
                        break
                    else:
                        break
            else:
                return 'no matches'


text = input()
data = [x for x in input().split()]
this_trie = trie(data)
k = 0
ans = {}
while text:
    if prefix_trie_matching(text, this_trie) != 'no matches':
        substr = prefix_trie_matching(text, this_trie)
        if substr not in ans:
            ans[substr] = [k]
        else:
            ans[substr].append(k)
    text = text[1:]
    k += 1
for x in ans.keys():
    print(x + ":", *ans.get(x))


filename = "inputbg2.txt" # input("Test case file name: ")
with open(filename, "r") as f:
    lines = [line.strip() for line in f.readlines()]

    N = int(lines[0])
    i = int(lines[1])
    graph = [set() for p in range(N)]
    for ln in range(2, 2+i):
        s, t = list(map(int, lines[ln].split()))
        graph[s].add(t)

    for idx, g in enumerate(graph):
        graph[idx] = sorted(g)

    dangerous = set()
    x = int(lines[2+i])
    for j in range(3+i, len(lines)):
        dangerous.add(int(lines[j]))

result = []
visited = set()
curPath = []
def dfs(node):
    # if node in visited or node in too dangerous
    # terminate path
    # if node == N-1:
    #     curPath.append(node)
    #     result.append("-".join(list(map(str, curPath))))
    #     curPath.pop()
        # curPath.clear()
        # return
    if node in visited:
        # result.append("-".join(list(map(str, curPath))))
        # curPath.clear()
        return
    else:
        curPath.append(node)
        if node == N-1:
            result.append("-".join(list(map(str, curPath))))
        for c in graph[node]:
            if c not in dangerous:
                dfs(c)
        curPath.pop()

dfs(0)
for p in result:
    print(p)



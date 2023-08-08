with open("input2.txt", "r") as f:
    lines = f.readlines()
    t,d = list(map(int, lines[0].split()))
    graph = dict()
    for i in range(1, 1+t):
        graph[lines[i].strip()] = []
    
    for j in range(1+t, len(lines)):
        u,v = lines[j].strip().split()
        graph[u].append(v)

    print(graph)

tasks = sorted(graph.keys())
for ta in tasks:
    graph[ta].sort()
topo = []
colors = {owo: 0 for owo in tasks}
def dfs(start, graph):
    # pass
    # use iterative search
    

    stk = []
    stk.append(start)
    # colors[start] = 1
    # topo = [] # finishing times
    visited = set()
    while len(stk) > 0:
        node = stk[-1]
        if colors[node] == 1: # in progress
            colors[node] = 2
            stk.pop()
            topo.append(node)
        elif colors[node] == 2: # done
            stk.pop()

        else: # not visited
            colors[node] = 1
            visited.add(node)
            for c in graph[node]:
                if colors[c] == 0:
                    stk.append(c)
                if c in visited:
                    return False
                # elif colors[c] == 2:
                #     return False
                
    return True

print(topo)
tasks.reverse()
for te in tasks:
    if colors[te] == 0:
        res = dfs(te, graph)
        if res == False:
            topo = []
            break

        
if len(topo) == 0:
    print("IMPOSSIBLE")

else:
    topo.reverse()
    print(topo)
    
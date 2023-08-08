numtasks, numedges = list(map(int, input().split()))

tasks = []
for i in range(numtasks):
    tasks.append(input())

edges = []
for i in range(numedges):
    edges.append(tuple(map(int, input().split())))
# initialize the graphs
tasks = sorted(set(tasks))
edges = sorted(set(edges))

# build graph:
graph = {k: [] for k in tasks}
for u, v in edges:
    graph[u].append(v)

# solve
visited = set()
topo = []
# initialize visited
# traverse in order of task list
# add to topological order when finished visiting
def dfs(node):
    visited.add(node)
    for c in graph[node]:
        if c not in visited:
            return dfs(c)
        else:
            return False
    return True
    
# check to ensure list is in topological order
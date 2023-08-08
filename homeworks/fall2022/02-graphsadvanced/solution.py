# read file
from heapq import heappush, heappop, heapify
filename = "input2.txt"
with open(filename, "r") as f:
    linecount = 0
    lines = f.readlines()
    j, c = list(map(int, lines[linecount].split()))
    linecount += 1
    junctions = dict()
    for junk in range(j):
        name, jtype = lines[linecount].strip().split()
        junctions[name] = jtype
        linecount += 1
    edges = []
    lightparents = dict()
    for _ in range(c):
        u,v, cost = lines[linecount].strip().split()
        cost = int(cost)
        edges.append((u,v,cost))
        if junctions[u] == "switch":
            lightparents[v] = u
        linecount += 1




def buildtree(edges, nodes):
    # create mst containing only junctions, breaker and outlet. wire while while breaker and outlet are not in the same group[]
    minCost = 0
    heap = []
    partitions = {node:node for node in nodes.keys()}
    def find(x):
        p = x
        while p != partitions[p]:
            partitions[p] = partitions[partitions[p]]
            p = partitions[p]
        return p
    def union(x,y):
        px = find(x)
        py = find(y)
        if px != py:
            partitions[px] = py
        
    allowedtypes = ["breaker", "outlet", "box"]
    remstuff = []
    for u,v,cost in edges:
        if nodes[u] in allowedtypes and nodes[v] in allowedtypes:
            heappush(heap, (cost, u, v))
        else:
            remstuff.append((u,v,cost))
    edges = remstuff
    def krustycrabs():
        nonlocal minCost
        while len(heap) > 0:
            cost, u,v = heappop(heap)
            if find(u)!=find(v):
                union(u,v)
                minCost += cost
    krustycrabs()
    # first edges considered should only contain breaker, outlet, and junction
    remstuff2 = []
    allowedtypes.append("switch")
    for u,v, cost in edges:
        if nodes[u] in allowedtypes and nodes[v] in allowedtypes:
            heappush(heap, (cost, u, v))
        else:
            remstuff2.append((u,v,cost))
    edges = remstuff2
    # add the switches to MST T* 
    krustycrabs()
    # second batch should only consider edges containing switches
    # add lights to MST T*
        # light edges must be light light or light switch paths
        # add light light edge only if the lights share two switches
    # third batch of edges should only consider light-light edges and 
    allowed = ["light", "switch"]
    for u,v,cost in edges:
        if nodes[u] == "light" and nodes[v] == "light":
            if lightparents[u] == lightparents[v]:
                heappush(heap, (cost, u,v))
        elif nodes[u] in allowed and nodes[v] in allowed:
            heappush(heap, (cost, u,v))
        
    # final result is the minimal cost circuit
    krustycrabs()
    return minCost

result = buildtree(edges, junctions)
print("MST cost: ", result)
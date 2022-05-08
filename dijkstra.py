# Single Source Shortest Path - Greedy approach 
# sample input 
# 6 7
# A B 4
# A C 2
# B C 5
# B D 10
# C E 3
# D F 11
# E D 4
# A D

# sample output 
# Paths Exists A to D with costs 9 

import heapq
from collections import defaultdict

def shortestPath(graph,src,dest):
    h = []
    # keep a track record of vertices with cost and update them
    # heappop will return vertex with least cost 
    # sre -> min -> min -> min -> dst termination condition 
    # if heap is empty then also terminates 
    heapq.heappush(h,(0,src))
    
    while len(h) != 0:
        currcost, currvtx = heapq.heappop(h)
        if currvtx == dest:
            print("Path Exists {} to {} with costs {}". format(src,dest,currcost))
            break
        for neigh, neighCost in graph[currvtx]:
            heapq.heappush(h,(currcost+neighCost, neigh))
    
graph = defaultdict(list)
v, e = map(int, input().split())
for i in range(e):
    u,v,w = map(str, input().split())
    graph[u].append((v, int(w)))

src, dest = map(str, input().split())
shortestPath(graph,src,dest)


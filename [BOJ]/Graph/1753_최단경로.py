import sys
from queue import PriorityQueue

input = sys.stdin.readline
INF = float("inf")

V, E = map(int, input().split())

distance = [10000000] * (V + 1)
K = int(input())
distance[K] = 0

adj_list = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))

visited = [False] * (V + 1)

q = PriorityQueue()
q.put((0, K))

curr_node = K
while q.qsize() > 0:
    curr_node = q.get()
    c_v = curr_node[1]
    if visited[c_v]:
        continue
    visited[c_v] = True
    # print(f"c_v : {c_v}")

    for next_node in adj_list[c_v]:
        node_idx, edge_dist = next_node[0], next_node[1]
        if distance[node_idx] > distance[c_v] + edge_dist:
            distance[node_idx] = distance[c_v] + edge_dist
            q.put((distance[node_idx], node_idx))


for i in range(1, V + 1):
    if distance[i] == 10000000:
        print("INF")
    else:
        print(distance[i])

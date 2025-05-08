import sys
from queue import PriorityQueue

input = sys.stdin.readline
INF = float("inf")

V, E = map(int, input().split())
K = int(input())

adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))
    # adj_list[v].append((u, w))

distance = [INF] * (V + 1)
distance[K] = 0

pq = PriorityQueue()
pq.put((distance[K], K))

while pq.qsize() > 0:
    dist, node = pq.get()

    for next in adj_list[node]:
        next_node_idx, next_node_edge = next[0], next[1]
        if distance[next_node_idx] > (dist + next_node_edge):
            distance[next_node_idx] = dist + next_node_edge
            pq.put((distance[next_node_idx], next_node_idx))


for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

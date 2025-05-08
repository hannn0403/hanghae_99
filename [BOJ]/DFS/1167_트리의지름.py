import sys
from collections import deque

V = int(input())
adj_list = [[] for _ in range(V + 1)]

for _ in range(1, V + 1):
    l = list(map(int, input().split()))
    curr_node = l[0]

    idx = 1
    while l[idx] != -1:
        connected_node_idx = l[idx]
        connected_node_dist = l[idx + 1]
        adj_list[curr_node].append((connected_node_idx, connected_node_dist))
        idx += 2

# print(adj_list)
distance = [0] * (V + 1)
max_dist = 0
visited = [False] * (V + 1)


def BFS(node):
    visited[node] = True
    queue = deque()
    queue.append((node, 0))
    curr_dist = 0
    while queue:
        node, dist = queue.popleft()
        if dist > curr_dist:
            curr_dist = dist

        for next_node_idx, next_node_dist in adj_list[node]:
            if not visited[next_node_idx]:
                visited[next_node_idx] = True
                queue.append((next_node_idx, dist + next_node_dist))
                distance[next_node_idx] = distance[node] + next_node_dist

    return curr_dist


# 각 노드에서 갈 수 있는 최대 거리
BFS(1)
Max = 1

for i in range(2, V + 1):
    if distance[Max] < distance[i]:
        Max = i

distance = [0] * (V + 1)
visited = [False] * (V + 1)
BFS(Max)
distance.sort()
print(distance[V])
# for node in range(1, V + 1):
#     if not visited[node]:
#         curr_max_dist = BFS(node)
#         if max_dist < curr_max_dist:
#             max_dist = curr_max_dist

# print(max_dist)

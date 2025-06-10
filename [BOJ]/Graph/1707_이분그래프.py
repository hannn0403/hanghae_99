import sys
from collections import deque

input = sys.stdin.readline

K = int(input())

for tc in range(K):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    visited = [False] * (V + 1)
    bipartite = True

    for _ in range(E):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    group_dict = {0: set(), 1: set()}
    for i in range(1, V+1):
        if visited[i]:
            continue

        queue = deque()
        queue.append((i, 0))
        visited[i] = True

        while queue and bipartite:
            node, group = queue.popleft()
            group_dict[group].add(node)

            for next_node in adj_list[node]:
                if visited[next_node]:
                    if next_node in group_dict[group]:
                        bipartite = False
                        print("NO")
                        break
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append((next_node, (group + 1) % 2))
        if not bipartite:
            break

    # print(f"group_dict : {group_dict}")
    if bipartite:
        print("YES")

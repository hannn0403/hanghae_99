import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline 

N, M = map(int, input().split())

visited = [False] * (N + 1)
connected_dict = {}
for i in range(1, N + 1):
    connected_dict[i] = []

for _ in range(M):
    u, v = map(int, input().split())
    connected_dict[u].append(v)
    connected_dict[v].append(u)

# print(f"visited : {visited}")
# print(f"connected_dict : {connected_dict}")


def find(node, list):
    global visited
    # list.append(node)

    for neigh in connected_dict[node]:
        if not visited[neigh]:
            visited[neigh] = True
            find(neigh, list)

    # return list


answer = 0
for i in range(1, N + 1):
    if not visited[i]:
        visited[i] = True
        find(i, [])
        answer += 1

# print(f"answer list : {answer}")
# print(f"answer len : {len(answer)}")
print(answer)

# ===============================================================================================
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

con_dict = {i:[] for i in range(1, N+1)}
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    con_dict[u].append(v)
    con_dict[v].append(u)

ans = 0
visited_node = 0
for i in range(1, N+1):
    if visited[i]:
        continue

    ans += 1
    visited[i] = True
    queue = deque()
    for j in con_dict[i]:
        visited[j] = True
        queue.append(j)

    while queue:
        curr_node = queue.pop()
        visited[curr_node] = True
        for x in con_dict[curr_node]:
            if not visited[x]:
                queue.append(x)



print(ans)

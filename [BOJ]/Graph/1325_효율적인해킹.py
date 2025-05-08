# 주의! Python으로 하면 시간초과가 나고, PyPy3로 제출해야 된다고 한다.

import sys
from collections import deque

input = sys.stdin.readline


def BFS(node):
    visited[node] = True
    queue = deque()
    queue.append(node)
    component = []

    while queue:
        node = queue.popleft()
        component.append(node)

        for next_node in adj_list[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

    return component


N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[b].append(a)

max_len = 0
max_list = []
visited = [False] * (N + 1)

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    # if not visited[i]:
    curr_list = BFS(i)

    if len(curr_list) > max_len:
        max_list = [i]
        max_len = len(curr_list)
    elif len(curr_list) == max_len:
        max_list.append(i)

max_list.sort()
for elem in max_list:
    print(elem, end=" ")

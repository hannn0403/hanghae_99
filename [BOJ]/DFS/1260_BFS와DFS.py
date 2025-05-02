import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())


connected_dict = {i: [] for i in range(1, N + 1)}
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    connected_dict[u].append(v)
    connected_dict[v].append(u)

# print(f"입력 받은 이후의 connectged dict : {connected_dict}")
for i in range(1, N + 1):
    connected_dict[i].sort()


def DFS(v):
    print(v, end=" ")
    visited[v] = True
    # print(f"connected_dict[{v}] : {connected_dict[v]} | visited : {visited}")
    for i in connected_dict[v]:
        # print(f"{v}와 연결되어 있는 {i}")
        if not visited[i]:
            # print(f"{i}의 재귀함수 실행")
            DFS(i)


visited = [False] * (N + 1)
DFS(V)


def BFS(v):
    queue = deque()
    queue.append(v)

    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=" ")
        for i in connected_dict[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


print()
visited = [False] * (N + 1)
BFS(V)

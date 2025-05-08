import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

visited = [False] * (N + 1)

# ans = 0
# ans_set = set()

possible = False


def DFS(now, depth):
    global possible
    if depth == 5:
        possible = True
        return

    visited[now] = True
    for next_node in adj_list[now]:
        if not visited[next_node]:
            DFS(next_node, depth + 1)
    visited[now] = False


for i in range(N):
    DFS(i, 1)
    if possible:
        break

if possible:
    print(1)
else:
    print(0)

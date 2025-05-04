# PyPy3로 제출해야 한다. (안 그러면 시간초과 발생) 

import sys

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

depth = [0] * (N + 1)
parent = [0] * (N + 1)
visited = [False] * (N + 1)


def BFS(node):
    queue = [node]
    visited[node] = True
    while queue:
        now_node = queue.pop(0)
        for next in tree[now_node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                parent[next] = now_node
                depth[next] = depth[now_node] + 1


BFS(1)


def executeLCA(a, b):
    if depth[a] < depth[b]:
        temp = a
        a = b
        b = temp

    while depth[a] != depth[b]:
        a = parent[a]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a


M = int(input())
mydict = dict()
for _ in range(M):
    a, b = map(int, input().split())
    if not mydict.get((a, b), 0):
        mydict[(a, b)] = mydict[(b, a)] = executeLCA(a, b)
    print(mydict.get((a, b)))

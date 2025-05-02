import sys
from collections import deque

input = sys.stdin.readline


def print_arr(arr):
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            print(f"{arr[i][j]:<3}", end=" ")
        print()
    print()


def shortest_length(start_y, start_x, end_y, end_x, graph):
    n, m = len(graph), len(graph[0])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = set()
    queue = deque([(start_y, start_x, 1)])

    while queue:
        y, x, dist = queue.popleft()
        if y == end_y and x == end_x:
            return dist

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    queue.append((ny, nx, dist + 1))

    return -1


N, M = map(int, input().split())

arr = [[0] * M for _ in range(N)]

for i in range(N):
    row = input()
    for j in range(len(row) - 1):
        arr[i][j] = int(row[j])

# print_arr(arr)

dist = shortest_length(0, 0, N - 1, M - 1, arr)
print(dist)

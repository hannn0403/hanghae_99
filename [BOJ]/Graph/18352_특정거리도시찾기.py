import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

adj_list = [[] for _ in range(1 + N)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)


queue = deque([(X, 0)])
visited[X] = True
city_list = []

while queue:
    city, dist = queue.popleft()
    if dist == K:
        city_list.append(city)

    for n_city in adj_list[city]:
        if not visited[n_city]:
            visited[n_city] = True
            queue.append((n_city, dist + 1))

if len(city_list) == 0:
    print(-1)
else:
    city_list.sort()
    for city in city_list:
        print(city)

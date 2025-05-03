import sys
from queue import PriorityQueue

input = sys.stdin.readline
INF = float("inf")

N = int(input())
M = int(input())

adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cost_arr = [INF] * (N + 1)

for _ in range(M):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))

start_city, end_city = map(int, input().split())

q = PriorityQueue()
q.put((0, start_city))
cost_arr[start_city] = 0

while q.qsize() > 0:
    city_cost, city_idx = q.get()
    if visited[city_idx]:
        continue
    visited[city_idx] = True

    for next_city_idx, bus_cost in adj_list[city_idx]:
        if cost_arr[next_city_idx] > cost_arr[city_idx] + bus_cost:
            cost_arr[next_city_idx] = cost_arr[city_idx] + bus_cost
            q.put((cost_arr[next_city_idx], next_city_idx))

print(cost_arr[end_city])

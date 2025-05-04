import sys

input = sys.stdin.readline
INF = float("inf")

N, M = map(int, input().split())

edge_list = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edge_list.append((a, b, c))

distance = [INF] * (N + 1)
distance[1] = 0


# (N-1) 번동안 돌면서 업데이트한다.
for i in range(N - 1):
    for a, b, c in edge_list:
        if distance[a] != INF and distance[b] > distance[a] + c:
            distance[b] = distance[a] + c

    # print(f"{i}번째 iteration : {distance}")

# 음수 사이클 체크
check_cycle = [distance[i] for i in range(len(distance))]

for a, b, c in edge_list:
    if check_cycle[a] != INF and check_cycle[b] > check_cycle[a] + c:
        check_cycle[b] = check_cycle[a] + c

isCycle = False
for i in range(len(distance)):
    if distance[i] != check_cycle[i]:
        isCycle = True
        break

if isCycle:
    print(-1)
else:
    for i in range(2, N + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])

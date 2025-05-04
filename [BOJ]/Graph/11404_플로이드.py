import sys

input = sys.stdin.readline
INF = float("inf")


def print_arr(arr):
    n, m = len(arr), len(arr[0])
    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j] == INF:
                print(0, end=" ")
            else:
                print(f"{arr[i][j]}", end=" ")
        print()


N = int(input())
M = int(input())

arr = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    arr[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    if arr[a][b] > c:
        arr[a][b] = c

# print("입력 받은후 초기화 상태")
# print_arr(arr)

for via in range(1, N + 1):
    for start in range(1, N + 1):
        for end in range(1, N + 1):
            arr[start][end] = min(arr[start][end], arr[start][via] + arr[via][end])

# print("플로이드 이후")
print_arr(arr)

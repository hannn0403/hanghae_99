import sys

input = sys.stdin.readline

n, m = map(int, input().split())

A = [[0] * (n + 1)]
D = [[0] * (n + 1) for _ in range(n + 1)]

# 이 for문을 
for i in range(n):
    A_row = [0] + list(map(int, input().split()))
    A.append(A_row)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i - 1][j] + D[i][j - 1] - D[i - 1][j - 1] + A[i][j]

for _ in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    result = D[y2][x2] - D[y1 - 1][x2] - D[y2][x1 - 1] + D[y1 - 1][x1 - 1]
    print(result)



# ===================================
# 4월 29일 문제 다시 푼 코드 

import sys

input = sys.stdin.readline


def print_arr(arr):
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            print(f"{arr[i][j]:<3}", end=" ")
        print()
    print()


N, M = map(int, input().split())

arr = [[0] * (N + 1) for _ in range(N + 1)]
sum_arr = [[0] * (N + 1) for _ in range(N + 1)]
# print("빈 Array")
# print_arr(arr)

for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        arr[i][j + 1] = row[j]

# print("값을 채운 Array")
# print_arr(arr)

# 여기부터
curr_col = 0
curr_row = 0
for i in range(1, N + 1):
    curr_row += arr[1][i]
    sum_arr[1][i] = curr_row

    curr_col += arr[i][1]
    sum_arr[i][1] = curr_col
# 여기까지는 굳이 안해줘도 괜찮은 부분이었다. (다만 밑의 2중 for문의 i, j 가 각각 2가 아닌 1부터 시작해야 함.)

# print("default 값만 넣은 sum arr")
# print_arr(sum_arr)

for i in range(2, N + 1):
    for j in range(2, N + 1):
        sum_arr[i][j] = (
            arr[i][j] + sum_arr[i - 1][j] + sum_arr[i][j - 1] - sum_arr[i - 1][j - 1]
        )

# print("전체 값 넣은 sum arr")
# print_arr(sum_arr)

for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    print(
        sum_arr[y2][x2]
        - sum_arr[y1 - 1][x2]
        - sum_arr[y2][x1 - 1]
        + sum_arr[y1 - 1][x1 - 1]
    )

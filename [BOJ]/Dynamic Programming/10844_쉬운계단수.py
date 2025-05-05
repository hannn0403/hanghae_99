import sys

input = sys.stdin.readline


def print_arr(arr):
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            print(f"{arr[i][j]:<3}", end=" ")
        print()
    print()


N = int(input())
if N == 1:
    print(9)
    exit()

mod = 1000000000

dp = [[0] * 10]
row = [0] + [1 for _ in range(9)]
dp.append(row)


for i in range(2, N + 1):
    row = []
    row.append(dp[i - 1][1])
    # row.append(dp[i - 1][2])
    for x in range(1, 9):
        row.append(dp[i - 1][x - 1] + dp[i - 1][x + 1])
    row.append(dp[i - 1][8])

    dp.append(row)

# print_arr(dp)
print(sum(dp[-1]) % mod)

import sys

input = sys.stdin.readline

N = int(input())
if N == 1 or N == 2:
    print(1)
    exit()

dp = [0] * (N + 1)
sum_arr = [0] * (N + 1)

dp[1] = 1
sum_arr[1] = 1
dp[2] = 1
sum_arr[2] = 2

for i in range(3, N + 1):
    dp[i] = sum_arr[i - 2] + 1
    sum_arr[i] = sum_arr[i - 1] + dp[i]

print(dp[-1])

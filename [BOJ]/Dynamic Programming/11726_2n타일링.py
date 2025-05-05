import sys

input = sys.stdin.readline

N = int(input())

if N <= 2:
    print(N)
    exit()

dp = [0] * (N + 1)
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[-1] % 10007)

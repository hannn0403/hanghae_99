import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

if N == 1:
    print(0)
    exit()


"""
dp = [0] * (N + 1)
dp[1] = 0

for i in range(2, N + 1):
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i // 3], dp[i // 2], dp[i - 1]) + 1
    elif i % 3 == 0 and i % 2 != 0:
        dp[i] = min(dp[i // 3], dp[i - 1]) + 1
    elif i % 3 != 0 and i % 2 == 0:
        dp[i] = min(dp[i // 2], dp[i - 1]) + 1
    else:
        dp[i] = dp[i - 1] + 1

print(dp[-1])
"""

top_down = [-1] * (N + 1)
top_down[1] = 0


def make_one(N):

    if top_down[N] != -1:
        return top_down[N]

    if (N % 3 == 0) and N % 2 == 0:
        top_down[N] = min(make_one(N // 3), make_one(N // 2)) + 1
    elif N % 3 == 0:
        top_down[N] = min(make_one(N // 3), make_one(N - 1)) + 1
    elif N % 2 == 0:
        top_down[N] = min(make_one(N // 2), make_one(N - 1)) + 1
    else:
        top_down[N] = make_one(N - 1) + 1

    return top_down[N]


print(make_one(N))

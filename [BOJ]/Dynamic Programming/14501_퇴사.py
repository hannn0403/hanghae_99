import sys

input = sys.stdin.readline

N = int(input())
T = [0]
P = [0]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 2)

for i in range(N, -1, -1):
    t, p = T[i], P[i]
    # 현재 해당 과제의 기간이 퇴사 전에 끝나지 않는다면 무용지물
    if i + T[i] > N + 1:
        dp[i] = dp[i + 1]
        continue

    dp[i] = max(dp[i + 1], p + dp[i + t])
    # print(dp)

print(dp[0])

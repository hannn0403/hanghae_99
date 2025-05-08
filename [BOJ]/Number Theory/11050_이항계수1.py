import sys

input = sys.stdin.readline

N, K = map(int, input().split())

upper = 1
for num in range(N, N - K, -1):
    upper *= num
# print(f"upper : {upper}")

lower = 1
for num in range(1, K + 1):
    lower *= num

# print(f"lower : {lower}")

print(upper // lower)

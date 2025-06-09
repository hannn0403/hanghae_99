import sys

input = sys.stdin.readline

N = int(input())
if N == 1:
    print(1)
    exit()

arr = [i for i in range(N+1)]

for k in range(2, N+1):
    if arr[k] == k:
        for j in range(k, N+1, k):
            arr[j] = arr[j] - arr[j] // k
        # print(f"index: {k} | arr : {arr}")
print(arr[-1])
# print(arr)
# ans = 0
# for i in range(1
#         , N+1):
#     if arr[i] == i:
#         ans += 1
# print(ans)


###########
import math
N = int(input())
result = N

for p in range(2, int(math.sqrt(N)) + 1):
    if N % p == 0:
        result -= result / p
        while N % p == 0:
            N /= p

if N > 1:
    result -= result / N
print(int(result))

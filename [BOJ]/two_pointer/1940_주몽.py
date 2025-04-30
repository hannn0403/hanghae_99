import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

arr = list(map(int, input().split()))

arr.sort()
# print(arr)
s = 0
e = len(arr) - 1

result = 0

while s < e:
    if arr[s] + arr[e] == M:
        result += 1
        s += 1
        e -= 1
    elif arr[s] + arr[e] < M:
        s += 1
    elif arr[s] + arr[e] > M:
        e -= 1

print(result)

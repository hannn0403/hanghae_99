import sys
import math

input = sys.stdin.readline

# 0. 입력 받기
A, B = map(int, input().split())

# 0-1. 예외 상황 처리
if B == 1:
    print(0)
    exit()

# 1. 먼저 소수를 구한다.
arr = [i for i in range(int(math.sqrt(B)) + 1)]
arr[0] = -1
arr[1] = -1

for i in range(2, int(math.sqrt(B)) + 1):
    if arr[i] == -1:
        continue

    for j in range(i + i, len(arr), i):
        arr[j] = -1


# 2. arr(소수들의 리스트)를 돌아가면서 거의 소수를 만들어내고 해당 범위 내에 있으면 ans 값 +1
ans = 0
for i in range(len(arr)):
    if arr[i] == -1:
        continue

    x = 2
    # while A <= i**x and i**x <= B:
    while i**x <= B:
        if A <= i**x:
            ans += 1
        x += 1


print(ans)

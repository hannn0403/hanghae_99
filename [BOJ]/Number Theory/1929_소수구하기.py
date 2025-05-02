import sys

input = sys.stdin.readline

M, N = map(int, input().split())

arr = [i for i in range(1, N + 1)]

idx = 0

while idx < len(arr):
    num = arr[idx]
    # 만약 수가 1이라면 지우고 넘어간다.
    # 이전에 이미 지워진 수라면 넘어간다.
    if num == 1 or num == -1:
        idx += 1
        continue

    else:
        if arr[idx] >= M:
            print(arr[idx])
        j = 1
        while idx + j * arr[idx] < len(arr):
            # print(
            #     f"arr[{idx} + {j} * {arr[idx]}] = {arr[idx + j * arr[idx]]}는 {arr[idx]}의 배수이므로 지운다."
            # )
            arr[idx + j * arr[idx]] = -1
            j += 1

    idx += 1

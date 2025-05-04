import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
# M : 수의 변경이 일어나는 횟수
# K : 구간의 합을 구하는 횟수

arr = []
for _ in range(N):
    arr.append(int(input()))

# print(f"arr : {arr}")

k = 0
while N > 2**k:
    k += 1

tree = [0] * (2 ** (k + 1))
for i in range(N):
    tree[2 ** (k) + i] = arr[i]
# print(f"tree : {tree}")

for i in range(2**k - 1):
    idx = 2**k - 1 - i
    tree[idx] = tree[2 * idx] + tree[2 * idx + 1]

# print(f"tree : {tree}")

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:  # b번째 수를 c로 변경
        curr_idx = 2**k - 1 + b
        prev_num = tree[curr_idx]
        diff = c - prev_num

        while curr_idx >= 1:
            tree[curr_idx] = tree[curr_idx] + diff
            # print(f"{curr_idx} 수정 : {tree}")
            curr_idx = curr_idx // 2

    elif a == 2:  # b번째 수부터 c번째 수까지의 합을 출력
        selected = []
        start_idx = 2**k - 1 + b
        end_idx = 2**k - 1 + c

        while start_idx <= end_idx:
            if start_idx % 2 == 1:
                selected.append(tree[start_idx])
                # print(f"selected : {selected}")
            if end_idx % 2 == 0:
                selected.append(tree[end_idx])
                # print(f"selected : {selected}")

            start_idx = (start_idx + 1) // 2
            end_idx = (end_idx - 1) // 2

        print(sum(selected))

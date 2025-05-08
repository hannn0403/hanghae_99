import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())


def get_sum(b, c, k):
    # 일단 b와 c를 seg_tree idx로 변경
    start_idx = 2**k - 1 + b
    end_idx = 2**k - 1 + c
    selected_list = []
    while start_idx <= end_idx:
        if start_idx % 2 == 1:
            selected_list.append(seg_tree[start_idx])
        if end_idx % 2 == 0:
            selected_list.append(seg_tree[end_idx])

        start_idx = (start_idx + 1) // 2
        end_idx = (end_idx - 1) // 2
    # print(f"get_sum의 마지막 list : {selected_list}")
    return sum(selected_list)


def change_value(b, c, k):
    # b번째 수를 c로 바꾼다.
    # b를 세그먼트 트리 인덱스로 변경
    b = 2**k - 1 + b
    diff = c - seg_tree[b]

    while b > 0:
        seg_tree[b] += diff
        if b == 1:
            break
        b = b // 2


arr = [0]
for _ in range(N):
    num = int(input())
    arr.append(num)

# k 구하기
k = 0
while 2**k < N:
    k += 1

# 세그먼트 트리 만들기
seg_tree = [0] * (2 ** (k + 1))
# 리프노드에 입력받은 리스트 넣기
for i in range(1, N + 1):
    seg_tree[2**k - 1 + i] = arr[i]

for i in range(2**k - 1, -1, -1):
    seg_tree[i] = seg_tree[i * 2] + seg_tree[i * 2 + 1]

# print(arr)
# print(seg_tree)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        change_value(b, c, k)
    elif a == 2:
        print(get_sum(b, c, k))

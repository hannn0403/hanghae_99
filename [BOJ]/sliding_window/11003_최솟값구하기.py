import sys
from collections import deque

input = sys.stdin.readline

# 값 입력 받기
N, L = map(int, input().split())

arr = list(map(int, input().split()))
queue = deque()

for i in range(len(arr)):
    curr_num = arr[i]

    # 만약 queue가 비어있다면 데이터를 일단 넣는다.
    if not queue:
        queue.append((curr_num, i))

    # queue가 비어있지 않다면,
    else:
        # 가장 뒤의 값과 삽입하려는 값의 value를 비교하고 삽입하려는 값이 작다면 가장 뒤의 값을 뺀다.
        # print(f"queue : {queue}")
        while queue and queue[-1][0] > curr_num:
            queue.pop()
        queue.append((curr_num, i))  # 데이터 삽입

    # queue의 첫 값과 방금 삽입한 데이터의 인덱스 값 비교 (L보다 크면 첫 값을 빼야 한다.)
    while queue[0][1] <= queue[-1][1] - L:
        queue.popleft()

    print(queue[0][0], end=" ")

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

ans_list = []
stack = deque()

for i in range(len(arr)):
    curr_index = len(arr) - 1  - i
    curr_val = arr[curr_index]

    # 만약 stack이 비어있다면 -1을 append하고, 해당 값을 넣는다.
    if not stack:
        ans_list.append(-1)
        stack.append(curr_val)
        continue

    # stack에 값이 존재하는데, curr_val보다 작은 것들은 전부 뺀다.
    while stack and stack[-1] <= curr_val:
        stack.pop()

    # 전부 빼다 보니까 stack이 비어진 경우는 ans_list에 -1을 넣고, stack에 해당 값을 넣는다.
    if not stack:
        ans_list.append(-1)
        stack.append(curr_val)
    else: # stack에 남아있는 경우는 stack의 가장 위에 값을 ans_list에 넣어주면 된다.
        ans_list.append(stack[-1])
        stack.append(curr_val)


# print(ans_list)
for i in range(len(ans_list)):
    print(ans_list[len(ans_list) - i - 1], end=' ')


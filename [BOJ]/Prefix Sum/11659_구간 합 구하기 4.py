import sys

input = sys.stdin.readline

N, M = map(int, input().split())


arr = [0] + list(map(int, input().split()))


sum_arr = [0]
curr_sum = 0
for i in range(1, N + 1):
    curr_sum += arr[i]
    sum_arr.append(curr_sum)

# print(f"Arr : {arr}")
# print(f"Sum Arr : {sum_arr}")


for _ in range(M):
    i, j = map(int, input().split())
    print(sum_arr[j] - sum_arr[i - 1])

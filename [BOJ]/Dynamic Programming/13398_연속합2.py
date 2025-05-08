import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

L = [0] * N
R = [0] * N

L[0] = arr[0]
R[-1] = arr[-1]

for i in range(1, N):
    L[i] = max(arr[i], arr[i] + L[i - 1])

for i in range(N - 2, -1, -1):
    R[i] = max(arr[i], arr[i] + R[i + 1])

# print(f"L : {L}")
# print(f"R : {R}")

l_max = max(L)
r_max = max(R)

one_num_out_max = float("-inf")

for i in range(1, N - 1):
    curr_num = L[i - 1] + R[i + 1]
    if one_num_out_max < curr_num:
        one_num_out_max = curr_num

print(max(l_max, r_max, one_num_out_max))

import sys

input = sys.stdin.readline

N = int(input())
if N == 1:
    print(1)
    exit()
elif N == 2:
    print(1)
    exit()

one = [0] * (N + 1)
zero = [0] * (N + 1)
one[1] = 1
zero[1] = 0
one[2] = 0
zero[2] = 1

for i in range(3, N + 1):
    one[i] = zero[i - 1]
    zero[i] = one[i - 1] + zero[i - 1]

print(one[-1] + zero[-1])

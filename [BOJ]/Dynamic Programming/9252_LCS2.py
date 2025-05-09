import sys

input = sys.stdin.readline


def print_arr(arr):
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            print(f"{arr[i][j]:<3}", end=" ")
        print()
    print()


A = input().rstrip()
B = input().rstrip()

dp = [[0] * len(B) for _ in range(len(A))]

# 0행과 0열에 대해서 초깃값을 설정해준다.
for i in range(len(A)):
    # if B[0] == A[i]:
    if B[0] in A[: i + 1]:
        dp[i][0] = 1

for i in range(len(B)):
    # if A[0] == B[i]:
    if A[0] in B[: i + 1]:
        dp[0][i] = 1

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# print_arr(dp)
print(dp[-1][-1])

lcs = ""
i = len(A) - 1
j = len(B) - 1

while i >= 0 and j >= 0:
    if dp[i][j] == 0:
        break

    if A[i] == B[j]:
        # print(f"i ({i}) 와 j ({j})가 {A[i]}로 같으므로 LCS : {A[i] + lcs}")
        lcs = A[i] + lcs
        i -= 1
        j -= 1
    else:
        if i == 0 and j > 0:
            j -= 1
        elif i > 0 and j == 0:
            i -= 1
        elif i > 0 and j > 0 and dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        elif i > 0 and j > 0 and dp[i - 1][j] < dp[i][j - 1]:
            j -= 1


print(lcs)

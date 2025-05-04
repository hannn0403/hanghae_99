import sys

input = sys.stdin.readline


def fact(a):
    if a <= 1:
        return 1
    ret = 1
    for i in range(1, a + 1):
        ret = ret * i
    return ret


def comb(a, b):
    return fact(a) // (fact(a - b) * fact(b))


N, M, K = map(int, input().split())

total_num = comb(N + M, N)
if total_num < K:
    print(-1)
    exit()


final_str = ""
while True:
    if N == 0 or M == 0:
        break

    # 현재 final_str에서 정해진 바로 그 뒤에 a가 들어오는 경우를 계산
    threshold = comb(N + M - 1, N - 1)

    if K <= threshold:
        final_str = final_str + "a"
        N -= 1
    else:
        final_str = final_str + "z"
        K -= threshold
        M -= 1


while N > 0:
    final_str = final_str + "a"
    N -= 1

while M > 0:
    final_str = final_str + "z"
    M -= 1

print(final_str)

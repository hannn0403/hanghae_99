import sys

input = sys.stdin.readline

S, P = map(int, input().split())
arr = input()
arr = arr[:-1]

A, C, G, T = map(int, input().split())

start = 0
end = P

pass_num = 0

if P == len(arr): 
    curr_a, curr_c, curr_g, curr_t = 0, 0, 0, 0
    for i in range(len(arr)):
        if arr[i] == "A":
            curr_a += 1
        elif arr[i] == "C":
            curr_c += 1
        elif arr[i] == "G":
            curr_g += 1
        elif arr[i] == "T":
            curr_t += 1
    if curr_a >= A and curr_c >= C and curr_g >= G and curr_t >= T:
        pass_num += 1

while end < len(arr):
    if start == 0:
        sub_str = arr[start:end]
        curr_a, curr_c, curr_g, curr_t = 0, 0, 0, 0
        for i in range(len(sub_str)):
            if sub_str[i] == "A":
                curr_a += 1
            elif sub_str[i] == "C":
                curr_c += 1
            elif sub_str[i] == "G":
                curr_g += 1
            elif sub_str[i] == "T":
                curr_t += 1
        if curr_a >= A and curr_c >= C and curr_g >= G and curr_t >= T:
            pass_num += 1

        start += 1
        continue

    else:
        if arr[start - 1] == "A":
            curr_a -= 1
        elif arr[start - 1] == "C":
            curr_c -= 1
        elif arr[start - 1] == "G":
            curr_g -= 1
        elif arr[start - 1] == "T":
            curr_t -= 1

        if arr[end] == "A":
            curr_a += 1
        elif arr[end] == "C":
            curr_c += 1
        elif arr[end] == "G":
            curr_g += 1
        elif arr[end] == "T":
            curr_t += 1

    if curr_a >= A and curr_c >= C and curr_g >= G and curr_t >= T:
        pass_num += 1

    start += 1
    end += 1

print(pass_num)


# 시간 초과 유의해야 한다. 
# 내가 놓쳤던 것은 input을 통해서 string을 입력 받으면 뒤에 개행문자가 딸려온다는 사실!

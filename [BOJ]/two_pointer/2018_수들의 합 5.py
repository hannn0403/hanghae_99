import sys

input = sys.stdin.readline

N = int(input())

start, end = 0, 0
curr = 0
result = 0

while end <= N:
    # print(f"start : {start} | end : {end} | curr : {curr}")
    if curr < N:
        end += 1
        curr += end
    elif curr == N:
        # print(f"{start}~{end}까지의 합이 {N}")
        result += 1
        end += 1
        curr += end
    elif curr > N:
        curr -= start
        start += 1

print(result)

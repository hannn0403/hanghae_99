import sys

input = sys.stdin.readline

N = int(input())

ans = 0

numbers = input().rstrip()

for i in range(len(numbers)):
    ans += int(numbers[i])

print(ans)

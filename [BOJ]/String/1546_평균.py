import sys

input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))

maximum = max(l)

for i in range(len(l)):
    l[i] = (l[i] / maximum) * 100

print(sum(l) / N)

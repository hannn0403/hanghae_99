import sys

input = sys.stdin.readline

N, M = map(int, input().split())


def find(a):
    if arr[a] == a:
        return arr[a]

    else:
        arr[a] = find(arr[a])
        return arr[a]


def union(a, b):
    real_a = find(a)
    real_b = find(b)
    arr[real_b] = real_a


arr = [i for i in range(N + 1)]

for _ in range(M):
    command, a, b = map(int, input().split())
    if command == 0:
        union(a, b)
    elif command == 1:
        real_a = find(a)
        real_b = find(b)
        if real_a == real_b:
            print("YES")
        else:
            print("NO")

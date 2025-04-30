import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
if len(arr) == 1:
    print(0)
    exit()


arr.sort()
good_num = 0


for i in range(len(arr)):
    num = arr[i]
    s = 0
    e = len(arr) - 1
    while s < e:
        if arr[s] + arr[e] == num:
            if s != i and e != i:
                # print(f"{num}은 {arr[s]}와 {arr[e]}의 합으로 나타내어지므로 좋은 수이다. ")
                good_num += 1
                break
            elif s == i:
                s += 1
            elif e == i:
                e -= 1

        elif arr[s] + arr[e] < num:
            s += 1
        elif arr[s] + arr[e] > num:
            e -= 1
print(good_num)

import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
# print(f"정렬된 배열 : {arr}")
M = int(input())
find_list = list(map(int, input().split()))


def BinarySearch(arr, X):
    s_idx = 0
    e_idx = len(arr) - 1

    find = False

    while s_idx <= e_idx:

        mid = (s_idx + e_idx) // 2
        # print(f"현재 상태: s_idx : {s_idx} | e_idx : {e_idx} | mid : {mid}")
        if arr[mid] == X:
            find = True
            break
        elif arr[mid] < X:
            # print(f"{arr[mid]}가 {X}보다 작다")
            s_idx = mid + 1
            # e_idx = mid - 1
        elif arr[mid] > X:
            # print(f"{arr[mid]}가 {X}보다 크다")
            # s_idx = mid + 1
            e_idx = mid - 1

    if find:
        return 1
    else:
        return 0


for X in find_list:
    print(BinarySearch(arr, X))

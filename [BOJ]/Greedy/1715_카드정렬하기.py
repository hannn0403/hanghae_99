import sys
import heapq

input = sys.stdin.readline

N = int(input())

file_list = []
for _ in range(N):
    file_list.append(int(input()))

heapq.heapify(file_list)

compare_num = 0

while len(file_list) > 1:
    one_small = heapq.heappop(file_list)
    two_small = heapq.heappop(file_list)

    # print(f"one_small : {one_small} | two_small : {two_small}")
    add_small = one_small + two_small
    compare_num += add_small

    heapq.heappush(file_list, add_small)


print(compare_num)

import heapq
import sys

input = sys.stdin.readline

N = int(input())
pos_list = []
neg_list = []

for _ in range(N):
    num = int(input())
    if num > 0:
        pos_list.append(-1 * num)
    else:
        neg_list.append(num)

heapq.heapify(pos_list)
heapq.heapify(neg_list)

total_sum = 0

while True:
    if len(pos_list) > 1:
        one_num = heapq.heappop(pos_list)
        two_num = heapq.heappop(pos_list)
        # print(f"pos_list : {one_num} * {two_num}")
        if one_num * two_num > -1 * one_num - two_num:
            total_sum += one_num * two_num
        else:
            total_sum -= one_num
            total_sum -= two_num
    if len(neg_list) > 1:
        one_num = heapq.heappop(neg_list)
        two_num = heapq.heappop(neg_list)
        if one_num * two_num > one_num + two_num:
            total_sum += one_num * two_num
        else:
            total_sum += one_num
            total_sum += two_num

    if len(pos_list) <= 1 and len(neg_list) <= 1:
        break


if len(pos_list) == 1:
    total_sum -= pos_list[0]
if len(neg_list) == 1:
    total_sum += neg_list[0]

print(total_sum)

import sys
import math

input = sys.stdin.readline

N = int(input())


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def DFS(num, N):
    if len(num) == N:
        print(num)
        return

    for add_num in rest_num_list:
        # num = num + add_num
        # print(f"num : {num + add_num}")
        if isPrime(int(num + add_num)):
            DFS(num + add_num, N)


first_num_list = ["2", "3", "5", "7"]
rest_num_list = ["1", "3", "5", "6", "7", "9"]

for first_num in first_num_list:
    DFS(first_num, N)

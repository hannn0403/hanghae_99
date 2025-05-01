import sys
from queue import PriorityQueue

input = sys.stdin.readline
N = int(input())
MyQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if MyQueue.empty():
            print(0)
        else:
            temp = MyQueue.get()
            print(temp[1])

    else:
        MyQueue.put((abs(request), request))

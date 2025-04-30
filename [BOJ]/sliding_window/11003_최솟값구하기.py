from collections import deque 
import sys 

input = sys.stdin.readline 

N, L = map(int, input().split()) 
mydeque = deque() 
now = list(map(int, input().split())) 

for i in range(N): 
    while mydeque and mydeque[-1][0] > now[i]: 
        mydeque.pop()
    mydeque.append((now[i], i)) 

    if mydeque[0][1] <= i - L: 
        mydeque.popleft() 
    print(mydeque[0][0], end=' ') 


# 시간 복잡도를 고려하여 deque을 사용해야 한다는 발상을 해야 한다. 

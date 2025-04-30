import sys

input = sys.stdin.readline

n = int(input())
ans = [0] * n 
A = list(map(int, input().split()))
myStack = [] 

for i in range(n): 

    while myStack and A[myStack[-1]] < A[i]: 
        ans[myStack.pop()] = A[i]
    myStack.append(i) 

while myStack: 
    ans[myStack.pop()] = -1 

for i in range(n): 
    print(ans[i], end=' ')


import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
myStack = [N - i for i in range(N)]
myStack = deque(myStack)

if N == 1: 
    print(myStack[0]) 
    exit()

# print(f"myStack :{myStack}")

while True:
    # 1. 제일 위에 있는 카드를 버린다.
    myStack.pop()

    # 종료 조건 : myStack에 남아있는 카드의 갯수가 1이면 while 문을 나온다.
    if len(myStack) == 1:
        break

    # 2. 제일 위에 있는 카드를 제일 밑으로 옮긴다.
    card = myStack.pop()
    myStack.appendleft(card)
    # print(f"myStack :{myStack}")


print(myStack[0])

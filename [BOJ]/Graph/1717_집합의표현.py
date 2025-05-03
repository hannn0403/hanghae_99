import sys 

input = sys.stdin.readline 

def find(a): 
    if arr[a] == a: 
        return a 
    else: 
        arr[a] = find(arr[a]) 
        return arr[a]


def union(a, b): 
    real_a = find(a)
    real_b = find(b)
    # arr[b] = real_a 
    arr[real_b] = real_a


n, m = map(int, input().split()) 

arr = [i for i in range(n+1)] 

for _ in range(m): 
    # print("\n\n===================")
    command, a, b = map(int, input().split()) 
    if command == 0: 
        union(a, b) 
        # print(f"union({a}, {b})이후 arr : {arr}")
    elif command == 1: 
        # print(f"find({a}), find({b}) 이전 arr : {arr}")
        real_a = find(a) 
        real_b = find(b) 
        # print(f"find({a}), find({b}) 이후 arr : {arr}")
        if real_a == real_b: 
            print('YES') 
        else: 
            print("NO") 

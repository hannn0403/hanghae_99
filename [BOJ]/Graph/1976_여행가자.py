import sys 

input= sys.stdin.readline 

def print_arr(arr): 
    n, m = len(arr), len(arr[0]) 
    for i in range(n): 
        for j in range(m): 
            print(f"{arr[i][j]:<3}", end=' ') 
        print()
    print() 

def find(a): 
    if union_find[a] == a: 
        return a 
    else: 
        union_find[a] = find(union_find[a]) 
        return union_find[a] 


def union(a, b): 
    real_a = find(a) 
    real_b = find(b) 
    union_find[real_b] = real_a


N = int(input()) 
M = int(input()) 
if M <= 1: 
    print("YES") 
    exit() 

union_find = [i for i in range(N+1)]

arr= [[0] * (N+1)] 
for _ in range(N):
    row = [0] + list(map(int, input().split())) 
    arr.append(row) 

# print_arr(arr) 
for i in range(1, N+1): 
    for j in range(1, i): 
        if arr[i][j] == 1: 
            union(i, j) 

route = list(map(int, input().split())) 
linked = find(route[0]) 
isLinked = True 

for i in range(1, len(route)): 
    if linked != find(route[i]): 
        isLinked = False
        break 

if isLinked: 
    print("YES") 
else: 
    print("NO") 

import sys 

input = sys.stdin.readline

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


N, M = map(int, input().split()) 
temp_list = list(map(int, input().split())) 
truth_num = temp_list[0] 

if truth_num == 0: 
    for _ in range(M): 
        temp = input() 
    print(M) 
    exit()

truth_list = [] 
for i in range(1, truth_num + 1): 
    truth_list.append(temp_list[i]) 

union_find = [i for i in range(N+1)] 

# 먼저 진실을 알고있는 사람들끼리 먼저 union 
for i in range(1, len(truth_list)): 
    union(truth_list[0], truth_list[i]) 

# 각 파티에 있는 사람들끼리 union 
party_arr = [] 
for _ in range(M): 
    temp_list = list(map(int, input().split())) 
    party_list = [temp_list[i] for i in range(1, temp_list[0] + 1)]
    party_arr.append(party_list) 
    for i in range(1, len(party_list)): 
        union(party_list[0], party_list[i])


truth_idx = find(truth_list[0]) 
answer = 0 
for i in range(M): 
    fun_party = True 
    for j in range(len(party_arr[i])): 
        if find(party_arr[i][j]) == truth_idx: 
            fun_party = False 
            break 
    if fun_party: 
        answer += 1

print(answer) 

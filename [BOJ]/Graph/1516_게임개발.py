import sys 
from collections import deque 

input = sys.stdin.readline 

N = int(input()) 
adj_list = [[] for _ in range(1 + N)] 
indegree = [0] * (N+1) 
building_time = [0] * (N+1) 
total_time = [0] * (N+1) 

for i in range(1, N+1): 
    l = list(map(int, input().split())) 
    building_time[i] = l[0]

    idx = 1 
    while l[idx] != -1: 
        adj_list[l[idx]].append(i)
        indegree[i] += 1 
        idx += 1

if N == 1: 
    print(building_time[1]) 
    exit()

queue = deque() 
for i in range(1, N+1): 
    if indegree[i] == 0: 
        queue.append(i) 

while queue: 
    building_idx = queue.popleft() 
    # 본인 건물이 올라가는 데 걸리는 시간
    total_time[building_idx] += building_time[building_idx]

    # 해당 건물이 지어져야 지을 수 있는 건물들에 대해서 해당 건물을 짓는 시간을 더하고, indegree를 1뺀다. 
    # indegree를 1 뺐을 때 0이 된다면 queue에 넣는다. 
    for next_building in adj_list[building_idx]: 
        # total_time[next_building] += building_time[building_idx]
        # total_time[next_building] += total_time[building_idx]
        total_time[next_building] = max(total_time[next_building], total_time[building_idx])
        indegree[next_building] -= 1 
        if indegree[next_building] == 0: 
            queue.append(next_building)

for i in range(1, len(total_time)): 
    print(total_time[i]) 

import sys 
from collections import deque 

input = sys.stdin.readline 

N, M = map(int, input().split()) 

arr = [[] for _ in range(N+1)] 
for _ in range(M): 
    a, b = map(int, input().split())
    arr[a].append(b) 

in_degree = [0] * (N+1)
visited = [False] * (N+1)
for i in range(1, N+1): 
    for j in range(len(arr[i])): 
        in_degree[arr[i][j]] += 1 

queue = deque() 
# indegree가 0인 것들을 먼저 queue에 넣는다. 
for i in range(1, N+1): 
    if in_degree[i] == 0: 
        visited[i] = True 
        queue.append(i) 

answer = [] 

while queue: 
    student = queue.popleft()
    answer.append(student) 
    # queue에서 뽑은 학생과 연관이 되어 있는 학생들의 리스트를 돈다. 
    for adj_stu in arr[student]: 
        # 해당 학생의 indegree를 1 감소시킨다. 
        in_degree[adj_stu] -= 1 
        # 1을 감소시켰을 때 indegree가 0일 때에는 queue에 넣는다. 
        if in_degree[adj_stu] == 0: 
            queue.append(adj_stu)

for a in answer: 
    print(a, end=' ') 


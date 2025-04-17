from collections import deque


def print_arr(arr):
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            print(f"{arr[i][j]:<3}", end=' ')
        print()
    print()


def shortest_dist_time_wall(start_y, start_x, end_y, end_x, time_wall, M):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1 ]

    visited = set([(start_y, start_x)])
    queue =deque([(start_y, start_x, 0)])

    while queue:
        y, x, dist = queue.popleft()
        if y == end_y and x == end_x:
            return dist

        for i in range(4):
            if y == M and 0 <= x < M and dy[i]==-1:
                ny, nx = x, M
            elif 0<= y < M and x == M and dx[i] == -1:
                ny, nx = M, y

            elif 0<= y < M and x == 2 * M -1 and dx[i] == 1:
                ny, nx = M, 3 * M - 1 - y
            elif y == M and 2 * M <= x < 3 * M and dy[i] == -1:
                ny, nx = 3 * M - 1 - x, 2 * M - 1

            elif y == 2 * M - 1 and 2*M <= x < 3 * M and dy[i] == 1:
                ny, nx =  x, 2 * M -1
            elif 2 * M <= y < 3 * M and x == 2 * M - 1 and dx[i] == 1:
                ny, nx = 2 * M - 1, y


            elif 2 * M <= y < 3 * M and x == M and dx[i] == -1:
                ny, nx = 2 * M - 1, 3 * M - 1 - y
            elif 2 * M - 1 == y and 0<= x < M and dy[i] == 1:
                ny, nx = 3 * M - 1 - x, M

            else:
                ny, nx = y + dy[i], x + dx[i]


            if 0<= ny < 3 * M and 0 <= nx < 3 *M :
                if time_wall[ny][nx] == 0 and (ny, nx) not in visited:
                    # print(f"(ny, nx) : ({ny}, {nx})")
                    visited.add((ny, nx))
                    queue.append((ny, nx, dist + 1))

    return -1


def shortest_dist_unknown_space(start_y, start_x, end_y, end_x, unknown_space, N, strange_pos, strange_direction, strange_term, first_stage_time):
    # 동 / 서 / 남 /북
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    visited = set([(start_y, start_x)])
    queue = deque([(start_y, start_x, first_stage_time, [(start_y, start_x)])])

    while queue:
        y, x, time, path = queue.popleft()

        if y == end_y and x == end_x:
            return time, path

        strange_set = set([])
        # 시간 이상 현상이 time에 따라 확산되는 것을 적용
        # 먼저 시간 이상 현상이 퍼지므로, time + 1 을 기준으로 해야 한다.
        for p in range(len(strange_pos)):
            # print("=======================================================")
            strange_set.add(strange_pos[p]) # 먼저 가장 첫번째
            # print(f"{p}번째 이상 현상 좌표 : {strange_pos[p]}")
            # print(f"{p}번째 이상 현상 좌표 이동 텀 : {strange_term[p]}")
            # print(f"{p}번째 이상 현상 좌표 이동 방향 : {dy[strange_direction[p]],dx[strange_direction[p]]}")
            # print(f"(time + 1) // strange_term[p] : {(time + 1) // strange_term[p]}")
            for q in range((time + 1) // strange_term[p]):
                strange_ny, strange_nx = strange_pos[p][0] + ((q+1) * dy[strange_direction[p]]), strange_pos[p][1] + ((q+1) * dx[strange_direction[p]])
                # print(f"strange_ny, strange_nx : {strange_ny, strange_nx}")
                if 0<= strange_ny < N and 0<= strange_nx < N:
                    # print(f"unknown_space[{strange_ny}][{strange_nx}] : {unknown_space[strange_ny][strange_nx]}")
                    if unknown_space[strange_ny][strange_nx] == 0:
                        strange_set.add((strange_ny, strange_nx))
                    else:
                        break
        # print(f"time : {time + 1} 때에 strange_set : {strange_set} | 현재 위치 : {(y, x)}")

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<= ny < N and 0<= nx < N:
                if unknown_space[ny][nx] == 4:
                    visited.add((ny, nx))
                    queue.append((ny, nx, time+1, path + [(ny, nx)]))
                if unknown_space[ny][nx] == 0 and (ny, nx) not in visited and (ny, nx) not in strange_set:
                    # print(f"ny, nx : {ny, nx}")
                    visited.add((ny, nx))
                    queue.append((ny, nx, time + 1, path + [(ny, nx)]))
    return -1, []








N, M, F = map(int, input().split())
# N : 미지의 공간 한 변의 길이
# M : 시간의 벽 한 변의 길이
# F 시간 이상 현상의 개수


# 미지의 공간 배열 입력 받기
unknown_space = []
for i in range(N):
    row = list(map(int, input().split()))
    unknown_space.append(row)


# print("미지의 공간")
# print_arr(unknown_space)



# 시간의 벽 입력 받기
east = []
for i in range(M):
    row = list(map(int, input().split()))
    east.append(row)
# 전개도에 넣기 위해서는 270도 회전시켜야 한다.
east = [x[::-1] for x in list(map(list, zip(*east[::-1])))[::-1]]

west = []
for i in range(M):
    row = list(map(int, input().split()))
    west.append(row)
# 전개도에 넣기 위해서는 90도 회전시켜야 한다.
west = list(map(list, zip(*west[::-1])))

south = []
for i in range(M):
    row = list(map(int, input().split()))
    south.append(row)

north = []
for i in range(M):
    row = list(map(int, input().split()))
    north.append(row)
# 전개도에 넣기 위해서는 180도 회전
north = [a[::-1] for a in north[::-1]]

upper = []
for i in range(M):
    row = list(map(int, input().split()))
    upper.append(row)

# 시간의 벽 전개도
time_wall = [[-1]* 3*M for _ in range(3 *M)]
for i in range(M):
    for j in range(M):
        time_wall[i][M + j] = north[i][j]
        time_wall[M + i][j]= west[i][j]
        time_wall[M+i][M+j] = upper[i][j]
        time_wall[M + i][2 * M + j] = east[i][j]
        time_wall[2 * M + i][M + j] = south[i][j]

# print("시간의 벽 전개도")
# print_arr(time_wall)


strange_pos = []
strange_direction = []
strange_term = []

# 동 / 서 / 남 /북
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
for _ in range(F):
    y, x, d, v = map(int, input().split())
    strange_pos.append((y, x))
    strange_direction.append(d)
    strange_term.append(v)

# 미지의 공간에서 탈출구 확인
entrance = (-1, -1)
final_exit = (-1, -1)

for y in range(N):
    for x in range(N):
        if unknown_space[y][x] == 4:
            final_exit = (y, x)
        if unknown_space[y][x] == 3:
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0<= ny < N and 0<= nx < N:
                    if unknown_space[ny][nx] == 0:
                        entrance = (ny, nx)

# print(f"미지의 공간 평면도와 시간의 벽이 맞닿아 있는 통로 : {entrance}")
# print(f"미지의 공간 평면도에서의 최종 출구 : {final_exit}")

# 시간의 벽에서 어디로 가야 하는 지 해당 좌표를 계산
# 시간의 벽 중심 좌표
time_wall_center = (-1, -1)
for i in range(N):
    for j in range(N):
        if unknown_space[i][j] == 3 and unknown_space[i+1][j] == 3 and unknown_space[i-1][j] == 3 and unknown_space[i][j+1] == 3 and unknown_space[i][j-1] == 3:
            time_wall_center = (i, j)

# print(f"time_wall_center : {time_wall_center}")
luy, lux = N + 1 , N + 1
for i in range(N):
    for j in range(N):
        if unknown_space[i][j] == 3:
            curr_y, curr_x = i,j
            if luy > i:
                luy = i
            if lux > j:
                lux = j


# luy, lux = time_wall_center[0] - M//2, time_wall_center[1] - M//2
# print(f"(luy, lux) : {luy, lux}")

time_wall_exit = (-1, -1)
# 아래에 통로가 위치한 경우
if 0<=entrance[0] -1<N and 0<= entrance[1] < N:
    if unknown_space[entrance[0]-1][entrance[1]] == 3:
        # time_wall_exit = (3*M-1, M + entrance[1] - time_wall_center[1] + 1)
        time_wall_exit = (3 * M - 1, M + entrance[1] - lux)

# 위에 통로가 위치한 경우
if 0<= entrance[0] + 1 < N and 0<= entrance[1] < N:
    if unknown_space[entrance[0]+1][entrance[1]] == 3:
        # time_wall_exit = (0, M + entrance[1] - time_wall_center[1] + 1)
        time_wall_exit = (0, M + entrance[1] - lux)


# 왼쪽에 통로가 위치한 경우
if 0<= entrance[0] < N and 0<= entrance[1] + 1 < N:
    if unknown_space[entrance[0]][entrance[1]+1] == 3:
        # print(f"(M + entrance[0] - time_wall_center[0] + 1, 0) : {(M + entrance[0] - time_wall_center[0] + 1, 0)}")
        # print(f"({M} + {entrance[0]} - {time_wall_center[0]} + 1, 0) : {(M + entrance[0] - time_wall_center[0] + 1, 0)}")
        # time_wall_exit = (M + entrance[0] - time_wall_center[0] + 1, 0)
        time_wall_exit = (M + entrance[0] - luy, 0)

# 오른쪽에 통로가 위치한 경우
if 0<= entrance[0] < N and 0<= entrance[1] - 1< N:
    if unknown_space[entrance[0]][entrance[1]-1] == 3:
        # time_wall_exit = (M + entrance[0] - time_wall_center[0] + 1, 3 * M - 1)
        time_wall_exit = (M + entrance[0] - luy, 3 * M - 1)




for i in range(M):
    for j in range(M):
        if time_wall[M + i][M+j] == 2:
            time_wall_entrance = (M + i, M + j)

first_stage_time = shortest_dist_time_wall(time_wall_entrance[0], time_wall_entrance[1], time_wall_exit[0], time_wall_exit[1], time_wall, M)
# print(f"시간의 벽 출발지 : {time_wall_entrance}")
# print(f"시간의 벽에서 탈출구 : {time_wall_exit}")
# print(f"Dist : {dist}")

# 만약 시간의 벽을 탈출하지 못한다면 바로 -1을 출력하고 끝
if first_stage_time == -1:
    # print("시간의 벽을 탈출하지 못함")
    print(-1)
    exit()
# 시간의 벽 탈출해서 평면도로 오는 시간
first_stage_time += 1
# print(f"first_stage_time : {first_stage_time}")


# 평면도의 시작점 (entrance)와 최종 도착지 (final_exit)으로 최단 경로를 찾아야 한다.
# 이 때, 시간 이상 현상이 되는 곳은 지날 수 없다.
# print(f"strange_pos : {strange_pos}")
# print(f"strange_direction : {strange_direction}")
# print(f"strange_term : {strange_term}")


final_answer, path  = shortest_dist_unknown_space(entrance[0], entrance[1], final_exit[0], final_exit[1], unknown_space, N, strange_pos, strange_direction, strange_term, first_stage_time)
# print(f"final_answer : {final_answer}")
# print(f"Path : {path}")
print(final_answer)

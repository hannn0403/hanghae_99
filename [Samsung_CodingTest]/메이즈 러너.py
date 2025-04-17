def print_arr(arr):
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            print(f"{arr[i][j]:<3}", end=' ')
        print()
    print()


# 거리 계산 함수
def cal_dist(start_y, start_x, end_y, end_x):
    return abs(start_y - end_y) + abs(start_x - end_x)


def user_movement(user_idx, user_list):
    global exit_y, exit_x, total_movement, maze
    n, m = len(maze), len(maze[0])
    start_y, start_x = user_list[user_idx]
    # 움직임의 우선순위에서 상/하를 우선시한다고 했다.
    # 여기에서는 순서를 y의 이동을 앞으로 배치하고
    # 조건이 맞으면 바로 return하는 방식으로 진행
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # 현재 출구와 참가자 간의 거리를 먼저 계산한다.
    curr_dist = cal_dist(start_y, start_x, exit_y, exit_x)

    for i in range(4):
        ny, nx = start_y + dy[i], start_x + dx[i]
        if 0<= ny < n and 0<= nx < m:
            if maze[ny][nx] == 0 and curr_dist > cal_dist(ny, nx, exit_y, exit_x):
                # print(f"{user_idx}번째 참가자 : {start_y, start_x} -> {ny, nx}")
                total_movement += 1
                user_list[user_idx] = (ny, nx)
                return
    return

def select_square(user_list):
    global exit_y, exit_x, maze
    min_len = len(maze) + 1
    min_y = len(maze)
    min_x = len(maze)

    for user_idx in range(len(user_list)):
        start_y, start_x = user_list[user_idx]
        # 정사각형 한 변의 길이 : max(가로 좌표의 절댓값 차, 세로 좌표의 절댓값 차)
        curr_len = max(abs(start_y - exit_y) + 1, abs(start_x - exit_x) + 1)
        # 정사각형의 좌상단 좌표
        curr_y = max(0, start_y - curr_len + 1, exit_y - curr_len + 1)
        curr_x = max(0, start_x - curr_len + 1, exit_x - curr_len + 1)

        if min_len > curr_len:
            min_len = curr_len
            min_y = curr_y
            min_x = curr_x
        elif min_len == curr_len:
            if min_y > curr_y:
                min_y = curr_y
                min_x = curr_x
            elif min_y == curr_y:
                if min_x > curr_x:
                    min_x = curr_x

    return min_y, min_x, min_len




def rotation_90(start_y, start_x, length):
    global maze, user_list, exit_y, exit_x
    n, m = len(maze), len(maze[0])
    new_arr = [[0] * m for _ in range(n)]
    # 미로 회전
    for y in range(start_y, start_y + length):
        for x in range(start_x, start_x + length):
            oy, ox = y - start_y, x - start_x
            ry, rx = ox, length - 1 - oy
            new_arr[ry + start_y][rx + start_x] = maze[y][x]

    for y in range(start_y, start_y + length):
        for x in range(start_x, start_x + length):
            maze[y][x] = new_arr[y][x]

    # 벽 내구도 1씩 깎음
    for y in range(start_y, start_y + length):
        for x in range(start_x, start_x + length):
            if maze[y][x] > 0:
                maze[y][x] = maze[y][x] - 1

    # 해당 칸에 있는 참가자들이 있다면 참가자들의 좌표 또한 수정
    for user_idx in range(len(user_list)):
        user_y, user_x = user_list[user_idx]
        if start_y <= user_y < start_y + length and start_x <= user_x < start_x + length:
            oy, ox = user_y - start_y, user_x - start_x
            ry, rx = ox, length - 1 - oy
            user_list[user_idx] = (ry + start_y, rx + start_x)

    # 출구도 항상 90도 회전이 적용된다.
    # print(f"회전 이전 출구 좌표 : {exit_y, exit_x}")
    oy, ox = exit_y - start_y, exit_x - start_x
    ry, rx = ox, length - 1 - oy
    exit_y, exit_x = (ry + start_y, rx + start_x)
    # print(f"회전 이후 출구 좌표 : {exit_y, exit_x}")


N, M, K = map(int, input().split())

# 미로 입력 받기
maze = []
for _ in range(N):
    row = list(map(int,input().split()))
    maze.append(row)

# 출구 좌표와 참가자 시작 좌표는 전부 1씩 뺀 값으로 저장
user_list = []
for _ in range(M):
    user_y, user_x = map(int, input().split())
    user_y -= 1
    user_x -= 1
    user_list.append((user_y, user_x))

exit_y, exit_x = map(int, input().split())
exit_y -= 1
exit_x -= 1

# 최종 출력 값인 참가자 이동 거리의 합
total_movement = 0

# print_arr(maze)
# print(f"출구 좌표 : {exit_y, exit_x}")
# print(f"참가자 좌표 : {user_list}")


# K 초 동안 참가자들과 미로의 회전이 반복된다.
for t in range(K):
    # print(f"==============={t}===============")
    # print_arr(maze)
    # 먼저 참가자들이 모두 1칸씩 움직인다.
    for user_idx in range(len(user_list)):
        # print(f"{user_idx}번째 참가자 이동 시도")
        user_y, user_x = user_list[user_idx]
        user_movement(user_idx, user_list)
        # print(f"참가자 좌표 : {user_list}")

    # 출구에 도달한 참가자는 삭제한다.
    new_user_list = []
    for user_idx in range(len(user_list)):
        user_y, user_x = user_list[user_idx]
        if (user_y, user_x) == (exit_y, exit_x):
            continue
        new_user_list.append((user_y, user_x))

    user_list = new_user_list
    # 더이상 미로에 있는 참가자가 없다면 break
    if len(user_list) == 0:
        break

    # 회전할 정사각형을 찾는다 .
    start_y, start_x, length = select_square(user_list)
    # print(f"회전할 정사각형 좌상단 : {start_y, start_x} | 길이 : {length}")

    # 정사각형 회전 | 회전한 벽 내구도 1깎음 | 사용자 좌표 회전 반영
    rotation_90(start_y, start_x, length)
    # print("회전한 이후 maze")
    # print_arr(maze)
    # print(f"회전 이후 user_list : {user_list}")







print(total_movement)
print(exit_y + 1, exit_x + 1) # 출구의 좌표를 입력 받을 때 1씩 뺐으므로, 여기에서는 1씩 더해서 출력해야 한다.

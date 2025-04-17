from collections import deque

def print_arr(arr):
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            print(f"{arr[i][j]:<3}", end=' ')
        print()
    print()

def shortest_path(start_y, start_x, end_y, end_x, graph):
    n, m = len(graph), len(graph[0])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = set([(start_y, start_x)])
    queue = deque([(start_y, start_x, [(start_y, start_x)])])

    while queue:
        y, x, path = queue.popleft()
        if y == end_y and x == end_x:
            return path

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<= ny < n and 0<= nx < m:
                if graph[ny][nx] == 0 and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    queue.append((ny, nx, path + [(ny, nx)]))
    return []

def check_upper(curr_y, curr_x, warrior_list, N):
    # 가상의 지도를 만듦
    virtual = [[0] * N for _ in range(N)]
    virtual[curr_y][curr_x] = -1
    # print("메두사만 위치")
    # print_arr(virtual)

    # 시야각 범위 내 영역을 1로 입력
    for i in range(1, curr_y+1):
        for j in range(curr_x - i, curr_x + i + 1):
            if 0<= curr_y - i < N and 0<= j < N:
                virtual[curr_y - i][j] = 1
    # print("메두사 시야각 (위쪽)")
    # print_arr(virtual)

    warrior_set = set(warrior_list)

    # 전사들의 위치를 돌아가면서 시야각 내에 있는 지 확인 -> 시야각 내에 있다면 전사의 위치는 그대로 두고, 뒤의 부분을 다시 0으로 만듦
    for w_idx in range(len(warrior_list)):
        wy, wx = warrior_list[w_idx]
        # 해당 전사가 시야각에 없는 경우
        if virtual[wy][wx] != 1:
            continue
        # 해당 전사가 시야각에 있는 경우
        # Case 1. 바로 위에 있는 경우 (wx == curr_y)
        if wx == curr_x:
            for i in range(wy):
                virtual[i][wx] = 0
        # Case 2. 왼쪽 위 대각선에 있는 경우
        elif wx < curr_x:
            for i in range(1, wy + 1):
                for j in range(wx - i, wx+1):
                    if 0<= wy -i < N and 0<= j < N:
                        virtual[wy-i][j] = 0
        # Case 3. 오른쪽 위 대각선에 있는 경우
        elif wx > curr_x:
            for i in range(1, wy + 1):
                for j in range(wx, wx + i + 1):
                    if 0<= wy - i < N and 0<= j < N:
                        virtual[wy-i][j] = 0

    upper_set = set([])
    # 최종적으로 1의 값을 가지는 부분에 전사들이 몇명이 있는지 확인
    for i in range(N):
        for j in range(N):
            if virtual[i][j] == 1 and (i, j) in warrior_set:
                upper_set.add((i, j))
    # print(f"위쪽 시야각 set : {upper_set}")
    upper_num = 0
    for w_idx in range(len(warrior_list)):
        wy, wx = warrior_list[w_idx]
        if (wy, wx) in upper_set:
            upper_num += 1


    return upper_set, virtual, upper_num

def check_down(curr_y, curr_x, warrior_list, N):
    # 가상의 지도를 만듦
    virtual = [[0] * N for _ in range(N)]
    virtual[curr_y][curr_x] = -1
    # print("메두사만 위치")
    # print_arr(virtual)

    # 시야각 범위 내 영역을 1로 입력
    for i in range(1, N - curr_y):
        for j in range(curr_x - i, curr_x + i + 1):
            if 0 <= curr_y + i < N and 0 <= j < N:
                virtual[curr_y + i][j] = 1
    # print("메두사 시야각 (아래쪽)")
    # print_arr(virtual)

    warrior_set = set(warrior_list)
    # 전사들의 위치를 돌아가면서 시야각 내에 있는 지 확인 -> 시야각 내에 있다면 전사의 위치는 그대로 두고, 뒤의 부분을 다시 0으로 만듦
    for w_idx in range(len(warrior_list)):
        wy, wx = warrior_list[w_idx]
        # 해당 전사가 시야각에 없는 경우
        if virtual[wy][wx] != 1:
            continue
        # 해당 전사가 시야각에 있는 경우
        # Case 1. 바로 아래에 있는 경우 (wx == curr_y)
        if wx == curr_x:
            for i in range(wy+1, N):
                virtual[i][wx] = 0
        # Case 2. 왼쪽 아래 대각선에 있는 경우
        elif wx < curr_x:
            for i in range(1, N):
                for j in range(wx - i, wx + 1):
                    if 0 <= wy + i < N and 0 <= j < N:
                        virtual[wy + i][j] = 0
        # Case 3. 오른쪽 아래 대각선에 있는 경우
        elif wx > curr_x:
            for i in range(1, N):
                for j in range(wx, wx + i + 1):
                    if 0 <= wy + i < N and 0 <= j < N:
                        virtual[wy + i][j] = 0

    down_set = set([])
    # 최종적으로 1의 값을 가지는 부분에 전사들이 몇명이 있는지 확인
    for i in range(N):
        for j in range(N):
            if virtual[i][j] == 1 and (i, j) in warrior_set:
                down_set.add((i, j))
   #  print(f"아래쪽 시야각 set : {down_set}")
    down_num = 0
    for w_idx in range(len(warrior_list)):
        wy, wx = warrior_list[w_idx]
        if (wy, wx) in down_set:
            down_num += 1

    return down_set, virtual, down_num

def check_left(curr_y, curr_x, warrior_list, N):
    # 가상의 지도를 만듦
    virtual = [[0] * N for _ in range(N)]
    virtual[curr_y][curr_x] = -1
    # print("메두사만 위치")
    # print_arr(virtual)

    # 시야각 범위 내 영역을 1로 입력
    for j in range(1, curr_x + 1):
        for i in range(curr_y - j, curr_y + j + 1):
            if 0 <= i < N and 0 <= curr_x - j < N:
                virtual[i][curr_x - j] = 1
    # print("메두사 시야각 (왼쪽)")
    # print_arr(virtual)

    warrior_set = set(warrior_list)
    # 전사들의 위치를 돌아가면서 시야각 내에 있는 지 확인 -> 시야각 내에 있다면 전사의 위치는 그대로 두고, 뒤의 부분을 다시 0으로 만듦
    for w_idx in range(len(warrior_list)):
        wy, wx = warrior_list[w_idx]
        # 해당 전사가 시야각에 없는 경우
        if virtual[wy][wx] != 1:
            continue

        # 해당 전사가 시야각에 있는 경우
        # Case 1. 바로 왼쪽에 있는 경우 (wy == curr_y)
        if wy == curr_y:
            for j in range(0, wx):
                virtual[wy][j] = 0

        # Case 2. 왼쪽 위 대각선에 있는 경우
        elif wy < curr_y:
            for j in range(1, wx + 1):
                for i in range(wy - j, wy+1):
                    if 0 <= wx - j < N and 0 <= i < N:
                        virtual[i][wx - j] = 0
        # Case 3. 왼쪽 아래 대각선에 있는 경우
        elif wy > curr_y:
            for j in range(1, wx+1):
                for i in range(wy, wy + j + 1):
                    if 0<= wx - j < N and 0<= i < N:
                        virtual[i][wx - j] = 0

    # print("최종 왼쪽 시야각")
    # print_arr(virtual)

    left_set = set([])
    # 최종적으로 1의 값을 가지는 부분에 전사들이 몇명이 있는지 확인
    for i in range(N):
        for j in range(N):
            if virtual[i][j] == 1 and (i, j) in warrior_set:
                left_set.add((i, j))
    # print(f"왼쪽 시야각 set : {left_set}")

    left_num = 0
    for w_idx in range(len(warrior_list)):
        wy, wx = warrior_list[w_idx]
        if (wy, wx) in left_set:
            left_num += 1

    return left_set, virtual, left_num

def check_right(curr_y, curr_x, warrior_list, N):
    # 가상의 지도를 만듦
    virtual = [[0] * N for _ in range(N)]
    virtual[curr_y][curr_x] = -1
    # print("메두사만 위치")
    # print_arr(virtual)

    # 시야각 범위 내 영역을 1로 입력
    for j in range(1, N):
        for i in range(curr_y - j, curr_y + j + 1):
            if 0 <= i < N and 0 <= curr_x + j < N:
                virtual[i][curr_x + j] = 1
    # print("메두사 시야각 (오른쪽)")
    # print_arr(virtual)

    warrior_set = set(warrior_list)
    # 전사들의 위치를 돌아가면서 시야각 내에 있는 지 확인 -> 시야각 내에 있다면 전사의 위치는 그대로 두고, 뒤의 부분을 다시 0으로 만듦
    for w_idx in range(len(warrior_list)):
        wy, wx = warrior_list[w_idx]
        # 해당 전사가 시야각에 없는 경우
        if virtual[wy][wx] != 1:
            continue

        # 해당 전사가 시야각에 있는 경우
        # Case 1. 바로 오른쪽에 있는 경우 (wy == curr_y)
        if wy == curr_y:
            for j in range(wx+1, N):
                virtual[wy][j] = 0
        # Case 2. 오른쪽 위 대각선에 있는 경우
        elif wy < curr_y:
            for j in range(1, N):
                for i in range(wy - j, wy+1):
                    if 0 <= wx + j < N and 0 <= i < N:
                        virtual[i][wx + j] = 0

        # Case 3. 오른쪽 아래 대각선에 있는 경우
        elif wy > curr_y:
            for j in range(1, N):
                for i in range(wy, wy + j + 1):
                    if 0 <= wx + j < N and 0 <= i < N:
                        virtual[i][wx + j] = 0
    # print("최종 오른쪽 시야각")
    # print_arr(virtual)

    right_set = set([])
    # 최종적으로 1의 값을 가지는 부분에 전사들이 몇명이 있는지 확인
    for i in range(N):
        for j in range(N):
            if virtual[i][j] == 1 and (i, j) in warrior_set:
                right_set.add((i, j))
    # print(f"오른쪽 시야각 set : {right_set}")

    right_num = 0
    for w_idx in range(len(warrior_list)):
        wy, wx = warrior_list[w_idx]
        if (wy, wx) in right_set:
            right_num += 1

    return right_set, virtual, right_num

def get_best_sight(curr_y, curr_x, warrior_list, N):
    # 상/하/좌/우의 우선순위를 가진다.
    upper_set, upper_map, upper_num = check_upper(curr_y, curr_x, warrior_list, N)
    down_set, down_map, down_num = check_down(curr_y, curr_x, warrior_list, N)
    left_set, left_map, left_num = check_left(curr_y, curr_x, warrior_list, N)
    right_set, right_map, right_num = check_right(curr_y, curr_x, warrior_list, N)
    # print(f"upper_set : {upper_set} | {len(upper_set)}")
    # print(f"down_set : {down_set} | {len(down_set)}")
    # print(f"left_set : {left_set} | {len(left_set)}")
    # (f"right_set : {right_set} | {len(right_set)}")

    # 먼저 default 값을 upper로 설정
    best_set = upper_set
    best_map = upper_map
    best_num = upper_num
    if best_num < down_num:
        best_set = down_set
        best_map = down_map
        best_num = down_num
    if best_num < left_num:
        best_set = left_set
        best_map = left_map
        best_num = left_num
    if best_num < right_num:
        best_set = right_set
        best_map = right_map
        best_num = right_num

    return best_set, best_map, best_num



# 1. 정보 입력 받기
N, M = map(int, input().split())
# 메두사 위치 : (my, mx) | 공원 위치 : (py, px)
my, mx, py, px = map(int, input().split())
# 전사들의 좌표
warrior_list = []
warrior_info = list(map(int, input().split()))
for i in range(len(warrior_info) // 2):
    warrior_list.append((warrior_info[2 * i], warrior_info[2 * i+1]))
# print("전사들의 초기 위치 리스트")
# print(warrior_list)


# 마을의 도로 정보
village = []
for i in range(N):
    row = list(map(int, input().split()))
    village.append(row)

# print("Village")
# print_arr(village)


# 2. 메두사의 집 - 공원까지 경로 구하기
# 상/하/좌/우의 순
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

path = shortest_path(my, mx, py, px, village)
# 예외 처리 : 집- 공원까지의 경로가 존재하지 않는 경우
if len(path) == 0:
    print(-1)
    exit()

# print(f"path : {path}")
# 3. 메두사와 전사들의 이동 - 메두사의 경로를 따라서 for문을 돌며 그에 따라 메두사의 시야나 전사들의 이동을 구현
for t in range(1, len(path)): # path가 시작점과 끝점을 모두 포함하고 있으므로, 시작점은 굳이 포함할 필요가 없다.

    # 3-0. 메두사가 공원에 도착한 경우 -> 0을 출력하고 끝
    if t == len(path) - 1:
        print(0)
        break

    # 3-1. 메두사의 이동
    # 메두사의 현재 위치
    curr_y, curr_x = path[t]
    # 메두사가 이동한 칸에 전사가 있을 경우 전사는 사라진다.
    new_warrior_list = []
    for wy, wx in warrior_list:
        if wy == curr_y and wx == curr_x:
            continue
        else:
            new_warrior_list.append((wy, wx))
    warrior_list = new_warrior_list

    # print(f"현재 warrior의 위치들 : {warrior_list}")

    # 3-2. 메두사의 시선
    # check_upper(curr_y, curr_x, warrior_list, N)
    # check_down(curr_y, curr_x, warrior_list, N)
    # check_left(curr_y, curr_x, warrior_list, N)
    stone, sight_map, stone_warrior_num = get_best_sight(curr_y, curr_x, warrior_list, N) # 돌로 변한 전사들의 좌표를 저장할 set
    # print(f"stone set : {stone}")
    # print("Sight Map")
    # print_arr(sight_map)

    # set 자료형은 중복이 count되지 않으므로, 다시 세줘야 한다.
    # stone_warrior_num = 0
    # for w_idx in range(len(warrior_list)):
    #     wy, wx = warrior_list[w_idx]
    #     if (wy, wx) in stone:
    #         stone_warrior_num += 1


    # 3-3. 전사들의 이동
    # 돌로 변한 전사인지 확인
    delete_index_set = set([]) # 삭제할 전사들의 인덱스
    # 전사들의 해당 stage에서 총 움직인 거리를 저장할 변수
    total_movement = 0
    # 메두사를 공격한 전사의 수를 저장할 변수
    attack_warrior = 0
    for w_idx in range(len(warrior_list)):
        wy, wx = warrior_list[w_idx]
        # print("==================")
        # print(f"움직이는 전사 : {wy, wx}")
        # 돌로 변한 전사라면 움직이지 않고 Pass
        if (wy, wx) in stone:
            # print("시야각 안에 들어 돌이됨 - 움직일 수 없음")
            continue

        # 돌로 변하지 않은 전사라면

        # 첫번째 이동 (상/하/좌/우의 우선순위로 이동)
        if curr_y < wy and sight_map[wy-1][wx] != 1: # 메두사의 현재 위치보다 전사가 아래에 있는 경우 -> 위로 한칸
            wy -= 1
            total_movement += 1
            warrior_list[w_idx] = (wy, wx)
            # print(f"total_movement 1 추가 : {wy, wx}")
        elif curr_y > wy and sight_map[wy+1][wx] != 1: # 메두사의 현재 위치보다 전사가 위에 있는 경우 -> 아래로 한칸
            wy += 1
            total_movement += 1
            warrior_list[w_idx] = (wy, wx)
            # print(f"total_movement 1 추가 : {wy, wx}")
        elif curr_x < wx and sight_map[wy][wx-1] != 1: # 메두사의 현재 위치보다 전사가 오른쪽에 있는 경우 -> 좌로 한칸
            wx -= 1
            total_movement += 1
            warrior_list[w_idx] = (wy, wx)
            # print(f"total_movement 1 추가 : {wy, wx}")
        elif curr_x > wx and sight_map[wy][wx+1] != 1: # 메두사의 현재 위치보다 전사가 왼쪽에 있는 경우 -> 우로 한칸
            wx += 1
            total_movement += 1
            warrior_list[w_idx] = (wy, wx)
            # print(f"total_movement 1 추가 : {wy, wx}")
        else:
            continue # 아무데도 움직일 수 없는 경우 continue를 통해서 두 번째 움직임 생략


        # 첫 번째 이동 후 메두사의 위치와 동일해진다면 -> 메두사 공격한 이후 사라진다. : 삭제 리스트에 추가 후 continue
        if wy == curr_y and wx == curr_x:
            delete_index_set.add(w_idx)
            attack_warrior += 1
            continue

        # 두 번째 이동 (좌/우/상/하의 우선순위로 이동)
        if curr_x < wx and sight_map[wy][wx-1] != 1:
            wx -= 1
            total_movement += 1
            warrior_list[w_idx] = (wy, wx)
            # print(f"total_movement 1 추가 : {wy, wx}")
        elif curr_x > wx and sight_map[wy][wx+1] != 1:
            wx += 1
            total_movement += 1
            warrior_list[w_idx] = (wy, wx)
            # print(f"total_movement 1 추가 : {wy, wx}")
        elif curr_y < wy and sight_map[wy-1][wx] != 1:
            wy -= 1
            total_movement += 1
            warrior_list[w_idx] = (wy, wx)
            # print(f"total_movement 1 추가 : {wy, wx}")
        elif curr_y > wy and sight_map[wy+1][wx] != 1:
            wy += 1
            total_movement += 1
            warrior_list[w_idx] = (wy, wx)
            # print(f"total_movement 1 추가 : {wy, wx}")
        else:
            continue  # 아무데도 움직일 수 없는 경우 continue를 통해서 두 번째 움직임 생략

        # 두 번째 이동 후 메두사의 위치와 동일해진다면 -> 사라진다. : 삭제 리스트에 추가 후 continue
        if wy == curr_y and wx == curr_x:
            delete_index_set.add(w_idx)
            attack_warrior += 1
            continue

        # 메두사를 만나지 않았다면 warrior_list에 업데이트 된 위치를 삽입
        warrior_list[w_idx] = (wy, wx)

    # 사라진 전사들에 대한 정보를 반영하여 warrior_list
    new_warrior_list = []
    for w_idx in range(len(warrior_list)):
        if w_idx not in delete_index_set:
            new_warrior_list.append(warrior_list[w_idx])
    warrior_list = new_warrior_list




    # 현재 stage마다 (모든 전사가 이동한 거리의 합) / (메두사로 인해 돌이 된 전사 수) / (메두사를 공격한 전사의 수) 출력
    print(total_movement, end=' ')# 모든 전사가 이동한 거리의 합
    # print(len(stone), end=' ')  # 메두사로 인해 돌이 된 전사 수
    print(stone_warrior_num, end=' ')  # 메두사로 인해 돌이 된 전사 수
    print(attack_warrior) # 메두사를 공격한 전사의 수



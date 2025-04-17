from collections import deque

def print_arr(arr):
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            print(f"{arr[i][j]:<3}", end=' ' )
        print()
    print()


def is_range(y, x, arr):
    global N
    return 1 <= y <= N and 1 <= x <= N

def distance(start_y, start_x, end_y, end_x):
    return (start_y - end_y)**2 + (start_x - end_x)**2

def find_nearest_santa_idx(ry, rx, santa_pos):
    global is_alive

    shortest_distance = 50000
    nearest_idx= -1

    # 일단 모든 산타를 iteration
    for santa_idx in range(len(santa_pos)):
        # 탈락하지 않은 산타에 대해서만 고려
        if is_alive[santa_idx]:
            sy, sx = santa_pos[santa_idx]
            curr_distance = distance(ry, rx, sy, sx)

            # 최소값 갱신이 되는 경우
            if shortest_distance > curr_distance:
                shortest_distance = curr_distance
                nearest_idx = santa_idx

            # 최소값이 같은 경우 (행이 더 큰것 -> 열이 더 큰 것)
            if shortest_distance == curr_distance:
                ny, nx = santa_pos[nearest_idx]
                # 행 먼저 비교
                if ny < sy : # 새로운 게 행이 더 크면 업데이트
                    nearest_idx = santa_idx
                elif ny == sy and nx < sx : # 행이 동일할 때 열이 더 크면 업데이트
                    nearest_idx = santa_idx

    return nearest_idx # 가장 가까운 산타의 인덱스를 반환

def find_rudolf_movement(ry, rx, santa_pos):
    nearest_santa_idx = find_nearest_santa_idx(ry, rx, santa_pos)
    sy, sx = santa_pos[nearest_santa_idx]

    # 움직이는 방향의 y, x좌표
    my, mx = 0, 0
    if ry > sy:
        my = -1
    elif ry < sy :
        my = 1

    if rx > sx :
        mx = -1
    elif rx < sx :
        mx = 1

    return my, mx


def find_santa_movement(ry, rx, santa_idx):
    # print(f"루돌프 좌표 : {ry}, {rx}")
    # 여기에서는 루돌프와 다르게 다른 산타에 대해서도 고려해야 한다.
    global santa_pos, arr
    sy, sx = santa_pos[santa_idx]
    # print(f"find_santa_movement 내에서 {santa_idx} 산타의 좌표 : {sy}, {sx}")
    min_distance = distance(ry, rx, sy, sx) # 최소 거리 초기화는 현재 거리
    # print(f"현재 루돌프와의 거리 : {min_distance}")
    my, mx = 0,0


    # 상 > 우 > 하 > 좌 의 순서대로 고려하여, 거리 값이 동일한 경우에는 그냥 넘어간다.
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    for i in range(4):
        ny, nx = sy + dy[i], sx + dx[i]
        # print(f"ny : {ny} / nx : {nx}")
        # 움직이려고 하는 것이 게임판 밖이거나 다른 산타가 있는 경우
        if not is_range(ny, nx, arr):
            # print(f"Out of range : {ny}, {nx}")
            continue

        elif arr[ny][nx] > 0:
            # print(f"{ny}, {nx} 에 다른({arr[ny][nx]}) 산타가 있음")
            continue

        curr_distance = distance(ry, rx, ny, nx)
        # print(f"({ny}, {nx})로 이동했을 때 루돌프와의 거리 : {curr_distance}")
        if curr_distance < min_distance:
            min_distance = curr_distance
            my, mx = dy[i], dx[i]

    return my, mx


def domino(idx, my, mx, gy, gx):
    global santa_pos, arr
    cy, cx = santa_pos[idx]
    # print_arr(arr)
    # 종료 조건
    # 움직인 칸이 게임판 밖인 경우
    if not is_range(gy, gx, arr):
        is_alive[idx] = False
        arr[cy][cx] = 0
        return
    # 움직인 칸이 빈칸인 경우
    elif arr[gy][gx] == 0 or arr[gy][gx] == idx:
        arr[cy][cx] = 0
        arr[gy][gx] = idx
        santa_pos[idx] = (gy, gx)
        return

    next_idx = arr[gy][gx]
    domino(next_idx, my, mx, gy + my, gx + mx)
    arr[gy][gx] = idx
    arr[cy][cx] = 0
    santa_pos[idx] = (gy, gx)


def rudolf_collision(ry, rx, my, mx, m):
    global arr, santa_score, stun, is_alive, C

    # 충돌하는 산타의 인덱스
    santa_idx = arr[ry + my][rx + mx]
    # 산타가 C 점을 획득
    santa_score[santa_idx] += C
    # 산타는 스턴을 먹는다.
    stun[santa_idx] = m + 2

    domino(santa_idx, my, mx, ry + my + C * my, rx + mx + C * mx)

    # 연쇄 이동이 모두 일어난 이후 루돌프 위치 변경
    arr[ry][rx] = 0
    arr[ry + my][rx+mx] = -1


def santa_collision(ry, rx, my, mx, santa_idx, m):
    global arr, santa_score, stun, D

    # 산타가 D 점을 획득
    santa_score[santa_idx] += D
    # 산타는 스턴을 먹는다.
    stun[santa_idx] = m + 2

    domino(santa_idx, -my, -mx, ry - D * my, rx - D * mx)




N, M, P, C, D = map(int, input().split())
# N : 게임판 크기
# M : 게임 턴 수
# P : 산타의 수
# C : 루돌프의 힘
# D : 산타의 힘

# 게임판 만들기
arr = [[0] * (N + 1) for _ in range(N+1)]

stun = [0] * (P + 1) # 충돌시 스턴 풀리는 stage에 대해서 저장
santa_pos = [(0,0)] * (P+1) # 각 산타의 위치에 대해서 저장
santa_score = [0] * (P + 1)
is_alive = [False] * (P + 1)

# 루돌프 위치 입력 받기
ry, rx = map(int, input().split())
arr[ry][rx] = -1 # 루돌프의 위치는 array에서 -1로 저장

# 산타 인덱스를 통해서 산타 위치 입력 받기
for _ in range(P):
    santa_idx, sy, sx = map(int, input().split())
    santa_pos[santa_idx] = (sy, sx)
    arr[sy][sx] = santa_idx
    is_alive[santa_idx] = True



for m in range(1, M+1):
    # print(f"=========={m}==========")
    # print("m번째 턴의 초기 상태")
    # print_arr(arr)


    # 루돌프가 움직일 방향 계산
    my, mx = find_rudolf_movement(ry, rx, santa_pos)
    # print(f"루돌프가 움직이는 방향 ({my}, {mx})")
    # 루돌프가 움직이려고 하는 칸이 빈칸인 경우
    if arr[ry + my][rx + mx] == 0:
        arr[ry][rx], arr[ry + my][rx + mx] = arr[ry + my][rx + mx], arr[ry][rx]
        ry = ry + my
        rx = rx + mx

    # 다른 산타가 있는 경우 (루돌프 이동에 의한 충돌)
    else:
        rudolf_collision(ry, rx, my, mx, m)
        ry = ry + my
        rx = rx + mx
    # print("최종 루돌프 이동 및 연쇄 작용 이후 arr ")
    # print_arr(arr)
    # print(f"최종 루돌프 이동 및 연쇄 작용 이후 루돌프 위치 : {ry}, {rx}")

    # 만약 모든 산타가 탈락했다면 즉시 종료
    if sum(is_alive) == 0:
        break

    # 1 ~ P까지 산타들의 움직임
    for santa_idx in range(1, P+1):
        # 산타가 탈락한 경우와 현재 stun 상태인 경우는 고려하지 않음
        if not is_alive[santa_idx] or m < stun[santa_idx]:
            continue
        # 현재 산타 위치
        sy, sx = santa_pos[santa_idx]
        # print(f"{santa_idx} 번째 산타 현재 위치 : ({sy}, {sx}) 이동 시작")
        # 산타가 움직이려는 방향 계산
        my, mx = find_santa_movement(ry, rx, santa_idx)
        # print(f"{santa_idx} 번째 산타 이동 방향 : ({my}, {mx}) ")

        # 산타가 움직였을 때 제자리인 경우
        if arr[sy + my][sx + mx] == santa_idx:
            # print(f"{santa_idx} 제자리 유지")
            continue
        # 산타가 움직였을 때 빈칸인 경우
        elif arr[sy + my][sx + mx] == 0:
            # print(f"{santa_idx} 빈칸 이동 ({sy}, {sx}) -> ({sy + my}, {sx + mx})")
            arr[sy][sx], arr[sy + my][sx + mx] = arr[sy + my][sx + mx], arr[sy][sx]
            santa_pos[santa_idx] = (sy + my, sx + mx)
        # 충돌하는 경우
        elif ry == sy + my and rx == sx + mx:
            # print(f"{santa_idx} 충돌 및 연쇄작용")
            santa_collision(ry, rx, my, mx, santa_idx, m)
    # print(f"산타 전부 이동했을 때 array")
    # print_arr(arr)
    # print(f"최종 루돌프 이동 및 연쇄 작용 이후 루돌프 위치 : {ry}, {rx}")

    # 만약 모든 산타가 탈락했다면 즉시 종료
    if sum(is_alive) == 0:
        break


    # 모든 턴 종료 이후 살아있는 산타에 대해서 1점씩 추가
    for santa_idx in range(1, len(santa_score)):
        if is_alive[santa_idx]:
            santa_score[santa_idx] += 1


# 최종 출력
for i in range(1, len(santa_score)):
    print(f"{santa_score[i]}", end=" ")

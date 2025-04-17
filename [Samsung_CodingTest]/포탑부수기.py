from collections import deque
import sys

from select import select

input = sys.stdin.readline

def print_arr(arr):
    n, m =len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            print(f"{arr[i][j]:<3}", end=' ')
        print()
    print()

def select_attacker(arr, time_arr):
    n, m = len(arr), len(arr[0])

    attack_y, attack_x = -1, -1

    # 가장 약한 포탑을 골라서, 그것의 (y, x)를 반환
    min_power = 5001
    attack_time = -1
    row_col_sum = -1
    col = -1

    for i in range(n):
        for j in range(m):
            # 생존해 있는 포탑들 중에서만 고려해야 한다.
            if arr[i][j] > 0:
                if min_power > arr[i][j]:
                    min_power = arr[i][j]
                    attack_time = time_arr[i][j]
                    row_col_sum = i + j
                    col = j
                elif min_power == arr[i][j]:
                    if attack_time < time_arr[i][j]:
                        attack_time = time_arr[i][j]
                        row_col_sum = i + j
                        col = j
                    elif attack_time == time_arr[i][j]:
                        if row_col_sum < i + j:
                            row_col_sum = i + j
                            col = j
                        elif row_col_sum == (i + j):
                            if col < j:
                                col = j

    attack_y, attack_x = row_col_sum - col, col

    return attack_y, attack_x



def select_victim(arr, time_arr, attack_y, attack_x):
    n, m = len(arr), len(arr[0])

    # 가장 강한 포탑을 골라서, 그것의 (y, x)를 반환
    max_power = -1
    attack_time = 1001
    row_col_sum = n + m + 1
    col = m + 1

    for i in range(n):
        for j in range(m):
            if attack_y == i and attack_x == j:
                continue
            # 생존해 있는 포탑들 중에서만 고려해야 한다.
            if arr[i][j] > 0:
                if max_power < arr[i][j]:
                    # print(f"현재 피해자 Update : {i, j}")
                    max_power = arr[i][j]
                    attack_time = time_arr[i][j]
                    row_col_sum = i + j
                    col = j
                elif max_power == arr[i][j]:
                    if attack_time > time_arr[i][j]:
                        # print(f"현재 피해자 Update : {i, j}")
                        attack_time = time_arr[i][j]
                        row_col_sum = i + j
                        col = j
                    elif attack_time == time_arr[i][j]:
                        if row_col_sum > i + j:
                            # print(f"현재 피해자 Update : {i, j}")
                            row_col_sum = i + j
                            col = j
                        elif row_col_sum == i + j:
                            if col > j:
                                # print(f"현재 피해자 Update : {i, j}")
                                col = j
    victim_y, victim_x = row_col_sum - col, col

    return victim_y, victim_x



def find_lazor_path(start_y, start_x, end_y, end_x, arr):
    n, m = len(arr), len(arr[0])
    # 우 / 하 / 좌 / 상의 우선순위
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    visited = set([(start_y, start_x)])
    queue = deque([(start_y, start_x, [(start_y, start_x)])])

    while queue:
        y, x, path = queue.popleft()
        if y == end_y and x == end_x:
            return path

        for i in range(4):
            ny, nx = (y + dy[i]) % n, (x + dx[i]) % m
            # print(f"ny, nx : {ny, nx}")
            if arr[ny][nx] > 0 and (ny,nx) not in visited:
                visited.add((ny, nx))
                queue.append((ny, nx, path + [(ny, nx)]))

    return []

def find_canon_path(start_y, start_x, end_y, end_x, arr):
    n,m = len(arr), len(arr[0])
    # 최종적으로 return을 할 path라는 list는 0번째 인덱스에는 공격자가, 마지막 인덱스에는 공격 대상이 그리고 중간에는 50%의 공격을 받을 대상들이 들어가야 한다.
    path = [(start_y, start_x)]

    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    # print("포탄 공격 후보지 : ")
    for i in range(len(dy)):
        ny, nx = (end_y + dy[i]) % n, (end_x + dx[i]) % m
        # print(f"{ny, nx} -> {arr[ny][nx]}")
        if arr[ny][nx] > 0:
            # print(f"{ny, nx} -> {arr[ny][nx]} > 0")
            if (ny, nx) != (start_y, start_x):
                path.append((ny, nx))
                # print("경로에 포함")
        # print()

    path.append((end_y, end_x))

    return path


def check_only_survivor(arr):
    n, m = len(arr), len(arr[0])
    survivor = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                survivor += 1
            else:
                arr[i][j] = 0 # 이거는 여기에서 죽은 포탑은 음수를 가지는 것이 아니라 0의 값을 갖도록 만들어줘야 victim을 정할 때 reverse로 바로 할 수 있다.

    return survivor



N, M, K = map(int, input().split())
arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

# print_arr(arr)

time_arr = [[0] * M for _ in range(N)]


for t in range(1, K+1):
    # print(f"=============={t}번째 공격 ==============")
    # print_arr(arr)
    # 공격자 포탑 선정
    attack_y, attack_x = select_attacker(arr, time_arr)
    arr[attack_y][attack_x] = arr[attack_y][attack_x] + N + M
    time_arr[attack_y][attack_x] = t
    # 공격당할 대상 포탑 선정
    victim_y, victim_x = select_victim(arr, time_arr, attack_y, attack_x)

    # print(f"공격자 : {attack_y, attack_x}")
    # print(f"공격 피해자 : {victim_y, victim_x}")



    # 공격
    # 레이저 공격
    path = find_lazor_path(attack_y, attack_x, victim_y, victim_x, arr)

    # 만약 레이저 공격의 경로를 찾지 못했다면
    if len(path) == 0:
        # print("포탄공격을 해야한다.")
        path = find_canon_path(attack_y, attack_x, victim_y, victim_x, arr)
    # else:
    #     print("레이저 공격 실행")

    # 공격력
    power = arr[attack_y][attack_x]
    # print(f"공격 경로 : {path} | 공격력 : {power}\n")
    #
    # print(f"공격 경로에 있는 대상 : ", end=' ')
    for i in range(1, len(path)-1):
        # 공격 당해야 하는 대상의 y,x 좌표를 얻는다.
        y, x = path[i][0], path[i][1]
        # print(f"{y, x}", end=' ')
        arr[y][x] = arr[y][x] - (power // 2)

    y, x = path[-1][0], path[-1][1]
    # print(f"\n최종 공격 대상 : {y, x}")
    arr[y][x] = arr[y][x] - power

    # print("공격이 된 이후 array")
    # print_arr(arr)


    # 포탑 정비
    # 공격에 관여한 포탑들을 set으로 만든다.
    active_set = set(path)
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and (i, j) not in active_set:
                arr[i][j] += 1

    # print("포탑 정비 후 array")
    # print_arr(arr)

    # 공격이 끝난 이후에 생존 포탑이 1개이면 바로 나온다.
    survivor = check_only_survivor(arr)
    # print(f"생존 포탑 수 : {survivor}")
    if survivor == 1:
        break


# 최종 출력 : 현존하는 포탑들 중에서 가장 강한 포탑의 공격력을 출력한다.
strong_y, strong_x = select_victim(arr, time_arr, -1, -1)
print(arr[strong_y][strong_x])

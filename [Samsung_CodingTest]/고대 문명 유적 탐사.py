from collections import deque
def print_arr(arr):
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            print(f"{arr[i][j]:<3}", end=' ')
        print()
    print()

def rotation_arr(start_y, start_x, length, angle, arr):
    # 해당 array를 angle만큼 돌린다.
    # 이 때 원본 array를 가지고 하는 것이 아닌 복사본을 가지고 한다.
    n, m = len(arr), len(arr[0])
    copy_arr = [[0] * m for _ in range(m)]
    for i in range(n):
        for j in range(m):
            copy_arr[i][j] = arr[i][j]

    temp_arr = [[0] * m for _ in range(n)]
    for y in range(start_y, start_y + length):
        for x in range(start_x, start_x + length):
            oy, ox = y - start_y, x - start_x
            if angle == 90:
                ry, rx = ox, length - 1 - oy
            elif angle == 180:
                ry, rx = length - 1 - oy, length - 1 -ox
            elif angle == 270:
                ry, rx = length - 1 - ox, oy
            temp_arr[start_y + ry][start_x + rx] = copy_arr[y][x]

    for y in range(start_y, start_y + length):
        for x in range(start_x, start_x + length):
            copy_arr[y][x] = temp_arr[y][x]

    return copy_arr


def connection(start_y, start_x, graph, visited):
    n, m = len(graph), len(graph[0])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited[start_y][start_x] = True
    value = graph[start_y][start_x]
    queue = deque([(start_y, start_x)])

    component = []

    while queue:
        y, x = queue.popleft()
        component.append((y, x))

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<= ny < n and 0<= nx < m:
                if graph[ny][nx]==value and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))

    return component

def cal_treasure_value(arr):
    # 해당 array에서 유물이 되는 list를 반환한다.
    n, m = len(arr), len(arr[0])
    visited = [[False] * m for _ in range(n)]

    answer = []

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                component = connection(i, j, arr, visited)
                if len(component) >= 3:
                    answer += component

    return answer





# 정보 입력 받기
# K : 탐사 반복 횟수  | M : 벽면에 적힌 유물 조각의 개수
K, M = map(int, input().split())

arr = []
for i in range(5):
    row = list(map(int, input().split()))
    arr.append(row)

wall = list(map(int, input().split()))

# print(f"K : {K}")
# print(f"M : {M}")

# print("Array")
# print_arr(arr)

# print(f"Wall : {wall}")
wall_idx = 0

# K 번의 유물 획득 과정을 거친다.
for _ in range(K):
    total_value = 0

    first_value = 0
    best_treasure_list = []
    best_i = -1
    best_j = -1
    best_angle = -1
    # 유물 1차 가치 획득 시도 : 우선순위가 높은 순으로 조건이 수행되고, 동점의 경우에는 갱신하지 않음으로써 조건이 맞춰지도록 했다.
    for angle in [90, 180, 270]:
        for j in range(3):
            for i in range(3):
                # 먼저 임시로 회전해보자.
                rotated_array = rotation_arr(i, j, 3, angle, arr)
                # 회전된 array의 유물 가치를 계산
                curr_treasure_list = cal_treasure_value(rotated_array)
                curr_value = len(curr_treasure_list) # 현재 회전된 유물 가치

                if first_value < curr_value: # 현재 가치가 지금까지 중 가장 큰 경우
                    first_value = curr_value
                    best_treasure_list = curr_treasure_list
                    best_i = i
                    best_j = j
                    best_angle = angle

    # 만약 1차 유물 획득이 0이라면 바로 종료
    if first_value == 0:
        exit()

    # 1차 유물획득이 0이 아닌 경우에는 지속

    # 이제 best로 실제로 array를 돌려야 한다.
    rotated_array = rotation_arr(best_i, best_j, 3, best_angle, arr)
    for i in range(best_i, best_i + 3):
        for j in range(best_j, best_j + 3):
            arr[i][j] = rotated_array[i][j]

    # 1차 유물 획득 : total_value를 올리고, 유물이 된 부분을 0으로 만든다.
    total_value += first_value
    for (y, x) in best_treasure_list:
        arr[y][x] = 0

    # 벽면에 있는 것들로 우선순위에 맞춰서 빈칸을 보면 채워간다.
    for j in range(len(arr[0])):
        for i in range(len(arr)):
            if arr[4-i][j] == 0:
                arr[4-i][j] = wall[wall_idx]
                wall_idx += 1


    # 유물 연쇄 획득 가능한지 확인 -> 해당 array에서 더이상 유물이 발견이 되지 않을때까지 반복
    while len(cal_treasure_value(arr)) != 0:
        additional_treasure_list = cal_treasure_value(arr)

        total_value += len(additional_treasure_list)
        for (y, x) in additional_treasure_list:
            arr[y][x] = 0

        # 벽면에 있는 것들로 우선순위에 맞춰서 빈칸을 보면 채워간다.
        for j in range(len(arr[0])):
            for i in range(len(arr)):
                if arr[4 - i][j] == 0:
                    arr[4 - i][j] = wall[wall_idx]
                    wall_idx += 1

    print(total_value, end=' ')

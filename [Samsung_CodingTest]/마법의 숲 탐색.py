from collections import deque

def print_arr(arr):
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            print(f"{arr[i][j]:<3}", end=' ')
        print()
    print()

def golem_movement(c, d):
    global arr
    n, m = len(arr), len(arr[0])
    # 골렘이 최대한 움직여서 위치하게된 정령의 위치와 해당 골렘의 출구 위치를 반환
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    # 골렘이 더 움직일 수 있는지 판단하게 하는
    not_anymore = False
    # 초기 정령의 위치
    y, x = 0, c
    # print(f"초기 골렘의 위치 : {y, x}")

    while not not_anymore:
        # 1번 경우: 남쪽으로 한칸 이동
        # if 0<= y < n-2 and 2 <= x < m-2:
        if 0 <= y < n - 2:
            # print(f"arr[{y+1}][{x-1}] + arr[{y+2}][{x}] + arr[{y+1}][{x+1}]")
            if arr[y+1][x-1] + arr[y+2][x] + arr[y+1][x+1] == 0: # 세 칸이 모두 비어 있는 경우
                # print("남으로 1칸 이동")
                y += 1
                continue
            # 2번 경우: 서쪽 방향으로 회전하면서 내려감
            elif y ==0 and 2< x and arr[y][x-2] + arr[y+1][x-2] + arr[y+1][x-1] + arr[y+2][x-1] == 0:
                # print("서쪽으로 회전 후 남쪽으로 1칸 이동")
                y += 1
                x -= 1
                d = (d - 1) % 4
                continue
            elif y != 0 and 2< x and arr[y-1][x-1] + arr[y][x-2] + arr[y+1][x-2] + arr[y+1][x-1] + arr[y+2][x-1] == 0:
                # print(f"서쪽으로 회전 후 남쪽으로 1칸 이동 - 이동 전 좌표 : {y, x}")
                y += 1
                x -= 1
                d = (d - 1) % 4
                continue

            # 3번 경우: 동쪽 방향으로 회전하면서 내려감
            # elif y == 0 and x < m-2 and arr[y][x+1] + arr[y+1][x+2] + arr[y+1][x+1] + arr[y+2][x+1] == 0:
            elif y == 0 and x < m - 2 and arr[y][x + 2] + arr[y + 1][x + 2] + arr[y + 1][x + 1] + arr[y + 2][x + 1] == 0:
                # print("동쪽으로 회전 후 남쪽으로 1칸 이동")
                y += 1
                x += 1
                d = (d + 1) % 4
                continue
            elif y != 0 and x < m-2 and arr[y-1][x+1] + arr[y][x + 2] + arr[y + 1][x + 2] + arr[y + 1][x + 1] + arr[y + 2][x + 1] == 0:
                # print("동쪽으로 회전 후 남쪽으로 1칸 이동")
                y += 1
                x += 1
                d = (d + 1) % 4
                continue
        not_anymore = True

    exit_y = y + dy[d]
    exit_x = x + dx[d]
    # print(f"최종 골렘의 위치 : {y,x} | 출구 위치 : {exit_y, exit_x}")

    return y, x, exit_y, exit_x

def get_final_elf_position(elf_y, elf_x):
    # 해당 위치에서 시작하는 정령의 움직임으로 최대한 남쪽으로 내려가보는 것
    global arr, exit_list
    n, m = len(arr), len(arr[0])

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]


    visited = set([(elf_y, elf_x)])
    queue = deque([(elf_y, elf_x, arr[elf_y][elf_x])]) # 마지막에 현재 위치한 골렘의 인덱스도 추가적으로 넣었다.

    final_y, final_x = 0, 0 # 최남단 좌표 초기화
    # 갈 수 있는 모든 곳을 가면서 queue에서 나왔을 때 최남단인지 확인
    while queue:
        y, x, golem_idx = queue.popleft()
        if y > final_y:
            final_y, final_x = y, x

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 1 <= ny < n and 0<= nx < m:
                # Case 1. 동일한 골렘 안에서 움직이는 경우
                if arr[ny][nx] == golem_idx and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    queue.append((ny, nx, golem_idx))
                # Case 2. 현재 위치(y,x)가 출구이므로, 다른 골렘으로 갈아타는 경우
                elif arr[ny][nx] != 0 and exit_list[golem_idx] == (y, x) and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    queue.append((ny, nx, arr[ny][nx]))

    return final_y, final_x

# R, C : 숲의 크기 | K : 정령의 수
R, C, K = map(int, input().split())

# arr = [[0] * (C+1) for _ in range(R+1)]
arr = [[0] * (C+1) for _ in range(R+2)]
# print("깨끗한 숲")
# print_arr(arr)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

exit_list = [(-1, -1)]
final_answer = 0


for k in range(1, K+1):
    c, d = map(int, input().split())

    # k번째 골렘에서 정령의 위치와 골렘 출구의 위치
    elf_y, elf_x, exit_y, exit_x = golem_movement(c, d)

    # 만약 골렘이 최대한 움직였는데, 몸의 일부가 밖에 나가있다. -> 다 지워 (근데, 출구 좌표는 더미로 하나 넣어야 함)
    # if elf_y <= 1:
    if elf_y <= 2:
        exit_list.append((-1, -1))
        # arr = [[0] * (C+1) for _ in range(R + 1)]
        arr = [[0] * (C + 1) for _ in range(R + 2)]
        continue

    # 골렘이 해당 숲 안에 들어있다면
    # 골렘의 인덱스로 숲의 빈칸을 채운다.
    arr[elf_y][elf_x] = k
    for i in range(4):
        ny, nx = elf_y + dy[i], elf_x + dx[i]
        arr[ny][nx] = k
    # 해당 골렘의 출구도 출구 리스트에 넣어준다.
    exit_list.append((exit_y, exit_x))
    # print(f"{k}번째 골렘이 최대한 내려왔을 때 Array")
    # print_arr(arr)

    # 정령이 갈수 있는 최대한 남쪽으로 간다.
    final_y, final_x = get_final_elf_position(elf_y, elf_x)
    # print(f"{k}번째 정령이 갈 수 있는 최남단 좌표 : {final_y, final_x}")
    # final_answer += final_y
    final_answer += final_y - 1

    # print(f"{k}번째 시점에 final_answer : {final_answer}")
    # print("==================================================================")

print(final_answer)


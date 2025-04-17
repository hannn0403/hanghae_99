from collections import deque

def print_arr(arr):
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            print(f"{arr[i][j]:<3}", end=' ')
        print()
    print()



def canMove(k_idx, d_idx, knight_pos, knight_area, L):
    global knight_arr
    n, m = len(knight_arr), len(knight_arr[0])
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


    # 기사들의 움직임이 가능한지를 알려주는 boolean 변수
    possible = True

    # knight_arr 딥카피
    copy_arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            copy_arr[i][j] = knight_arr[i][j]

    copy_pos = []
    copy_area = []
    for i in range(len(knight_pos)):
        copy_pos.append(knight_pos[i])
        copy_area.append(knight_area[i])

    # 왕명을 받은 기사 제외하고 움직인 기사들의 인덱스 리스트
    moved_knights = set([k_idx])
    queue = deque([k_idx])

    while queue and possible:
        knight_idx = queue.popleft()
        r,c = copy_pos[knight_idx]
        h,w = copy_area[knight_idx]
        dy, dx = d[d_idx]

        # 먼저 움직였을 때 chess 판 위에 있는지 확인
        if 0 < r + dy <= L - h + 1 and 0 < c + dx <= L - w  + 1:
            possible = True
        else:
            possible = False
            continue

        # 그 다음에 움직인 이후 영역에 벽(-1)이 존재하는 지 확인
        for y in range(r, r + h):
            for x in range(c, c + w):
                if copy_arr[y + dy][x + dx] == -1:
                    # print(f"{knight_idx}번 기사가 {dy, dx}로 움직이려는 와중 벽이 존재함 : (copy_arr[{y} + {dy}][{x} + {dx}])")
                    # print_arr(copy_arr)
                    possible = False
        # 움직이려는 영역에 벽이 존재한다면 while을 나온다.
        if not possible:
            break


        # 움직일 수 있는 경우에 움직인 이후 영역에 다른 기사 인덱스가 존재하는 지 확인 후 있다면 queue에 넣는다.
        # 먼저 array에서 현재 위치를 전부 빈칸으로 만든다.
        # 이 때 이미 이전 기사가 움직여서 해당 값으로 덮어씌워진 칸은 놔둔다.
        for y in range(r, r+h):
            for x in range(c, c + w):
                if copy_arr[y][x] == knight_idx:
                    copy_arr[y][x] = 0

        # 이후 array에 해당 인덱스를 입력해가며 0이 아닌 값이 있는 경우에는 queue에 넣는다. (이 때 중복적으로 넣지 않게 moved_knights를 통해 확인)
        for y in range(r, r+h):
            for x in range(c, c + w):
                if copy_arr[y + dy][x + dx] != 0 and copy_arr[y + dy][x + dx] not in moved_knights:
                    # print(f"{copy_arr[y + dy][x + dx]}도 연쇄이동해야함")
                    moved_knights.add(copy_arr[y + dy][x + dx])
                    queue.append(copy_arr[y + dy][x + dx])
                copy_arr[y+dy][x+dx] = knight_idx
        # print(f"{knight_idx}가 움직인 이후 copy_arr")
        # print_arr(copy_arr)

        # 다 움직였다면 기사들의 위치를 업데이트한다.
        prev_y, prev_x = copy_pos[knight_idx]
        copy_pos[knight_idx] = (prev_y + dy, prev_x+dx)

    moved_knights.remove(k_idx) # 왕명을 받은 기사는 대미지 계산에서 제외하기 위해 빼준다.
    return possible, copy_arr, copy_pos, list(moved_knights)

def calDamage(knight_idx):
    global knight_pos, knight_area, knight_hp, chess, knight_arr
    # 해당 기사의 영역에 존재하는 함정의 수를 계산해서 기사의 대미지를 계산하고 이를 knight_hp에 반영한다.

    r,c = knight_pos[knight_idx]
    h,w = knight_area[knight_idx]
    # k = knight_hp[knight_idx]

    # 해당 영역 돌면서 확인
    trap_num = 0
    for i in range(r, r+h):
        for j in range(c, c + w):
            if chess[i][j] == 1:
                trap_num += 1

    # print(f"{knight_idx}번 기사가 받은 피해 : {trap_num} | HP : {knight_hp[knight_idx]} -> {knight_hp[knight_idx] - trap_num}")

    knight_hp[knight_idx] = knight_hp[knight_idx] - trap_num

    # 만약 해당 기사의 체력이 0과 같거나 작아진다면 array에서 빼준다.
    if knight_hp[knight_idx] <= 0:
        # print(f"{knight_idx}의 기사의 체력이 소진되었으므로 knight_arr에서 제외")
        for y in range(len(knight_arr)):
            for x in range(len(knight_arr[0])):
                if knight_arr[y][x] == knight_idx:
                    knight_arr[y][x] = 0

        # print_arr(knight_arr)



# L (격자한면 길이), N (기사 수), Q (명령 수)
L, N, Q = map(int, input().split())

# 체스판 정보 (L+1, L+1) 의 격자를 만들고, 0행, 0열은 벽으로 채운다.
# 먼저 일단 정보 입력 받음
temp_arr = []
for i in range(L):
    row = list(map(int, input().split()))
    temp_arr.append(row)

chess = [[2] * (L+1) for _ in range(L+1)]
for i in range(L):
    for j in range(L):
        chess[i + 1][j + 1] = temp_arr[i][j]

# print()
# print_arr(chess)

# 기사들의 영역을 표시할 knight_arr도 있어야 된다.
knight_arr = [[0] * (L+1) for _ in range(L+1)]
for i in range(L+1):
    for j in range(L+1):
        if chess[i][j] == 2:
            knight_arr[i][j] = -1



# 기사 정보 입력 받기 : 이것도 왕의 명령이 1 ~ N 번 기사를 하므로, 리스트의 0번째 인덱스에는 더미 정보가 들어가야 한다.
knight_pos = [(-1, -1)] # 기사의 좌 상단 위치
knight_area = [(0,0)]   # 기사의 방패 영역
knight_hp = [0]         # 기사의 체력

for _ in range(N):
    r,c, h, w, k = map(int, input().split())
    knight_pos.append((r,c))
    knight_area.append((h, w))
    knight_hp.append(k)

# 최종적으로 입은 대미지의 합을 구해야 하므로, 원본 체력 리스트를 별도로 저장해놓아야 한다.
origin_hp = []
for i in range(len(knight_hp)):
    origin_hp.append(knight_hp[i])

# print(f"기사 위치 리스트 : {knight_pos}")
# print(f"기사 방패 리스트 : {knight_area}")
# print(f"기사 체력 리스트 : {knight_hp}")


# knight_arr에 정보를 반영
for i in range(1, len(knight_pos)):
    r, c = knight_pos[i]
    h, w = knight_area[i]

    for y in range(r, r + h):
        for x in range(c, c + w):
            knight_arr[y][x] = i

# print("정보를 반영한 knight_arr")
# print_arr(knight_arr)
# print('=============================')
# print()

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 왕명 입력
for _ in range(Q):
    k_idx, d_idx = map(int, input().split())
    # print(f"{k_idx}번 기사가, {d[d_idx]} 방향으로 이동")

    # 먼저 왕명을 받은 기사가 생존해 있는 지 확인 -> 생존 X 라면 바로 넘어가
    if knight_hp[k_idx] <= 0:
        # print(f"{i}번째 기사의 hp는 {knight_hp[i]} 이므로 움직일 수 없음 - 체스판에서 사라짐")
        continue

    possible, copy_arr, copy_pos, moved_knights = canMove(k_idx, d_idx, knight_pos, knight_area, L)
    # 기사들이 움직이는게 불가능하다면 바로 넘어가
    if not possible:
        # print(f"{k_idx}번 기사가, {d[d_idx]} 방향으로 이동하는 것은 불가능")
        # print()
        # print("원본 array")
        # print_arr(knight_arr)
        # print("============================")
        # print()
        continue

    # 기사들이 움직이는게 가능하다면 knight_arr를 copy_arr로 반영
    for i in range(len(knight_arr)):
        for j in range(len(knight_arr[0])):
            knight_arr[i][j] = copy_arr[i][j]

    # 기사들이 움직이는게 가능하다면 knight_pos를 copy_pos로 반영
    for i in range(len(knight_pos)):
        knight_pos[i] = copy_pos[i]

    # print("기사들이 움직인 이후에 knight_arr")
    # print_arr(knight_arr)

    # 그리고 움직인 기사들의 대미지를 계산
    for knight_idx in moved_knights:
        calDamage(knight_idx)

# 최종 출력
final_answer = 0
for i in range(len(knight_hp)):
    # 기사가 생존한 경우에만 받은 데미지를 더해야 한다.
    if knight_hp[i] > 0:
        final_answer += (origin_hp[i] - knight_hp[i])

print(final_answer)

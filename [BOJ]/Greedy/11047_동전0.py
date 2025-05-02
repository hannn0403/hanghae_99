import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coin_list = []
for _ in range(N):
    coin_list.append(int(input()))

coin_num = 0
coin_idx = len(coin_list) - 1
while K > 0 and coin_idx >= 0:
    curr_coin = coin_list[coin_idx]
    mok = K // curr_coin
    rest = K % curr_coin

    if mok == 0:
        coin_idx -= 1
        continue

    else:
        coin_num += mok
        K = rest
        coin_idx -= 1

print(coin_num)

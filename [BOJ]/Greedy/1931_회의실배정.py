import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input())

meeting_pq = PriorityQueue()
meeting_num = 0

for _ in range(N):
    s, e = map(int, input().split())
    meeting_pq.put((e, s))

time = 0

while not meeting_pq.empty():
    e, s = meeting_pq.get()
    if time <= s:
        meeting_num += 1
        # print(
        #     f"현재 시각: {time}| {s} ~ {e}까지 진행되는 미팅을 할 수 있습니다. | 현재까지 진행된 미팅수 : {meeting_num}"
        # )
        time = e
print(meeting_num)

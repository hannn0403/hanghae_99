import sys

input = sys.stdin.readline

n = int(input())
stack = []
sign_list = []
numbers = [n - i + 1 for i in range(1, n + 1)]
ref_list = [0] * (n + 1)

for i in range(1, n + 1):
    num = int(input())
    ref_list[i] = num

# print(f"numbers : {numbers}")
# print(f"ref_list : {ref_list}")

for i in range(1, n + 1):

    prev_num = ref_list[i - 1]
    curr_num = ref_list[i]
    # print(f"{i}번째 숫자 처리 | prev_num : {prev_num} | curr_num : {curr_num} ")

    if prev_num < curr_num:
        # 이전 숫자보다 현재 숫자가 큰 경우에, 현재 숫자 만큼 stack에 push한다.
        while len(numbers) > 0 and numbers[-1] <= curr_num:
            push_num = numbers.pop()
            stack.append(push_num)
            # print(f"stack에 {push_num} 삽입 | 현재 stack : {stack}")
            sign_list.append("+")
        # 다 넣었으면 마지막에 curr_num을 pop해줘야 한다.
        stack.pop()
        # print(f"다 삽입한 이후 마지막에 pop | 현재 stack : {stack}")
        sign_list.append("-")

    elif prev_num > curr_num:
        # 이전 숫자보다 현재 숫자가 작은 경우에, pop을 할 것인지 아니면 NO를 출력할 것인지 확인
        if curr_num == stack[-1]:
            # 만약 현재 숫자가 stack에 있는 마지막 숫자와 동일하다면 -> pop
            pop_num = stack.pop()
            # print(f"stack에 {pop_num} pop | 현재 stack : {stack}")
            sign_list.append("-")

        else:
            print("NO")
            exit()

for si in sign_list:
    print(si)

import sys

input = sys.stdin.readline

cal_str = input()
num_list = []
sign_list = []

num_str = ""
for i in range(len(cal_str)):
    if cal_str[i] == "\n":
        num_list.append(int(num_str))
        continue

    if cal_str[i] != "+" and cal_str[i] != "-":
        num_str += cal_str[i]
    else:
        num_list.append(int(num_str))
        sign_list.append(cal_str[i])
        num_str = ""

# print(f"num_list : {num_list}")
# print(f"sign_list : {sign_list}")


result = num_list[0]
num_idx = 1
sign_idx = 0


during_minus = False
minus_num = 0
while num_idx < len(num_list) and sign_idx < len(sign_list):

    sign = sign_list[sign_idx]
    num = num_list[num_idx]
    # print(f"sign : {sign} | num : {num }")

    if sign == "-":
        during_minus = True
        # print(f"{result} - {num}")
        result -= num
    elif sign == "+" and not during_minus:
        # print(f"{result} + {num}")
        result += num
    elif sign == "+" and during_minus:
        # print(f"{result} - {num}")
        result -= num

    num_idx += 1
    sign_idx += 1

print(result)

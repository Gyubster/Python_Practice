# s = "1S2D*10T"
# print([i for i in range(1,4)])
#
# s_list = list(map(str, s))
# s_list.append('')
# #맨뒤에 넣는 수를 못찾음
# for i in range(1, len(s_list)//3):
#     if s_list[3*i] != '*' or s_list[3*i] != '#':
#         s_list.insert(3*i-1, '')
#
# first_list = [str(i) for i in s_list[:3]]
# second_list = [str(i) for i in s_list[3:6]]
# third_list = [str(i) for i in s_list[6:]]
#
# print(third_list)


# def solution(dart_result):
#     dart_result_list = list(map(str, dart_result))
#     for i in range(dart_result):
#         dart_result[i]
s = "1S"
s1 = "2D"

# is digit -> str에서 숫자인지아닌지.
# is alpha -> str에서 문자열인지아닌지.
# for idx, val in enumerate(arr, n)

import re
dart_result = "1S2D*10T"
bonus = {'S': 1, 'D': 2, 'T': 3}
option = {'*': 2, '#': -1}

#있거나 없거나의 경우는 바깥에 물음표가 붙음.
part = re.compile('(\d+)([SDT])([*#]?)')
match_part = part.findall(dart_result)

print(match_part)
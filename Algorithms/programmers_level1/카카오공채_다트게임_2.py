import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'*' : 2, '#' : -1, '' : 1}

    #있거나 없거나의 경우는 바깥에 물음표가 붙음.
    part = re.compile('(\d+)([SDT])([*#]?)')
    dart = part.findall(dartResult)

    for i in range(len(dart)):
        if dart[i][2] == '*' and i>0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    answer = sum(dart)
    return answer

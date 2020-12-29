def solution(n):
    str_list = []
    for i in range(n):
        if i%2 == 0:
            str_list.append('수')
        else:
            str_list.append('박')
    answer = "".join(str_list)
    return answer

n = 3
solution(n)

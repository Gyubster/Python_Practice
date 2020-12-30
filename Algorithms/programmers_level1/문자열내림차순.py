def solution(s):
    string_list = list(map(str, s))
    string_list.sort()
    string_list.reverse()
    answer = "".join(string_list)
    return answer

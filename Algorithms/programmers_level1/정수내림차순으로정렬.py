def solution(n):
    n_list = list(map(str, str(n)))
    n_list.sort()
    n_list.reverse()
    answer = int("".join(n_list))
    return answer
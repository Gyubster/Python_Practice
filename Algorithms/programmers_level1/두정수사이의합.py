def solution(a, b):
    if a<=b:
        sol_list = [i for i in range(a, b+1)]
        answer = sum(sol_list)
    elif a>=b:
        sol_list = [i for i in range(b, a+1)]
        answer = sum(sol_list)
    return answer
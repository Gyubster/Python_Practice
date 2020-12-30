def solution(s):
    mid_point = (len(s)-1)//2
    if len(s)%2 == 0:
        answer = f"{s[mid_point]}{s[mid_point+1]}"
    else:
        answer = f"{s[mid_point]}"
    return answer
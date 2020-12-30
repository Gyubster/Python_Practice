def solution(s):
    answer = True
    number_list = [str(i) for i in range(1, 10)]
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if s[i] not in number_list:
                verification_string = 1
                if verification_string == 1:
                    answer = False
    return answer

def solution2(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        try:
            type(int(s)) == int

        except ValueError:
            answer = False
    else:
        answer = False
    return answer
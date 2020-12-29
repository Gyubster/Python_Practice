s = "a B z"
n = 4

def solution(s, n):
    s_list = list(map(str, str(s)))
    answer_list = []

    for i in range(len(s_list)):
        aski_s = ord(s_list[i])
        print(aski_s)
        if aski_s >= 97 and aski_s <= 122:
            sum_aski_s = aski_s + n
            if sum_aski_s > 122:
                sum_aski_s = sum_aski_s - 122 + 97 - 1
                fixed_s = chr(sum_aski_s)
                answer_list.append(fixed_s)
            else:
                fixed_s = chr(sum_aski_s)
                answer_list.append(fixed_s)
        elif aski_s >= 65 and aski_s <= 90:
            sum_aski_s = aski_s + n
            if sum_aski_s > 90:
                sum_aski_s = sum_aski_s - 90 + 65 - 1
                fixed_s = chr(sum_aski_s)
                answer_list.append(fixed_s)
            else:
                fixed_s = chr(sum_aski_s)
                answer_list.append(fixed_s)
        elif aski_s == 32:
            sum_aski_s = 32
            fixed_s = chr(sum_aski_s)
            answer_list.append(fixed_s)
    answer = "".join(answer_list)
    return answer

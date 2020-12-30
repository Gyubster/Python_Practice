def solution(arr, divisor):
    answer_list = [i for i in arr if i%divisor == 0]
    answer = answer_list.sort()
    if answer == []:
        answer = [-1]
    return answer
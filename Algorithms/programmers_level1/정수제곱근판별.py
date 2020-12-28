import math

def solution(n):
    number_range = math.sqrt(50000000000000)
    square_list = [i**2 for i in range(number_range)]
    if n not in square_list:
        answer = -1
    elif n in square_list:
        number = int(math.sqrt(n))
        answer = (number+1)**2
    return answer

def solution(num):
    n = 0
    answer = 0
    while True:
        if n != 500:
            if num != 1:
                if num%2 == 0:
                    num = num/2
                    n += 1
                elif num%2:
                    num = num*3 + 1
                    n += 1
            elif num ==1:
                answer = n
                print(answer)
                return answer
        elif n==500:
            answer = -1
            print(answer)
            return answer

num = 626331
solution(num)

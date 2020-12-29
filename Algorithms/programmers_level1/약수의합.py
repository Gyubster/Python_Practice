def solution(n):
    n = int(n)
    divisor_list = []
    for i in range(1, n+1):
        if n%i == 0:
            divisor_list.append(i)
    answer = sum(divisor_list)
    print(answer)
    return answer

n = 12
solution(n)

print([i for i in range(1,25)])
def solution(n):
    prime_number_list = []
    prime_number_list2 = []
    for i in range(1,1000000):
        n = i
        for j in range(1,i):
            if i%j == 0:
                prime_number_list2.append(i/j)
                if len(prime_number_list2) == 2:
                    prime_number_list.append(i)
    for i in range(len(prime_number_list)):
        if n < prime_number_list[i]:
            answer = i-1
    return answer

# 소수 리스트를 만들고 그 안의 요소와 숫자를 비교하여 n을 출력. -> 실패
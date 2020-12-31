n=6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

def line(arr, n):
    arr_answer = []
    for i in range(n):
        a = arr[i]
        arr_list = []
        for j in range(n-1, -1, -1):
            b = 2**j
            if a >= b:
                arr_list.append('#')
                a -= b
            else:
                arr_list.append(' ')
        arr_answer.append(arr_list)
    return arr_answer

def solution(arr1, arr2, n):
    arr1_list = line(arr1, n)
    print(arr1_list)
    arr2_list = line(arr2, n)
    print(arr2_list)
    answer = []

    for i in range(n):
        answer_list = []
        for j in range(n):
            if arr1_list[i][j] == ' ' and arr2_list[i][j] == ' ':
                answer_list.append(' ')
            else:
                answer_list.append('#')
        answer_string = "".join(answer_list)
        print(answer_string)
        answer.append(answer_string)
    print(answer)
    return answer

solution(arr1, arr2, n)

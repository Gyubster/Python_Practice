n=5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

# list, dict 둘다 값을 집어넣는 방식은 유사.

def solution(n, arr1, arr2):
    arr = [arr1[i]+arr2[i] for i in range(n)]
    arr_answer = []

    for i in range(len(arr)):
        a = arr[i]
        arr_list =[]
        for j in range(n-1, -1, -1):
            s = 2**j
            if a >= s:
                a -= s
                arr_list.append('#')
            else:
                arr_list.append(' ')
        answer_string = "".join(arr_list)
        arr_answer.append(answer_string)

    return arr_answer


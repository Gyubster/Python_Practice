def solution_not_answer(arr):
    return list(set(arr))
# 다지우는게 아님

def solution(arr):
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1]:
            del arr[i]
    return arr

arr = [1, 1, 3, 3, 0, 1, 1]
answer = []

answer.append(arr[0])
for i in range(len(arr)):
    if answer[i-1] != arr[i]:
        answer.append(arr[i])

#리스트 오류 범위 맞는것같은데..
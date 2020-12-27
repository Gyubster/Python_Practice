def solution(arr):
    if len(arr) != 1:
        list_length = len(arr)
        list_min= min(arr)
        for i in range(list_length):
            if arr[i] == list_min:
                del arr[i]
    else:
        arr[0] = -1
    return arr
# 왜안되는지 모르겟음.
arr = [5,4,3,2,1]
arr1 = [1,2,3,4,5]
solution(arr1)
print(arr)

def solution(arr):
    list_length = len(arr)
    list_min = min(arr)

    if list_length > 1:
        arr.remove(list_min)
    elif list_length == 1:
        arr[0] = -1
    return arr
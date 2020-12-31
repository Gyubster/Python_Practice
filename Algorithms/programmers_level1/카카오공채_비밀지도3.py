#비트연산 체크

n=5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]
answer = []

def solution(arr1, arr2, n):
    answer=[]
    for i in range(n):
        a = bin(arr1[i] | arr2[i])[2:]
        answer.append(a.replace('1','#').replace('0',' '))
    return answer

def solution2(n, arr1, arr2):
    ans = []
    for i in range(n):
        bin_str = bin(arr1[i] | arr2[i])[2:]
        ans.append(("0" *(n - len(bin_str)) + bin_str).replace("1", "#").replace("0", " "))
    return ans

for i in range(n):
    bin_str = bin(arr1[i] | arr2[i])[2:]

a = ("0" *(n - len(bin_str)) + bin_str).replace('1','#').replace('0',' ')
b = bin_str.replace('1','#').replace('0',' ')

print(type(a))
print(type(b))
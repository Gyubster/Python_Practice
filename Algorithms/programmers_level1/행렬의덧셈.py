#
# def solution(arr1, arr2):
#     answer = []
#     MatrixLength = len(arr1[0])
#     for i in range(len(arr1)):
#         ListElementSum =[]
#         for j in range(MatrixLength):
#             ElementSum = arr1[i][j] + arr2[i][j]
#             ListElementSum.append(ElementSum)
#         answer.append(ListElementSum)
#     return answer

c = [1, 2]
d = [3, 4]
print(list(zip(c,d)))
print([a+b for a,b in zip(c, d)])

A = [[1,2], [2,3]]
B = [[3,4],[5,6]]
answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]

print(list(zip(A,B)))
print(answer)
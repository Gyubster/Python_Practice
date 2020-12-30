#앞에 인덱스를 붙여서 정렬한 이후 인덱스 지우기.

def solution(l, n):
    new_l = []
    for i in range(len(l)):
        new_s = l[i][n] + l[i]
        new_l.append(new_s)
    new_l.sort()
    for i in range(len(new_l)):
        new_l[i] = new_l[i][1:]
    answer = new_l
    return answer


n = 1
l = ["sun", "bed", "car"]
print(l[1][1])


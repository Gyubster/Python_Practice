
def solution(x):
    x = int(x)
    NumberList = list(map(int, str(x)))
    HashadNumber = sum(NumberList)
    if int(x)%HashadNumber == 0:
        answer = True
    else:
        answer = False
    return answer
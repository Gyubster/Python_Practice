
def solution(participant, completion):
    AnswerList = [x for x in participant if x not in completion]
    answer = AnswerList[0]
    return answer

# 겹치는 경우를 다 지워버림.


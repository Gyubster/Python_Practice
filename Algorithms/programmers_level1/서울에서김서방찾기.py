def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            location = i
    answer = f"김서방은 {location}에 있다"
    return answer
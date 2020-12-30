def solution (a, b):
    month_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_list = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    if a == 1:
        days = b
    else:
        days = sum(month_list[:a-1]) + b
    answer = day_list[days%7]

    return answer

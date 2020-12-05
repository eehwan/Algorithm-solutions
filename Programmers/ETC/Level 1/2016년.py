def solution(a, b):
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = b
    for i in range(a-1):
        total_days += month[i]
    return day[(3+total_days)%7]

# import datetime
# def solution(a,b):
#     return ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'][datetime.date(2016,a,b).weekday()]

print(solution(5, 24))

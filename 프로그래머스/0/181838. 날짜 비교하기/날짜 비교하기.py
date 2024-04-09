def solution(date1, date2):
    answer = 0
    date_1 = str(date1[0]) + str(date1[1]) + str(date1[2])
    date_2 = str(date2[0]) + str(date2[1]) + str(date2[2])
    answer = 1 if int(date_1) < int(date_2) else 0
    return answer
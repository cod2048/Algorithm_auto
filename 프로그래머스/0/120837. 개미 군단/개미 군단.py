def solution(hp):
    ants = [5, 3, 1]
    strong_ant = hp // ants[0]
    normal_ant = (hp - (strong_ant * 5)) // ants[1]
    week_ant = hp - strong_ant * 5 - normal_ant * 3
    answer = strong_ant + normal_ant + week_ant
    return answer
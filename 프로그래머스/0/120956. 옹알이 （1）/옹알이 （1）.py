def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    result = []
    for babb in babbling:
        original = babb
        for word in words:
            babb = babb.replace(word, ",")
            new_babb = [s for s in babb.split(",") if s]
        if not new_babb:
            answer += 1
            
    return answer
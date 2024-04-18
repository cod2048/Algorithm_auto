def solution(id_pw, db):
    answer = "fail"
    if id_pw in db:
        answer = "login"
    else:
        for i in range(len(db)):
            if db[i][0] == id_pw[0]:
                answer = "wrong pw"
                break
    return answer
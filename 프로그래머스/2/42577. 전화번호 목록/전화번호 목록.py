def solution(phone_book):
    answer = True
    # 접두어이면 false
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
    return answer
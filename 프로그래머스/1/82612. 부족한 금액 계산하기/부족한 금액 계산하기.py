def solution(price, money, count):
    answer = 0
    total_price = 0
    
    for i in range(1, count + 1):
        total_price += price * i
        
    if money-total_price < 0:
        answer = abs(money-total_price)

    return answer
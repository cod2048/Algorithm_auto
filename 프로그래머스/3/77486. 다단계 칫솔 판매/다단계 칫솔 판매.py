def solution(enroll, referral, seller, amount):
    profit_dict = {name: 0 for name in enroll}  # 판매원별 수익을 추적하는 딕셔너리
    parent_dict = {}  # 판매원별 추천인을 추적하는 딕셔너리

    # 추천인 딕셔너리 생성
    for i in range(len(enroll)):
        parent_dict[enroll[i]] = referral[i]

    # 각 판매 이벤트 처리
    for i in range(len(seller)):
        current_seller = seller[i]
        profit = amount[i] * 100  # 판매로 인한 수익
        while current_seller != "-" and profit > 0:  # "-"는 회사를 의미
            # 수익의 10%를 계산
            parent_profit = profit // 10
            
            # 판매원에게 나머지 수익을 분배
            profit_dict[current_seller] += profit - parent_profit
            
            # 추천인으로 이동
            current_seller = parent_dict[current_seller]
            profit = parent_profit  # 추천인에게 분배할 수익으로 갱신

            # 분배할 금액이 1원 미만인 경우 분배 중단
            if profit < 1:
                break

    # 최종 수익 리스트 생성
    answer = [profit_dict[name] for name in enroll]
    return answer

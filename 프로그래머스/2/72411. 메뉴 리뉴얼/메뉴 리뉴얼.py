from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    
    for course_size in course:
        combinations_list = []
        for order in orders:
            # 현재 주문에서 가능한 모든 조합을 찾아 리스트에 추가
            combinations_list += combinations(sorted(order), course_size)
        
        # 모든 조합의 등장 횟수를 계산
        combination_counts = Counter(combinations_list)
        
        # 가장 많이 등장한 조합의 등장 횟수가 2 이상인 경우에만 결과에 추가
        if combination_counts:
            max_count = max(combination_counts.values())
            if max_count >= 2:
                for comb, count in combination_counts.items():
                    if count == max_count:
                        answer.append(''.join(comb))
    
    return sorted(answer)

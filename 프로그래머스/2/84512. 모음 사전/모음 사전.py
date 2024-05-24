def solution(word):
    chars = ['A', 'E', 'I', 'O', 'U']
    result = 0

    def recursive_count(current_word):
        nonlocal result
        result += 1
        
        # 현재 단어가 목표 단어와 같으면 True 반환
        if current_word == word:
            return True
        
        # 현재 단어 길이가 5이면 False 반환 (더 이상 재귀하지 않음)
        if len(current_word) == 5:
            return False
        
        # 각 문자를 현재 단어에 추가하여 재귀 호출
        for char in chars:
            if recursive_count(current_word + char):
                return True
        
        return False
    
    # 빈 문자열로 재귀 시작
    recursive_count('')
    
    return result - 1
def solution(n, words):
    answer = [0, 0]
    # 이전 단어의 끝 글자와 현재 단어의 첫 글자가 일치하지 않거나, 이미 사용된 적 잇다면 탈ㄹㄹㄹㄹ락
    next_letter = words[0][-1]
    word_list = set()
    word_list.add(words[0])
    
    for i in range(1, len(words)):
        word = words[i]
        if word not in word_list and word[0] == next_letter:
            word_list.add(word)
            next_letter = word[-1]
        else:
            answer = [(i % n) + 1, (i // n) + 1]
            break
    
    return answer
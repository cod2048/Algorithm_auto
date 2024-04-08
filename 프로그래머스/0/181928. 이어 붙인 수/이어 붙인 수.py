def solution(num_list):
    answer = 0
    odd_num = ""
    even_num = ""
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            odd_num += str(num_list[i])
        else:
            even_num += str(num_list[i])
    
    answer = int(odd_num) + int(even_num)
    return answer
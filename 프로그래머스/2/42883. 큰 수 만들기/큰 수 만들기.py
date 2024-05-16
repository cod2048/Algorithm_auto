#     numbers = []
    
#     for idx, num in enumerate(number):
#         numbers.append((idx, int(num)))
        
#     numbers.sort(key = lambda x : (x[1], x[0]), reverse = True)
    
#     for _ in range(k):
#         numbers.pop()
        
#     numbers.sort(key = lambda x : x[0])
        
#     for i in range(len(numbers)):
#         answer += str(numbers[i][1])

def solution(number, k):
    answer = ''
    stk = []
    
    for num in number:
        while stk and stk[-1] < num and k > 0:
            stk.pop()
            k -= 1
        stk.append(num)
    
    answer = "".join(stk)
    
    if answer == number:
        answer = answer[:-k]
            
    return answer
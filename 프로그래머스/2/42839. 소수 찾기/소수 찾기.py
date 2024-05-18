from itertools import permutations

def is_prime(number):
    if number == 1 or number == 0:
        return 0
    
    if number == 2:
        return 1
    
    result = 1
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            result = 0
            break
    
    return result

def solution(numbers):
    answer = 0
    result = []
    
    all_numbers = set()
    
    for length in range(1, len(numbers) + 1):
        for perm in permutations(numbers, length):
            number_str = ''.join(perm)
            all_numbers.add(int(number_str))
    
    for num in all_numbers:
        answer += is_prime(num)
    
    return answer
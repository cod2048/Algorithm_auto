def solution(nums):
    answer = 0
    unique_pokemon = set(nums)
    answer = min(len(nums)//2, len(unique_pokemon))
    return answer

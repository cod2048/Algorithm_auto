def solution(s):
    answer = []
    tmp = ''
    nums = dict()
    
    for t in s:
        if t.isdigit():
            tmp += t
        elif t == "}" or t == ",":
            if tmp:
                if tmp in nums:
                    nums[tmp] += 1
                else:
                    nums[tmp] = 1
                tmp = ""

    sorted_nums = sorted(nums.items(), key=lambda x: -x[1])
    
    answer = [int(num) for num, _ in sorted_nums]

    return answer

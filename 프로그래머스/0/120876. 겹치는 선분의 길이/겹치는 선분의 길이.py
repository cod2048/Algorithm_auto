def getOverlab(line1, line2):
    if line1[1] > line2[0]:
        if line1[1] > line2[1]:
            return line2
        else:
            return [line2[0], line1[1]]
    else:
        return []
    
def checkOverlab(lst, case):
    if case:
        for i in range(case[0], case[1]):
            lst[i] = True
            
    return lst

def solution(lines):
    answer = 0
    lines.sort()
    tmp = sum(lines, [])
    min_num = min(tmp)
    max_num = max(tmp)
    overlap = [False for _ in range(abs(max_num - min_num))]
    
    case1 = getOverlab(lines[0], lines[1])
    case2 = getOverlab(lines[1], lines[2])
    case3 = getOverlab(lines[0], lines[2])
    
    overlap = checkOverlab(overlap, case1)
    overlap = checkOverlab(overlap, case2)
    overlap = checkOverlab(overlap, case3)
    
    answer = overlap.count(True)
    return answer
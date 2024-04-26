def solution(line):
    # 2중 for문을 이용해 교점 구하기
    # 기울기를 구해서 기울기 같을 경우 예외처리
    # 배열에서 소수점이 있는 교점 제거
    # 배열에서 남은 값 중 x, y의 가장 큰 값을 구해 행, 열 크기 구하고 그 크기만큼 . 찍기
    # 배열에 남은 좌표에 해당하는 .은 *로 변경
    
    answer = []
    meets = set()
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            x1 = line[i][0]
            y1 = line[i][1]
            num1 = line[i][2]
            
            x2 = line[j][0]
            y2 = line[j][1]
            num2 = line[j][2]
            
            denom = ((x1*y2) - (y1*x2))
            mole_x = ((y1*num2) - (num1*y2))
            mole_y = ((num1*x2) - (x1*num2))
            
            if denom == 0:
                continue
            nx = mole_x / denom
            ny = mole_y / denom
            if nx == int(nx) and ny == int(ny):
                meets.add((int(nx), int(ny)))
                
    
    min_x = min(meet[0] for meet in meets) # -4
    max_x = max(meet[0] for meet in meets) # 4
    
    min_y = min(meet[1] for meet in meets)
    max_y = max(meet[1] for meet in meets)
    
    for i in range(max_y, min_y-1, -1):
        tmp = ""
        for j in range(min_x, max_x+1):
            if (j, i) in meets:
                tmp += "*"
            else:
                tmp += "."
        answer.append(tmp)
    
    
        
    return answer
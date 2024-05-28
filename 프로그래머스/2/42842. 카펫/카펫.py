def solution(brown, yellow):
    tiles = brown + yellow
    
    for height in range(3, tiles // 3 + 1):
        if tiles % height == 0:
            width = tiles / height
            
            if (width - 2) * (height - 2) == yellow:
                return [width, height]
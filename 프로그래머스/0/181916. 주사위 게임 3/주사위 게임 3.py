def solution(a, b, c, d):
    answer = 0
    dice_dic = {}
    
    for i in range(1, 7):
        dice_dic[i] = 0
    
    dice_dic[a] += 1
    dice_dic[b] += 1
    dice_dic[c] += 1
    dice_dic[d] += 1
    
    sorted_dice = sorted(dice_dic.items(), key = lambda x : x[1], reverse = True)
    print(sorted_dice)
    
    if sorted_dice[0][1] == 4:
        answer += 1111 * sorted_dice[0][0]
    elif sorted_dice[0][1] == 3:
        answer += ((10 * sorted_dice[0][0]) + sorted_dice[1][0]) ** 2
    elif sorted_dice[0][1] == 2:
        if sorted_dice[1][1] == 2:
            answer += (sorted_dice[0][0] + sorted_dice[1][0]) * abs(sorted_dice[0][0] - sorted_dice[1][0])
        else:
            answer += sorted_dice[1][0] * sorted_dice[2][0]
    else:
        answer += sorted_dice[0][0]    
    
    return answer
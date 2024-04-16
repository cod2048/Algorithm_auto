def solution(box, n):
    box_width = box[0] // n
    box_length = box[1] // n
    box_height = box[2] // n
    answer = box_width * box_length * box_height
    return answer
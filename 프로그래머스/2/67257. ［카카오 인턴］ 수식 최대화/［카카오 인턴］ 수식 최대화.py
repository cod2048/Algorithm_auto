from itertools import permutations
import re

def calc(tokens):
    num1, exp, num2 = tokens
    if exp == '+': return int(num1) + int(num2)
    elif exp == '*': return int(num1) * int(num2)
    else: return int(num1) - int(num2)

def solution(expression):
    answer = []
    operators = ["*", "+", "-"]
    for operator in permutations(operators):
        tmp = re.split(r'([-+*])', expression)
        for exp in operator:
            while exp in tmp:
                idx = tmp.index(exp)
                tmp[idx-1] = str(calc(tmp[idx-1:idx+2]))
                tmp[idx] = tmp[idx + 1] = ""
                tmp = [i for i in tmp if i]
                
        answer.append(abs(int(tmp[0])))
    return max(answer)
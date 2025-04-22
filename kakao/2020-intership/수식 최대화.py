import re
from itertools import permutations

def solution(expression):
    operators = [i for i in expression if not i.isdigit()]
    numbers = list(map(int, re.split('[\+\-\*]', expression)))
    operation_orders = permutations(set(operators))
    answers = []
    
    for operation_order in operation_orders:
        new_operators = operators[:]
        new_numbers = numbers[:]
        for order in operation_order:
            while len(list(filter(lambda x: x == order, new_operators))):
                for i, operator in enumerate(new_operators):
                    if (operator == order):
                        new_operator = new_operators.pop(i)
                        if (new_operator == '+'):
                            new_numbers[i] += new_numbers.pop(i+1)
                        if (new_operator == '-'):
                            new_numbers[i] -= new_numbers.pop(i+1)
                        if (new_operator == '*'):
                            new_numbers[i] *= new_numbers.pop(i+1)
                        break
        answers.append(abs(new_numbers[0]))
    return max(answers)

if __name__ == '__main__':
    samples = [
        ("100-200*300-500+20",),      # 60420
        ("50*6-3*2",),                # 300
    ]
    results = [solution(*x) for x in samples]
    print(*results, sep='\n')

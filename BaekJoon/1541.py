import sys

formula = sys.stdin.readline()
split_minus = formula.split('-')
total_minus = []
for i in split_minus:
    split_plus = i.split('+')
    total_plus = 0
    for j in split_plus:
        total_plus+=int(j)
    total_minus.append(total_plus)

result = 2*total_minus[0]
for k in total_minus:
    result-=k
print(result)

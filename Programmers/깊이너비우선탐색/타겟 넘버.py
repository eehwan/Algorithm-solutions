def func(k:list, results:list = [0]):
    if k == []:
        return results
    temp = k.pop()
    new_results = []
    for result in results:
        new_results.append(result+temp)
        new_results.append(result-temp)
    return func(k, new_results)

def solution(numbers, target):
    remain = sum(numbers) - target
    if remain < 0:
        return 0
    if remain == 0:
        return 1
    return func(numbers).count(target)

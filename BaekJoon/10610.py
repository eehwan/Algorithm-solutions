import sys

num = list(sys.stdin.readline())[0:-1]
def mulOf30(_list):
    if not('0' in _list):
        return -1
    sum =0
    for i in _list:
        sum += int(i)
    if not(sum%3==0):
        return -1
    _list.sort(reverse=True)
    str = ""
    for j in _list:
        str+=j
    return int(str)

print(mulOf30(num))

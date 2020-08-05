n = int(input())    # n진법
t = int(input())    # 미리구할 갯수
m = int(input())    # 게임에 참가하는 인원
p = int(input())    # 튜브의 순서

def convert(n:int, value:int):  # return값은 str으로 나옴
    num_list="123456789ABCDE"
    q = value//n
    r = value%n
    if q==0:
        return num_list[r]
    else:
        return convert(n,q) + num_list[r]

tube_list =[]
for i in range(m*t):
    for j in list(convert(n, i)):
        tube_list.append(j)

print(tube_list,len(tube_list))
for i in range(t):
    print(tube_list[p-1 + m*i],end='')

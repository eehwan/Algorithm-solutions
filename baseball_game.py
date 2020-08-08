import sys
import random

min_lev = 1
max_lev = 5

level = int(input(f"난이도를 설정해주세요({min_lev}~{max_lev}) :\n"))
while (level>max_lev and level<min_lev):
    level = int(input("난이도를 다시 설정해주세요(1~10) :\n"))

answer=[]
for _ in range(level):
    answer.append(str(random.randint(1,9)))
#answer#
print("".join(answer))

input_nums=[]
while not(input_nums == answer):
    input_nums = list(str(input("입력 : ")))
    if len(input_nums)!=level:
        print("잘못 입력되었습니다")
        input_nums = list(str(input("입력 : ")))
    strike = 0
    ball = 0
    for index, value in enumerate(input_nums):
        if value in answer:
            ball+=1
            if value == answer[index]:
                strike+=1
    print(f"{strike} strike\n{ball} ball")

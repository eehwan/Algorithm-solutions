def solution(numbers):
    answer = []
    for num in numbers:
        if num%2 == 0:
            answer.append(num+1)
        else:
            base2 = list("0" + str(format(num , "b")))
            for i in range(len(base2)-1, -1, -1):
                if base2[i] == "0":
                    base2[i] = "1"
                    base2[i+1] = "0"
                    break
            base2 = "".join(base2)
            answer.append(int(base2, 2))
    return answer
# 비트연산자를 활용한 풀이
# def solution(numbers):
#     answer = []
#     for idx, val in enumerate(numbers):
#         answer.append(((val ^ (val+1)) >> 2) +val +1)

#     return answer

print(solution([3, 7]))
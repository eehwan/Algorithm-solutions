import copy
def solution(land):
    answer = land[0]
    for i in range(1, len(land)):
        new_answer = land[i]
        for j in range(4):
            temp = copy.deepcopy(answer)
            temp.pop(j)
            print(j , temp)
            print(land[i][j])
            new_answer[j] += max(temp)
            print(new_answer)
            print("----------------")
        answer = new_answer
        print(new_answer)
    return max(answer)

print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
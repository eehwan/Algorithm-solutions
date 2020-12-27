def solution(A, B):
    A.sort(reverse=True); B.sort(reverse=True)
    print(A, B)
    answer = 0
    while A and B:
        a = A.pop(); b = B.pop()
        print(a,b)
        while B and a >= b:
            b = B.pop()
        if a < b: answer +=1; print("a: ", a, "b: ", b)
    return answer
def solution1(A, B):
    A.sort(); B.sort()
    answer = 0
    j = 0
    for i in range(len(A)):
        if A[j] < B[i]:
            answer = answer + 1
            j = j+1
    return answer

print(solution([1,2,3,4,5], [2,2,2,2,5]))

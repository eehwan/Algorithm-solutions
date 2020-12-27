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

print(solution([1,2,3,4,5], [2,2,2,2,5]))

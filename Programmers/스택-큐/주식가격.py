def solution(prices):
    length = len(prices)
    result=[0]*length
    for i in range(length):
        for j in range(i+1,length):
            result[i]+=1
            if prices[i]>prices[j]:
                break
    return result

test_case = \
[\
[1, 2, 3, 2, 3]
]
expected_value=\
[\
[4, 3, 1, 1, 0]
]

print(solution([1,2,3,2,3]))

def solution(clothes):
    count_clothes={}
    for value in clothes:
        wearing_part = value[1]
        if not(wearing_part in count_clothes.keys()):
            count_clothes[wearing_part] = 1
        else:
            count_clothes[wearing_part]+=1
    print(count_clothes)
    result = 1
    for i,(key,value) in enumerate(count_clothes.items()):
        print(f"{key},{value}")
        result*=value+1
    result-=1
    return result
# from collections import Counter
# from functools import reduce
#
# def solution(clothes):
#     cloth_counter = Counter([ctype for (_, ctype) in clothes])
#     print(cloth_counter)
#     return reduce(lambda a, b:  a+b+a*b, cloth_counter.values())

test_case = \
[\
[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]],\
[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]\
]
expected_value=\
[\
5,\
3\
]
result = solution(test_case[0])
print(result)

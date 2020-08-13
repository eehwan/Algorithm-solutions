def solution(phone_book):
    sort_phone_book = sorted(phone_book, key = len)
    print(sort_phone_book)
    for index,value in enumerate(sort_phone_book):
        len_phone_book = len(sort_phone_book)
        len_value = len(value)
        try:
            for i in range(index+1,len_phone_book):
                if sort_phone_book[i][:len_value] == value:
                    return False
        except:
            return True
    return True

# from itertools import combinations as comb
# def solution(phoneBook):
#     phoneBook.sort(key=len)
#     for num1,num2 in comb(phoneBook,2):
#         if num2.startswith(num1):
#             return False
#     return True

test_case = \
"""
["119", "97674223", "1195524421"]
["123", "456", "789"]
["12", "123", "1235", "567", "88"]
"""
expected_value=\
"""
false
true
false
"""
result = solution(["12345", "123", "11"])
print(result)

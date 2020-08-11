def solution(phone_book):
    sort_phone_book = sorted(phone_book, key = lambda x: len(x))
    print(sort_phone_book)
    for index,value in enumerate(sort_phone_book):
        len_phone_book = len(sort_phone_book)
        len_value = len(value)
        try:
            for i in range(index+1,len_phone_book):
                if sort_phone_book[i][:len_value] == value:
                    print(value)
                    return False
        except:
            return True
    return True

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

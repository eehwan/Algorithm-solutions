from collections import Counter

def solution(want, number, discount):
    want_counter = dict(zip(want, number))
    discount_counter = Counter()

    answer = 0
    for i, item in enumerate(discount):
        if (i >= 10):
            old_item = discount[i-10]
            if (discount_counter[old_item] == 1):
                discount_counter.pop(old_item)
            else:
                discount_counter[discount[i-10]] -= 1
        discount_counter[item] += 1
        
        if discount_counter == want_counter:
            answer += 1

    return answer

if __name__ == "__main__":
    test_cases = [
        [["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]],  # 3
        [["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]],                                                                        # 0
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")
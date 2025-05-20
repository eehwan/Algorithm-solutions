from collections import Counter
def solution(want, number, discount):
    want_counter = Counter({ key: value for key, value in zip(want, number) })
    discount_counter = Counter()
    answer = 0
    for i, v in enumerate(discount):
        if (i >= 10):
            discount_counter[discount[i-10]] -= 1
        discount_counter[v] += 1
        
        for j, key in enumerate(want_counter):
            if want_counter[key] > discount_counter[key]:
                break
            elif j == len(want_counter) - 1:
                answer += 1

    return answer

if __name__ == "__main__":
    test_cases = [
        [["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]],  # 3
        [["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]],                                                                        # 0
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")
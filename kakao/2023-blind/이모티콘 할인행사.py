from itertools import product

def solution(users, emoticons):
    discount_ratios = [10, 20, 30, 40]
    answer = (0, 0)

    for discounts in product(discount_ratios, repeat=len(emoticons)):
        curr_subscribers = 0
        curr_sales = 0

        for user_prefer_ratio, user_prefer_price in users:
            total = 0
            for emoticon, discount in zip(emoticons, discounts):
                if discount >= user_prefer_ratio:
                    total += emoticon * (100 - discount) / 100

            if total >= user_prefer_price:
                curr_subscribers += 1
            else:
                curr_sales += total

        answer = max(answer, (curr_subscribers, curr_sales))
    return [answer[0], int(answer[1])]

if __name__ == "__main__":
    test_cases = [
        [[[40, 10000], [25, 10000]], [7000, 9000]],                                                                         # [1, 5400]
        [[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]],   # [4, 13860]
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")
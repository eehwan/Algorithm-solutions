def solution(today, terms, privacies):
    def parse2day(y, m, d):
        return (y * 12 + m) * 28 + d
    
    today_total = parse2day(*map(int, today.split('.')))
    terms_dict = { x.split(' ')[0]: int(x.split(' ')[1]) for x in terms }
    
    answer = []
    for i, privacy in enumerate(privacies):
        curr_date, curr_type = privacy.split(' ')
        d = terms_dict[curr_type]
        a, b, c = map(int, curr_date.split('.'))

        curr_total = parse2day(a, b + d, c)
        if (today_total >= curr_total):
            answer.append(i + 1)
    return answer


if __name__ == "__main__":
    test_cases = [
        ["2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]],           # [1, 3]
        ["2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]],   # [1, 4, 5]
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")

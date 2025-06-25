def solution(today, terms, privacies):
    def date2days(y, m, d):
        return (y * 12 + m) * 28 + d
    
    today_in_days  = date2days(*map(int, today.split('.')))
    terms_dict = { x: int(y) for x, y in (term.split() for term in terms) }
    
    answer = []
    for i, privacy in enumerate(privacies):
        date_str, term_type  = privacy.split(' ')
        year, month, day = map(int, date_str.split('.'))
        valid_months = terms_dict[term_type ]

        expiry_in_days = date2days(year, month + valid_months, day)
        if (today_in_days >= expiry_in_days):
            answer.append(i + 1)
    return answer


if __name__ == "__main__":
    test_cases = [
        ["2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]],           # [1, 3]
        ["2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]],   # [1, 4, 5]
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")

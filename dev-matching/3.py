def solution(enroll, referral, seller, amount):
    incomeMap = {x: 0 for x in enroll}
    refer = {x: y for x, y in zip(enroll, referral)}
    for i, salesman in enumerate(seller):
        firstIncome = amount[i] * 100
        while salesman != "-":
            tax = int(firstIncome/10)
            incomeMap[salesman] += (firstIncome - tax)
            
            salesman = refer[salesman]
            firstIncome = tax
    return list(incomeMap.values())

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],\
     ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],\
         ["young", "john", "tod", "emily", "mary"],\
             [12, 4, 2, 5, 10]))
def solution(enroll, referral, seller, amount):
    incomeMap = {x: 0 for x in enroll}
    # print("incomeMap", incomeMap)
    for i, salesman in enumerate(seller):
        # print("-------------------------------")
        firstIncome = amount[i] * 100
        while salesman != "-":
            tax = int(firstIncome/10)
            # print(salesman, firstIncome, tax)
            incomeMap[salesman] += (firstIncome - tax)
            
            salesman = referral[enroll.index(salesman)]
            firstIncome = tax
            # print(salesman, firstIncome)
            # print(incomeMap)
    return list(incomeMap.values())

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],\
     ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],\
         ["young", "john", "tod", "emily", "mary"],\
             [12, 4, 2, 5, 10]))
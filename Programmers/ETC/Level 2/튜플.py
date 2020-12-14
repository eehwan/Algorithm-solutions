def solution(s):
    answer = []
    for i in sorted([x.replace("{","").replace("}","") for x in s[1:-1].split("},")], key = len):
        for j in i.split(","):
            if int(j) not in answer:
                answer.append(int(j))
    return answer

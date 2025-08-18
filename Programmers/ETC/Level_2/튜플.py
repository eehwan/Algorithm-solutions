def solution(s):
    answer = []
    for i in sorted([x.replace("{","").replace("}","") for x in s[1:-1].split("},")], key = len):
        for j in i.split(","):
            if int(j) not in answer:
                answer.append(int(j))
    return answer

import re
from collections import Counter
def solution1(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

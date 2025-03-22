def solution(n, t, m, p):
    def to_base(x, n):
        if x == 0:
            return '0'
        digits = '0123456789ABCDEF'
        res = ''
        while x > 0:
            res = digits[x % n] + res
            x //= n
        return res

    curr_num = 0
    curr_idx = 0
    answer = ''
    
    while len(answer) < t:
        for char in to_base(curr_num, n):
            if (curr_idx % m == p-1):
                answer += char
            curr_idx += 1
        curr_num += 1
    
    return answer[:t]

if __name__ == '__main__':
    samples = [
        (2, 4, 2, 1),       # "0111"
        (16, 16, 2, 1),     # "02468ACE11111111"
        (16, 16, 2, 2),     # "13579BDF01234567"
    ]
    results = [solution(n, t, m, p) for n, t, m, p in samples]
    print(*results, sep='\n')

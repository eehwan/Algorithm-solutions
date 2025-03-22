def to_base(x, n):
    if x == 0:
        return '0'
    
    digits = '0123456789ABCDEF'
    result = []

    while x > 0:
        result.append(digits[x % n])
        x //= n
    
    return ''.join(reversed(result))


def solution(n, t, m, p):
    result = []
    curr_num = 0
    idx = 0

    while len(result) < t:
        for char in to_base(curr_num, n):
            if idx % m == p - 1:
                result.append(char)
                if len(result) == t:
                    break
            idx += 1
        curr_num += 1
    
    return ''.join(result)


if __name__ == '__main__':
    samples = [
        (2, 4, 2, 1),       # "0111"
        (16, 16, 2, 1),     # "02468ACE11111111"
        (16, 16, 2, 2),     # "13579BDF01234567"
    ]
    results = [solution(*x) for x in samples]
    print(*results, sep='\n')

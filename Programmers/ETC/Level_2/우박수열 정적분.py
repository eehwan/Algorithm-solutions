def solution(k, ranges):
    sequence = [k]
    while sequence[-1] != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        sequence.append(k)

    n = len(sequence)
    areas = [(sequence[i] + sequence[i + 1]) / 2 for i in range(n - 1)]
    result = []

    for start, offset in ranges:
        end = n - 1 + offset
        if start > end:
            result.append(-1)
        else:
            result.append(sum(areas[start:end]))

    return result


if __name__ == '__main__':
    samples = [
        (5, [[0, 0], [0, -1], [2, -3], [3, -3]]),   # [33.0, 31.5, 0.0, -1.0]
        (3, [[0, 0], [1, -2], [3, -3]]),            # [47.0, 36.0, 12.0]
    ]
    results = [solution(*x) for x in samples]
    print(*results, sep='\n')

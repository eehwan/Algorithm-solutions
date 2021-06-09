def solution(dirs):
    command = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
    history = set()
    current = [0, 0]

    for dir in dirs:
        nx, ny = [a+b for a,b in zip(current, command[dir])]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            history.add((current[0], current[1], nx, ny))
            history.add((nx, ny, current[0], current[1]))
            current = [nx, ny]

    return len(history)//2

print(solution("ULURRDLLU"))
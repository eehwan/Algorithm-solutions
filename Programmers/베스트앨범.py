def solution(genres, plays):
    play_count = {}
    for i,value in enumerate(genres):
        if not(value in play_count.values()):
            play_count[value]=plays[i]
        else:
            play_count[value]+=plays[i]

    sort_play_count = sorted(play_count.items(),key=lambda x:x[1],reverse=True)
    return sort_play_count

test_case = \
[["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]]

expected_value=\
[4,1,3,0]
result = solution(test_case[0],test_case[1])
print(result)

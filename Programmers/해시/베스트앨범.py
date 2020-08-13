def solution(genres, plays):
    play_count = {genre:0 for genre in genres}
    for index,value in enumerate(genres):
        play_count[value]+=plays[index]
    sort_play_count = sorted(play_count.items(),key=lambda x:x[1],reverse=True)
    print(sort_play_count)

    new_list = []
    for i in zip(genres, plays,range(len(genres))):
        new_list.append(i)
    new_list.sort(key= lambda x: -x[1])
    print(new_list)

    result = []
    for genre in sort_play_count:
        top_genre = genre[0]
        count=0
        for index,value in enumerate(new_list):
            if count>=2:
                break
            if value[0]==top_genre:
                result.append(value[2])
                count+=1
    return result

# def solution(genres, plays):
#     answer = []
#     d = {e:[] for e in set(genres)}
#     for e in zip(genres, plays, range(len(plays))):
#         d[e[0]].append([e[1] , e[2]])
#     genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
#     for g in genreSort:
#         temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
#         answer += temp[:min(len(temp),2)]
#     return answer

test_case = \
[
["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500],
["classic","pop","classic","pop","classic","classic"] , [400,600,150,2500,500,500]
]
expected_value=\
[
[4,1,3,0],
[3,1,4,5]
]
result = solution(test_case[0],test_case[1])
print(result)

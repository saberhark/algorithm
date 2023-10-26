def solution1(genres, plays):
    answer = []

    dict = {}
    cnt = {}

    for i in range(len(plays)):
        if genres[i] in dict:
            dict[genres[i]][i] = plays[i]
        else :
            dict[genres[i]] = {
                i : plays[i]
            }
        cnt[genres[i]] = cnt.get(genres[i], 0) + plays[i]

    for (genre, count) in sorted(cnt.items(), reverse=True, key = lambda item:item[1]):
        for (k,v) in sorted(dict[genre].items(), reverse=True, key = lambda item:item[1])[0:2]:
            answer.append(k)

    return answer


def solution1(genres, plays):
    answer = []
    genre_and_idx_dict = {}
    genre_rank = {}

    for idx in range(0, len(genres)):
        genre = genres[idx]
        play = plays[idx]

        if genre_rank.get(genre) is None:
            genre_rank[genre] = 0
        genre_rank[genre] += play

        if genre_and_idx_dict.get(genre) is None:
            genre_and_idx_dict[genre] = []
        genre_and_idx_dict[genre].append(idx)


    for key in genre_and_idx_dict.keys():
        genre_and_idx_dict[key] = sorted(genre_and_idx_dict[key], key = lambda item:plays[item], reverse=True)[0:2]

    for key in dict(sorted(genre_rank.items(), key=lambda item:item[1], reverse=True)).keys():
        answer.extend(genre_and_idx_dict[key])

    return answer


print(solution1(["classic1", "pop2", "classic3", "classic4", "pop5"], [500, 600, 150, 800, 2500])) # 4 3 1 0 2
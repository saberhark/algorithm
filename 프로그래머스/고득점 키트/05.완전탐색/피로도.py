def solution(k, dungeons):
    answer = []
    dungeon_explore(k, dungeons, 0, answer)

    return max(answer)


# 모든 경우를 다 도는 재귀 N = len(dungeons) O(N!)
def dungeon_explore(rest_hp, dungeons, cnt, answer):

    for idx in range(len(dungeons)):
        tmp = dungeons[idx]
        tmp_hp = rest_hp
        tmp_cnt = cnt
        # 이미 시도한 던전이면 건너 뜀
        if not tmp:
            continue

        dungeons[idx] = False

        # 돌 수 있는 던전이면 돔
        if rest_hp >= tmp[0]:
            rest_hp -= tmp[1]
            cnt += 1
        rest_hp, cnt = dungeon_explore(rest_hp, dungeons, cnt, answer)

        if dungeons == [False] * len(dungeons):
            answer.append(cnt)
            cnt = 0

        # 배열 다시 원상 복귀
        dungeons[idx] = tmp
        cnt = tmp_cnt
        rest_hp = tmp_hp


    return rest_hp, cnt


print(solution(80, [[80,20],[50,40],[30,10]]))


dungeons=[[4,1],[12,3],[8,2],[16,4], [15,3]]
print(sorted(dungeons, key = lambda x : ((x[1]+x[0])/x[0], -x[1])))

[[15, 3], [16, 4], [12, 3], [8, 2], [4, 1]]
def solution(begin, target, words):
    if target not in words:
        return 0

    cur_words = [begin]
    cnt = 0

    while cur_words:
        tmp = []

        if target in cur_words:
            return cnt

        for cur_word in cur_words:
            idx = 0
            while idx < len(words):
                # 하나 차이면
                if check(words[idx], cur_word):
                    tmp.append(words.pop(idx))
                else:
                    idx += 1

        cur_words = tmp
        cnt += 1

    return 0


# 두 단어가 알파뱃 1개 차이 인지 확인
def check(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
        if cnt > 1:
            break
    return True if cnt <= 1 else False


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
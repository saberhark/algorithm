def solution1(participant, completion):
    answer = ''
    dic = {}
    for part in participant:
        dic[part] = dic.get(part, 0)+1
    for comp in completion:
        if dic[comp]-1 == 0:
            del(dic[comp])
        else:
            dic[comp] -= 1
    answer = dic.keys()

    for answer in list(answer):
        answer = answer
    return answer

# 시간 초과
def solution2(participants, completions):
    for completion in completions:
        participants.pop(participants.index(completion))

    return participants


def solution3(participants, completions):
    answer = ""
    participants_dict = {}
    for participant in participants:
        if participants_dict.get(participant) is None:
            participants_dict[participant] = 0
        participants_dict[participant] = participants_dict[participant] + 1

    for completion in completions:
        participants_dict[completion] = participants_dict[completion] - 1
        if participants_dict[completion] == 0:
            participants_dict.pop(completion)

    return list(participants_dict.keys())[0]


print(solution3(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
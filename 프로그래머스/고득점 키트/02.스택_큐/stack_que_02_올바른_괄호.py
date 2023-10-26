def solution(s):
    tmp = []
    for i in s:
        if i == "(":
            tmp.append(i)
        else:
            try:
                tmp.pop()
            except:
                return False
    return True if len(tmp) == 0 else False

print(solution("(()()))"))
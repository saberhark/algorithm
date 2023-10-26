def solution(word):
    answer = 0
    converted_words = [word_converter(i) for i in list(word)]
    weight = [625+125+25+5+1, 125+25+5+1, 25+5+1, 5+1, 1]
    l = len(word)

    return l + sum([converted_words[i]*weight[i] for i in range(l)])


def word_converter(word):
    if word == "A":
        return 0
    elif word == "E":
        return 1
    elif word == "I":
        return 2
    elif word == "O":
        return 3
    elif word == "U":
        return 4
    else:
        return -1

print(solution("AAAE"))
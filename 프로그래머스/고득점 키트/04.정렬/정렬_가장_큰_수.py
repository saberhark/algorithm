def solution(numbers):
    answer = ''
    for i in sorted(numbers, key=lambda item: str(item)*3, reverse=True):
        answer += str(i)
    return str(int(answer))

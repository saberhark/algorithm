def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, sum(numbers), target)


    return answer


def dfs(numbers, total, target):
    global answer
    # 맨 뒤부터 탐색
    peek = numbers.pop()
    # 남은 원소 총합
    total -= peek

    # 탐색 남아 있는 경우
    if numbers:
        # 마지막 원소를 뺏을 때
        if abs(target + peek) <= total:
            dfs(numbers, total, target + peek)
        # 마지막 원소를 더 했을 때
        if abs(target - peek) <= total:
            dfs(numbers, total, target - peek)
    # 탐색 완료
    else:
        # target에 도달했는지 체크
        if abs(target) == peek:
            answer += 1
            # 탐색 완료 후 배열 복구해줌

    numbers.append(peek)


print(solution([1,1,1,1], 0))
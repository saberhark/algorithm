def solution(arr):
    answer = [10]
    for i in arr:
        if answer[-1] != i:
            answer.append(i)
    answer.pop(0)
    return answer

print(solution([1, 1, 3, 3, 0, 1, 1]))
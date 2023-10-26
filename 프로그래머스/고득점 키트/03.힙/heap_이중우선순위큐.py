import heapq

def solution(operations):
    answer = []
    for operation in operations:
        if operation ==  "D 1":
            try:
                answer.pop(-1)
            finally:
                continue
        elif operation == "D -1":
            try:
                answer.pop(0)
            finally:
                continue
        else:
            answer.append(int(operation.split()[1]))
            answer.sort()

    if answer:
        answer = [answer[-1], answer[0]]
    else:
        answer = [0,0]

    return answer


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])) # 0, 0
print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])) # 333, -45


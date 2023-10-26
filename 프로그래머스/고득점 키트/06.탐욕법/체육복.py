import random
import time


def solution(n, lost, reserve):
    answer = 0
    total = [1 for i in range(n+2)]
    total[0] = 0
    total[n+1] = 0
    cnt = 0

    for i in lost:
        total[i] -= 1
    for i in reserve:
        total[i] += 1

    for i in range(1,n+1):
        if total[i] == 0:
            if total[i-1] == 2:
                total[i-1] -= 1
                total[i] += 1
                cnt += 1
            elif total[i+1] == 2:
                total[i+1] -= 1
                total[i] += 1
                cnt += 1
        elif (total[i] == 1) | (total[i] == 2):
            cnt += 1
        answer = cnt
    print(total)
    return answer


def solution1(n, lost, reserve):
    answer = 0
    students = [1] * n

    for i in lost:
        students[i-1] -= 1

    for i in reserve:
        students[i-1] += 1

    cnt = 0
    for idx, student in enumerate(students):
        if student == 0:
            if students[max(idx-1, 0)] == 2:
                students[max(idx - 1, 0)] -= 1
                students[idx] += 1
            elif students[min(idx + 1, len(students)-1)] == 2:
                students[min(idx + 1, len(students)-1)] -= 1
                students[idx] += 1

    for student in students:
        if student > 0:
            cnt += 1

    return cnt


def solution2(n, lost, reserve):
    answer = 0

    # 차집합
    lost_dif = [item for item in lost if item not in reserve]
    reserve_dif = [item for item in reserve if item not in lost]

    for item in lost_dif:
        for i in [-1, 1]:
            if item+i in reserve_dif:
                reserve_dif.remove(item+i)
                answer += 1
                break

    return n-len(lost_dif)+answer


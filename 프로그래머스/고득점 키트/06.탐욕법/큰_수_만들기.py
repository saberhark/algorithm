def solution1(number, k):
    answer = ''
    idx = 0

    while k>0:
        tmpIdx = 0
        maxNum = int(number[idx])
        #tmpIdx = number[idx: idx+k+1].index(max(number[idx: idx+k+1]))
        for i in range(k+1):
            if int(number[idx+i]) > maxNum:
                maxNum = int(number[idx+i])
                tmpIdx = i
            if maxNum == 9:
                break

        answer += number[idx+tmpIdx]
        idx += tmpIdx+1
        k -= tmpIdx
        if len(number)-idx-1 < k:
            return answer

    answer += number[idx:]
    return answer


def solution(numbers, k):
    answer = ""
    numbers = [int(i) for i in numbers]
    idx = 0
    remove_idx = set()

    while idx < len(numbers):
        # max number 위치 찾아
        max_num = numbers[idx]
        max_idx = 0

        # 현재부터 k+1개 중에서 최댓값의 idx를 찾는다
        for i in range(k+1-len(remove_idx)):
            if max_num == 9:
                break
            if max_num < numbers[idx+i]:
                max_num = numbers[idx+i]
                max_idx = i

        # 최대값 앞의 숫자들을 모두 제거 리스트에 등록
        for i in range(idx, idx + max_idx):
            remove_idx.add(i)

        # max 다음 위치로 이동 (다 같은 경우는 1칸 이동됨)
        idx += max_idx+1

        # 남은 길이가 자를 길이와 같으면 종료함
        if len(numbers)-1-idx == k-len(remove_idx)-1:
            for i in range(idx, idx+k-len(remove_idx)):
                remove_idx.add(i)
            break

    for i in range(len(numbers)):
        if i not in remove_idx:
            answer += str(numbers[i])

    return answer


#solution("1924", 2)
#solution("1231234", 3)
print(solution("3211", 2))
print(solution("321", 2))
print(solution("1", 0))
print(solution("8887771234"*100001, 1000000))
print(solution("8"*1000000+"8", 1000000))
# print(solution("4177252841", 4))
# print(solution("11111111111111111", 4))
# print(solution("123456", 5))
# print(solution("100", 2))

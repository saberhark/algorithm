def solution(brown, yellow):
    answer = []
    for i in range(1,int((brown+yellow)**(1/2))):
        if (i)*(int(brown/2)-i-2) == yellow:
            answer = [int(brown / 2) - i, i + 2]
            answer.sort(reverse=True)
    return answer


def solution1(brown, yellow):
    answer = []
    for w, h in divisors(yellow):
        if w + h + w + h + 4 == brown:
            return [h+2, w+2]
    return answer


def divisors(number):
    div = []
    for i in range(int(number**0.5)):
        i += 1
        if number % i == 0:
           div.append([i, number//i]) # same as int(number/i) 속도는 더 빠름
    return div

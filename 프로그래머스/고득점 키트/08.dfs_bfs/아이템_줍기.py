def solution(rectangles, characterX, characterY, itemX, itemY):
    # 시계 방향 vs 반시계 방향 (케릭터=> item 시계 방향 vs item=> 케릭터 시계 방향)
    return min(solution1(rectangles, characterX, characterY, itemX, itemY), solution1(rectangles, itemX, itemY, characterX, characterY))


def solution1(rectangles, characterX, characterY, itemX, itemY):
    answer = 0
    # 한점은 최대 두 사각형만 교차 가능함
    while True:
        for rectangle in rectangles:
            # 점이 사각형 변위에 있고 사각형 내부가 아닐 경우 계속 반복
            while True:
                # result : None / x, y
                result = is_at_rectangle_line(rectangle, characterX, characterY)

                # 현재 점이 변위에 있으면 이동
                if result:
                    characterX += result[0]
                    characterY += result[1]
                    answer += 1
                    if characterX == itemX and characterY == itemY:
                        return answer

                    # 옮긴점이 다른 사각형 내부라면 다시 back하고 다른 사각형 변위에서 이동
                    # 변의 길이가 1이면 옮긴전이 내부가 아니고 변에 위치하는 경우가 생김, 하지만 사각형을 뚫고 지나가는 경우가 생김
                    # 해결법 =>  1씩 이동하지 않고 0.5만큼 이동해서 내부인지 확인하고 내부가 아니면 1을 이동한단 마인드
                    if is_in_rectangle(rectangles, characterX-(result[0]/2), characterY-(result[1]/2)):
                        # 케릭터 좌료 원상 복구
                        characterX -= result[0]
                        characterY -= result[1]
                        answer -= 1

                        # 다음 사각형으로 이동
                        break
                # 점이 사각형 변위에 없으면 다른 사각형 탐색
                else:
                    break

    return answer


# 점(x,y)이 다른 사각형 안에 있는지 판별
def is_in_rectangle(rectangles, x, y):
    for x1, y1, x2, y2 in rectangles:
        if is_at_rectangle_line([x1, y1, x2, y2], x, y):
            pass
        # 변위에 있지 않고 사각형 내부에 있을 경우
        elif x1 <= x <= x2 and y1 <= y <= y2:
            return True
    return False


# 점(x,y)이 사각형 변에 있는지 판별 후 이동할 좌표 return / None
# 무조건 시계 방향으로 탐색
def is_at_rectangle_line(rectangle, x, y):
    x1, y1, x2, y2 = rectangle

    if x == x1 and y1 <= y < y2:
        return 0, 1

    elif x == x2 and y1 < y <= y2:
        return 0, -1

    elif x1 < x <= x2 and y == y1:
        return -1, 0

    elif x1 <= x < x2 and y == y2:
        return 1, 0

    else:
        return None


print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)) # 17
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1)) # 11
print(solution([[1,1,5,7]], 1, 1, 4, 7)) # 9
print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10)) # 15
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3)) # 10
def solution(name):
    answer = 0
    tmp = [min(ord(i) - ord('A'), ord('Z') + 1 - ord(i)) for i in name]
    name = tmp
    pos = 0
    move = 0

    #오른쪽 방향 우선 그리디탐색
    while sum(name) != 0:
        answer += name[pos]
        name[pos] = 0
        move += 1

        if name[(pos+move) % len(name)] != 0:
            pos = (pos+move) % len(name)
            answer += move
            move = 0
            continue
        elif name[(pos-move) % len(name)] != 0:
            pos = (pos-move) % len(name)
            answer += move
            move = 0
            continue

    return answer


def solution1(name):
    answer = 0

    # 좌표들 간격 중 가장 큰 간격
    max_distance = 0
    prev_idx = 0
    max_inf = []

    cursor_cnt = [0]

    for idx, w in enumerate(name):
        if w != "A":
            # 알파뱃 count
            answer += move_from_a(w)

            # 커서 카운트
            # 간격이 가장 큰 경우 >> 가운데를 비운채로 좌, 우의 거리를 구해서 그 합을 구할것이기 때문에 비워질 부분이 가장 큰 케이스가 최소 거리이다.
            if idx - prev_idx > max_distance:
                max_distance = idx - prev_idx
                max_inf = [prev_idx, idx]
            prev_idx = idx

            # (역방향) 첫번째 A가 아닌곳을 찾아서 역방향으로 도는 케이스 // 최초 1회만 돔
            if len(cursor_cnt) == 1:
                cursor_cnt[0] = len(name) - idx
                cursor_cnt.append(idx)
            # (정방향) 마지막 A가 아닌곳을 찾아서 계산 // 마지막 한번만 구하면됨
            else:
                cursor_cnt[1] = idx

    if max_inf:
        cursor_cnt.append(len(name) - max_distance + min(len(name)-max_inf[1], max_inf[0]))

    return answer + min(cursor_cnt)


def move_from_a(ch):
    return min(ord(ch) - ord("A"), ord("Z") - ord(ch) + 1)


# target 까지 가는 방법 결정
def move_cursor(name_len, cursor_from, cursor_target):
    # from - target 사이 거리
    between = abs(cursor_from - cursor_target)
    return min(between, name_len - between)


# case 1
# 무지성 정방향이 나은 경우 >> [-1]
# case 2
# 무지성 역방향이 나은 경우 >> [0]
# case 3
# 왔다 갔다하기


l = ["A"]*20
l[1] = "B"
l[5] = "B"
l[18] = "B"
a = ""
for i in l:
    a+=i

print(a)
print(solution1(a)) # 9
print(solution1("AAAA")) # 9
print(solution1("BAAA")) # 9
print(solution1("ABAA")) # 9
print(solution1("AABA")) # 9
print(solution1("AAAB")) # 9

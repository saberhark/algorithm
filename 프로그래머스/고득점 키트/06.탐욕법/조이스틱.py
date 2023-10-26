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
    cursors = []

    for idx, w in enumerate(name):
        if w != "A":
            answer += move_from_a(w)
            cursors.append(idx)

    idx = 0
    prev_cursor = 0
    while cursors:
        # 오른쪽 이동
        a = move_cursor(len(name), prev_cursor, cursors[idx])
        # 왼쪽 이동
        b = move_cursor(len(name), prev_cursor, cursors[idx-1])

        # 왼쪽 이동
        if a > b:
            prev_cursor = cursors.pop(idx - 1)
            answer += b
            idx -= 1
        # 오른쪽 이동
        else:
            prev_cursor = cursors.pop(idx)
            answer += a
    return answer


def move_from_a(ch):
    return min(ord(ch) - ord("A"), ord("Z") - ord(ch) + 1)


def move_cursor(name_len, cursor_from, cursor_target):
    return min(abs(cursor_from - cursor_target), -abs(cursor_from - cursor_target) + name_len)

print(solution1("JEROEN"))
print(solution1("JAN"))
print(solution1("AAB"))

print(move_from_a("J"))
print(move_from_a("E"))
print(move_from_a("R"))
print(move_from_a("O"))
print(move_from_a("E"))
print(move_from_a("N"))
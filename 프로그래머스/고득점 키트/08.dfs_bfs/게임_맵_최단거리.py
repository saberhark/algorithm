def solution1(maps):
    col = len(maps)
    row = len(maps[0])

    # 현재 위치
    cur_node = [(0,0)]

    # 여태까지 탐색한 노드
    prev_node = set()
    cnt = 1

    while cur_node:
        prev_node.update(cur_node)

        if (col-1, row-1) in prev_node:
            return cnt

        tmp = set()
        for i, j in cur_node:
            for move_i, move_j in [[-1,0],[1,0],[0,-1],[0,1]]:
                if 0 <= i+move_i < col and 0 <= j+move_j < row:
                    if maps[i+move_i][j+move_j] == 1 and (i+move_i, j+move_j) not in prev_node:
                        tmp.add((i+move_i, j+move_j))
        cnt += 1
        cur_node = tmp
    return -1

# 이전에 방문한 노드를 체크하지 말고 어차피 안갈거니까 그냥 0으로 바꿔서 벽으로 만들어버린다.
def solution(maps):
    col = len(maps)
    row = len(maps[0])

    # 현재 위치
    cur_node = [[0,0]]
    cnt = 1

    # 탐색할 노드가 없으면 종료하고 -1 return
    while cur_node:
        # 종료점이 0이 됐다는것은 이미 방문 했다는 것
        if maps[col-1][row-1] == 0:
            return cnt

        tmp = []
        for i, j in cur_node:
            for move_i, move_j in [[-1,0],[1,0],[0,-1],[0,1]]:
                if 0 <= i+move_i < col and 0 <= j+move_j < row:
                    if maps[i+move_i][j+move_j] == 1:
                        tmp.append([i+move_i, j+move_j])
                        maps[i+move_i][j+move_j] = 0
        cnt += 1
        cur_node = tmp
    return -1



#print(solution([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
#print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
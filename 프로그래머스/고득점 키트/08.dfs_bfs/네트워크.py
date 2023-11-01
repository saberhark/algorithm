def solution(n, computers):
    paths = []
    done = set()

    idx = 0
    while idx < n:
        # 처음 도달한 컴퓨터
        if idx not in done:
            paths.append(dfs(n, [], idx, computers))
            done.update(paths[-1])
        idx += 1

    return len(paths)


def dfs(n, path, idx, computers):
    links = computers[idx]

    for i in range(n):
        
        # idx+1부터 보면 안됨 역방향으로 갈 수도 있어서. path에 있는지 확인해야됨 안그러면 무한 루프에 빠짐
        if links[i] == 1 and i not in path:
            path.append(i)
            dfs(n, path, i, computers)

    return path


com = [[1, 1, 0],
       [1, 1, 0],
       [0, 0, 1]]

print(solution(3, com))
print(solution(4, [[1, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]))

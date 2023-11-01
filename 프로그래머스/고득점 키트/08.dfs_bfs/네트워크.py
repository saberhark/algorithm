def solution(n, computers):
    answer = 0
    paths = []

    return answer


def dfs(n, idx, computers):
    a = computers.pop(idx)

    for i in range(idx+1, n):
        if a[i] == 1:
            dfs(n, i, computers[idx ])

    # idx 가 1이면 1+1 부터 탐색하면 됨
    for i in range(idx+1, n):
        computers[i]

    return




com = [[1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]]


print(solution(3, com))
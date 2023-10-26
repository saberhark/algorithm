def solution(sizes):
    # 각 명함의 긴 부분의 최댓값
    long_max = 0
    # 각 명함의 짧은 부분의 최댓값
    short_max = 0

    for size in sizes:
        long_max = max(max(size), long_max)
        short_max = max(min(size), short_max)

    return long_max*short_max



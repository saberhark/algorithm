import random
import time

'''
heap pop = O(logN)

list pop = O(N)
이라서 solution1이 더 효율적이다
'''

def solution(jobs):
    time = 0
    work_time = 0
    length = len(jobs)


    jobs = sorted(jobs, key=lambda item: item[1])

    # O(N)
    while jobs:
        flag = True
        # O(N)
        for idx, job in enumerate(jobs):
            if job[0] <= time:
                # O(N)
                s, w = jobs.pop(idx)
                work_time += time - s + w
                time = time+w
                flag = False
                break
        if flag:
            time += 1

    return int(work_time/length)


def solution1(jobs):
    import heapq
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    # O(N)
    while i < len(jobs):
        # O(N)
        for j in jobs:
            if start < j[0] <= now:
                # O(logN)
                heapq.heappush(heap, [j[1],j[0]])
        if len(heap) > 0:
            # O(N)
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now += 1
    return int(answer / len(jobs))






random.seed(90)
for _ in range(10):
    st = time.time()
    for _ in range(100):
        jobs_len = random.randrange(500000)+1
        l = []
        for _ in range(jobs_len):
            s = random.randrange(1001)
            w = random.randrange(1000)+1
            l.append([s, w])
        solution(l)
    et = time.time()

    st1 = time.time()
    for _ in range(100):
        jobs_len = random.randrange(500000)+1
        l = []
        for _ in range(jobs_len):
            s = random.randrange(1001)
            w = random.randrange(1000)+1
            l.append([s, w])
        solution(l)
    et1 = time.time()

    print(et- st, et1-st1)
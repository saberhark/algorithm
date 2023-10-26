from queue import PriorityQueue
import heapq

# PriorityQueue는 thread safe를 유지하기 위해 속도가 느림
def solution1(scovilles, K):
    answer = 0
    heap = PriorityQueue()

    for scoville in scovilles:
        heap.put(scoville)

    while not heap.empty():
        min_scoville = heap.get()
        if min_scoville >= K:
            return answer

        if not heap.empty():
            answer += 1
            new_scoville = min_scoville + heap.get()*2
            heap.put(new_scoville)
        else:
            return -1
    return -1

# heapq를 써야 속도가 빠름
def solution2(scovilles, K):
    answer = 0
    heapq.heapify(scovilles)

    while len(scovilles) > 0:
        min_scoville = heapq.heappop(scovilles)
        if min_scoville >= K:
            return answer

        if len(scovilles) > 0:
            answer += 1
            new_scoville = min_scoville + heapq.heappop(scovilles)*2
            heapq.heappush(scovilles, new_scoville)
        else:
            return -1
    return -1


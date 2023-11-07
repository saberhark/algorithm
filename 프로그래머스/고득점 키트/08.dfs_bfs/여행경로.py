def solution(tickets):
    answer = ["ICN"]
    start_to_end = {}

    # 딕셔너리로 변환
    for start, end in sorted(tickets, key=lambda item : item[1]):
        if start_to_end.get(start):
            start_to_end[start].append(end)
        else:
            start_to_end[start] = [end]

    # 시작 지점이 정해졌 있음
    dfs(start_to_end, answer[0], answer)

    return answer


# 잘못된 길로 왔을 떄 다시 기어 올라 가야되는데 그러질 못함.
# 표시한곳 다시 보기
def dfs(ticket_dict, start, path):
    if ticket_dict.get(start):
        for _ in range(len(ticket_dict[start])):
            next_ticket = ticket_dict[start].pop(0)
            path.append(next_ticket)

            # 다음 행선지가 없는 출발지 제거
            if not ticket_dict[start]:
                ticket_dict.pop(start)

            # 다 탐색 했으면
            if not ticket_dict:
                return

            # 다음 탐색 시작
            dfs(ticket_dict, next_ticket, path)

            # 다 탐색 했으면
            if not ticket_dict:
                return

                # 완상 복구
            if ticket_dict.get(start):
                ticket_dict[start].append(next_ticket)
            else:
                ticket_dict[start] = [next_ticket]
        path.pop()
    else:
        # 잘못된 길로 왔을 때
        path.pop()

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))


def a(test_case, answer):
    s = solution(test_case)
    if s != answer:
        print(s)
    else:
        print("pass")

#a([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]],
#  ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])

a([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]],
  ["ICN", "AOO", "BOO", "COO", "DOO", "EOO", "DOO", "COO", "BOO", "AOO"])

a([["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "COO"], ["COO", "AOO"], ["BOO", "ZOO"]],
  ["ICN", "AOO", "COO", "AOO", "BOO", "ZOO"])

a([["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "BOO"], ["BOO", "AOO"], ["BOO", "FOO"], ["FOO", "COO"], ["COO", "ZOO"]],
  ["ICN", "AOO", "BOO", "AOO", "BOO", "FOO", "COO", "ZOO"])

a([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]],
  ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"])

a([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]], [
    "ICN", "AAA", "ICN", "AAA", "ICN", "AAA"])

a([["ICN", "BBB"],["ICN", "CCC"],["BBB", "CCC"],["CCC", "BBB"],["CCC", "ICN"]],
  ["ICN", "BBB", "CCC", "ICN", "CCC", "BBB"])

a([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]],
  ["ICN", "JFK", "HND", "IAD"])

a([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]],
  ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])

a([["ICN", "AOO"], ["ICN", "AOO"], ["AOO", "ICN"], ["AOO", "COO"]],
  ["ICN", "AOO", "ICN", "AOO", "COO"])

a([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]],
  ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"])

a([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]],
  ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"])
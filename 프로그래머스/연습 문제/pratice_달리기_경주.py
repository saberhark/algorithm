def solution(players, callings):
    answer = []
    players_dict = {}

    for idx, player in enumerate(players):
        players_dict[player] = idx


    for call in callings:
        idx = players_dict[call]
        players_dict[call] -= 1
        players_dict[players[idx-1]] += 1

        tmp = players[idx]
        players[idx] = players[idx - 1]
        players[idx - 1] = tmp

    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
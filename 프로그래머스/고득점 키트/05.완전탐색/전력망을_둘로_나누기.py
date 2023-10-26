def solution(n, wires):
    answer = []

    for idx, wire1 in enumerate(wires):
        tmp_wires = [i for i in wires]

        tmp_wires.pop(idx)

        tmp1 = set([wire1[0]])
        tmp2 = set([wire1[1]])

        idx = 0
        while tmp_wires:
            wire2 = tmp_wires[idx]

            if wire2[0] in tmp1 or wire2[1] in tmp1:
                tmp1.add(wire2[0])
                tmp1.add(wire2[1])
                tmp_wires.pop(idx)
            elif wire2[0] in tmp2 or wire2[1] in tmp2:
                tmp2.add(wire2[0])
                tmp2.add(wire2[1])
                tmp_wires.pop(idx)
            idx += 1

            if len(tmp_wires) <= idx:
                idx = 0

        if len(tmp2) == 0:
            tmp2.add(0)
        answer.append(max(len(tmp1)-len(tmp2), - len(tmp1)+len(tmp2)))

    return min(answer)



print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(9, [[1, 3], [3,4]]))

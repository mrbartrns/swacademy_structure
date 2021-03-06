# BOJ 20061
import copy
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def move(cur_block):
    """
    integrate 함수로부터 받아온 블럭들의 모음을 움직이게 하는 함수이다.
    @param cur_block: 블록들의 좌표를 모아둔 리스트
    @type cur_block: list
    @return: None
    """
    # color blue 0, 1
    location = copy.deepcopy(cur_block)
    while True:
        check = True
        for i in range(len(location)):
            y, x = location[i]
            ny, nx = y, x + 1
            if nx >= 10 or graph[ny][nx] > 0:
                check = False
                break

        if not check:
            for i in range(len(location)):
                y, x = location[i]
                graph[y][x] = 1
            break

        for i in range(len(location)):
            y, x = location[i]
            ny, nx = y, x + 1
            location[i] = [ny, nx]

    location = copy.deepcopy(cur_block)
    while True:
        check = True
        for i in range(len(location)):
            y, x = location[i]
            ny, nx = y + 1, x
            if ny >= 10 or graph[ny][nx] > 0:
                check = False
                break
        if not check:
            for i in range(len(location)):
                y, x = location[i]
                graph[y][x] = 1
            break
        for i in range(len(location)):
            y, x = location[i]
            ny, nx = y + 1, x
            location[i] = [ny, nx]


def integrate(que):
    """
    check if block nears another block and integrate them
    @param que: init blocks
    @type que: deque
    @return: integrated block
    @rtype: list
    """
    blocks = []
    t1, y, x = que.popleft()
    blocks.append([y, x])
    if t1 == 2:
        blocks.append([y, x + 1])
    elif t1 == 3:
        blocks.append([y + 1, x])
    return blocks


def check_score():
    # blue check, green check 한번에
    b_idx = -1
    g_idx = -1
    b_line = 0
    g_line = 0
    for i in range(9, 3, -1):
        if graph[i][0] and graph[i][1] and graph[i][2] and graph[i][3]:
            g_idx = max(g_idx, i)
            g_line += 1
        elif g_line > 0:
            break

    for i in range(9, 3, -1):
        if graph[0][i] and graph[1][i] and graph[2][i] and graph[3][i]:
            b_idx = max(b_idx, i)
            b_line += 1
        elif b_line > 0:
            break

    return [b_idx, b_line, g_idx, g_line]


def clear_line(graph, color_type, idx, line):
    for i in range(idx, 3 + line, -1):
        for j in range(4):
            # blue
            if color_type == 0:
                graph[j][i] = graph[j][i - line]
            # green
            else:
                graph[i][j] = graph[i - line][j]
    for i in range(4, 4 + line):
        for j in range(4):
            if color_type == 0:
                graph[j][i] = 0
            else:
                graph[i][j] = 0


if __name__ == "__main__":
    n = int(si())
    block = deque()
    graph = [[0 for _ in range(10)] for _ in range(10)]
    score = 0
    left = 0
    for _ in range(n):
        t, r, c = map(int, si().split())
        block.append((t, r, c))

    while block:
        integrated_block = integrate(block)
        move(integrated_block)
        b_idx, b_line, g_idx, g_line = check_score()
        score += b_line
        score += g_line
        if b_line > 0:
            clear_line(graph, 0, b_idx, b_line)
        if g_line > 0:
            clear_line(graph, 1, g_idx, g_line)

        # 연한 색의 칸에 블록이 있는지 없는지 체크
        b_line, g_line = 0, 0
        for i in range(5, 3, -1):
            for j in range(4):
                if graph[i][j] > 0:
                    g_line += 1
                    break
                if graph[j][i] > 0:
                    b_line += 1
                    break
        if b_line > 0:
            clear_line(graph, 0, 9, b_line)
        if g_line > 0:
            clear_line(graph, 1, 9, g_line)

        for i in range(10):
            for j in range(10):
                print(graph[i][j], end=" ")
            print()
        print()

    for i in range(10):
        for j in range(10):
            if graph[i][j] > 0:
                left += 1
            # print(graph[i][j], end=" ")
        # print()

    print(score)
    print(left)

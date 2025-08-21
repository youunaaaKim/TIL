import sys
sys.stdin = open('sdoku.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    # print(arr)

    valid = 1  # 유효하면 1, 아니면 0

    # 열과 행을 돌아가며 숫자 겹치는거 있는지 찾기
    # 행 검사
    for r in arr:
        c = [0] * 10
        for num in r:
            c[num] += 1
            if c[num] >= 2:
                valid = 0

    # 열 검사
    for col in zip(*arr):
        c = [0] * 10
        for num in col:
            c[num] += 1
            if c[num] >= 2:
                valid = 0

    # 3x3 검사
    for i in range(0, 9, 3): # i: 0, 3, 6 (행의 시작 인덱스)
        for j in range(0, 9, 3): # j: 0, 3, 6
            c = [0] * 10
            for x in range(3): # 3x3 구역의 행 탐색
                for y in range(3): # 3x3 구역의 열 탐색
                    num = arr[i + x][j + y] # 3x3 구역의 각 숫자
                    c[num] += 1
                    if c[num] >= 2:
                        valid = 0

    print(valid)

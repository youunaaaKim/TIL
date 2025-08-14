'''
숫자가 있는지 확인하기
델타로 돌면서 상하좌우 확인,
상자의 행렬 크기 확인
상자의 수를 카운트

모두 하나의 상자에 어팬드
'''


import sys
sys.stdin = open('04_input.txt')

#델타의 움직임 정의
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #print(arr)

    #초기 위치 찾기
    r,c = 0, 0
    #상자 찾기
    for r in range(N):
        for c in range(N):
            #0이 아니라면!!!!
            if arr[r][c] != 0:
                for i in range(4):
                    nr = r + dr[i]  # next_row
                    nc = c + dc[i]  # next_column

                    # [핵심] 벽(경계) 체크: 이동 후 위치가 배열 범위를 벗어나지 않는지 확인
                    if 0 <= nr < N and 0 <= nc < N:
                        print(arr[nr][nc], end=' ')







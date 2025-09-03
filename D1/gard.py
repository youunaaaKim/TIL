import sys
sys.stdin = open('gard_input.txt')

T = int(input())
for tc in range(1, T+1):
    N  = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    cou = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:

                for i in range(4):  # i: 0부터 3까지 → 4방향 반복
                    x, y = r, c  # 현재 위치 복사 (새로운 시작점)
                    for j in range(N):  # 거리만큼 반복
                        x += dr[i]  # i 방향으로 이동
                        y += dc[i]  # i 방향으로 이동
                        #print(i, j, x, y)  # 어떻게 바뀌는지 출력

                        if 0 <= x < N and 0 <= y < N : # 범위를 벗어나지 않으면서
                            if arr[x][y] == 0: # 0 이면
                                arr[x][y] = 3
                            elif arr[x][y] == 1:
                                break
                        else:
                            break

    for k in range(N):
        for h in range(N):
            if arr[k][h] == 0:
                cou +=1

    print(arr)
    print(f'#{tc} {cou}')


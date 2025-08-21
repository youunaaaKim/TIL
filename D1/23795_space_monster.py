import sys
sys.stdin = open('23795_space_monster.txt')

# 델타: 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input()) # 테스트케이스
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #print(arr)

    for r in range(N):
        for c in range(N):
            if arr[r][c] != 2:
                continue

            for i in range(4):  # 각 방향별 검사
                nr, nc = r, c  # 현재 위치 초기화

                # 각 칸은 0 (빈칸) 1(벽) 괴물(2) 중의 하나이다.
                # 범위 체크에서 범위 안에 있으면 while 반복, 한 방향으로 계속 전진하며 검사
                while 0 <= nr < N and 0 <= nc < N:
                    # 다음 위치 계산
                    # (이 부분 틀림)
                    # nr = r + dr[i]  # next_row  매번 기준 좌표 r에서 출발해서 한 칸 이동.
                    # nc = c + dc[i]  # next_column 반복할 때마다 처음 좌표에서 1칸만 보는 것.
                    nr += dr[i] # 이전에 이동한 좌표 nr에서 다시 다음 좌표로 계속 진행.
                    nc += dc[i]

                    # 이동 후 범위를 벗어나지 않는다면
                    if 0 <= nr < N and 0 <= nc < N:
                        # 벽을 만나면 해당 방향 종료(시야 차단)
                        if arr[nr][nc] == 1:
                            break
                        # 0이면 1로 변경 (괴물 직선 가시 구역)
                        if arr[nr][nc] == 0:
                            arr[nr][nc] = 1
                    else:
                        break

    #print(arr)
        # 살아남은 0의 개수 세기
    safe_count = sum(row.count(0) for row in arr)
    print(f'#{tc} {safe_count}')








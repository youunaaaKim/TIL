import sys
sys.stdin = open('23795_space_monster.txt')

# 델타: 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input()) # 테스트케이스
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)

    for r in range(N):
        for c in range(N):
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
                        # 괴물을 만난다면 (여기서 막힘 - > 어떻게 그 범위를 구해서 빼야할지 생각 못함)

                        if arr[nr][nc] == 2:  # 괴물 발견
                            # 벽을 만나기 전까지 0 -> 1로 바꾸기
                            # back_r, back_c = nr - dr[i], nc - dc[i] 이것은 한 칸만 바꿈
                            # while (back_r, back_c) != (r, c):
                            #     if arr[back_r][back_c] == 0:
                            #         arr[back_r][back_c] = 1
                            #     back_r -= dr[i]
                            #     back_c -= dc[i]
                            # break
                            forward_r, forward_c = nr, nc  # 괴물위치
                            while 0 <= forward_r < N and 0 <= forward_c < N: # 벽을 만날 때까지 계속 진행
                                if arr[forward_r][forward_c] == 1: # 벽을 만나면 종료
                                    break

                                if arr[forward_r][forward_c] == 0: # 빈칸(0)을 발견하면 1로 변경
                                    arr[forward_r][forward_c] = 1

                                forward_r += dr[i] # 계속 한 칸 더 진행
                                forward_c += dc[i]
                            break  # 한 번 괴물을 찾으면 다른 방향 확인을 멈춤

    print(arr)
        # 살아남은 0의 개수 세기
    safe_count = sum(row.count(0) for row in arr)
    print(safe_count)








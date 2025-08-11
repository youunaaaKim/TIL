import sys
sys.stdin = open('algo2_sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    # N: 행의 개수, M: 열의 개수
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 안전 구역 개수 초기화
    number_of_safe_area = 0

    # ↖ (-1,-1), ↗ (-1,+1), ↙ (+1,-1), ↘ (+1,+1)
    dr = [-1, -1, 1, 1]
    dc = [-1,  1, -1, 1]

    # 전체 N×M 배열을 순회
    for i in range(N):
        for j in range(M):
            # 현재 위치가 안전한지 여부
            safe = True

            # 4개의 대각선 방향을 검사
            for k in range(4):
                ni = i + dr[k]  # 이웃 셀의 행 좌표
                nj = j + dc[k]  # 이웃 셀의 열 좌표

                # 이웃 좌표가 배열 범위 안에 있을 때만 비교
                if 0 <= ni < N and 0 <= nj < M:
                    # 현재 값보다 크거나 같은 이웃이 있으면 안전하지 않음
                    if arr[ni][nj] > arr[i][j]:
                        safe = False
                        break

            # 모든 대각선 이웃보다 크면 안전 구역으로 카운트
            if safe:
                number_of_safe_area += 1

    # 결과 출력
    print(f'#{tc} {number_of_safe_area}')

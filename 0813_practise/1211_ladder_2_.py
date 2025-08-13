import sys

sys.stdin = open('1211_ladder_input.txt')

T = 10
for tc in range(1, T + 1):
    Test = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    best_steps = None
    best_start = -1

    for start_c in range(N): # 출발 위치 설정 0 행에서 1 찾기
        if arr[0][start_c] == 1:
            r,c =0, start_c
            steps = 0

            # 이동하는 동안 1의 갯수를 세는 리스트
            while r < N - 1:  # 마지막 줄 전까지만 반복
                # 왼쪽 먼저 확인
                if c > 0 and arr[r][c - 1] == 1:
                    while c > 0 and arr[r][c - 1] == 1:
                        c -= 1
                        steps += 1

                # 오른쪽 확인
                elif c < N - 1 and arr[r][c + 1] == 1:  # c가 0 - 99까지 봤을 때 오른쪽이 이동 가능한지, 오른쪽에 1 값이 있는지
                    while c < N - 1 and arr[r][c + 1] == 1:
                        c += 1
                        steps += 1
                # 한 줄 아래로 이동
                r += 1
                steps += 1

            # 최솟값 확인
            if arr[99][c] == 1:
                if best_steps is None or steps < best_steps or (steps == best_steps and start_c < best_start):
                    best_steps = steps
                    best_start = start_c

    print(f"#{tc} {best_start}")

    # # 마지막 행(99행)에서 현재 열이 1인 경우에만 비교
    # if arr[99][c] == 1:
    #
    #     # 아직 최소 이동 거리가 설정되지 않은 경우 → 첫 값으로 세팅
    #     if best_steps is None:
    #         best_steps = steps
    #         best_start = start_c
    #
    #     # 현재 경로가 기존 최소 거리보다 짧은 경우 → 갱신
    #     elif steps < best_steps:
    #         best_steps = steps
    #         best_start = start_c
    #
    #     # 현재 경로가 최소 거리와 동일하지만 시작 열이 더 왼쪽인 경우 → 갱신
    #     elif steps == best_steps and start_c < best_start:
    #         best_steps = steps
    #         best_start = start_c

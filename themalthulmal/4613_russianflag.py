# 위에서부터 흰색(W) 구간, 파란색(B) 구간, 빨간색(R) 구간이 각각 최소 한 줄 이상 존재해야 함

import sys
sys.stdin = open('4613_russianflag_input.txt')
T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 행의 개수 (깃발 높이), M: 열의 개수 (깃발 너비)
    arr = [list(input().strip()) for _ in range(N)]

    min_count = float('inf')  # 다시 칠해야 하는 최솟값
    best_arr = []  # 가장 적게 칠한 상태의 깃발 배열을 저장할 변수

    # 0 -> 3 전 줄 까지 흰색 가능 W
    # w + 1 부터 2전 줄 까지 파란색 가능 B
    # R 은 나머지

    # 가장 적은 칸을 바꾸는 조합 탐색
    # 흰색 구간 w는 0부터 최대 len(N-3)까지 가능
    for w in range(N - 2):
        # 파란색 b는 w+1부터 최대 len(N-2)까지 가능
        for b in range(w + 1, N - 1):
            count = 0  # 현재 조합(w, b)에서 칠해야 할 칸 수

            # 흰색 줄 : 0번 줄 ~ w번
            for row in range(0, w + 1):
                for col in range(M):
                    if arr[row][col] != 'W':  # 흰색이 아닌 경우
                        count += 1  # 다시 칠해야 하므로 +1

            # 파란색 줄 : w+1번 줄 - b번 줄
            for row in range(w + 1, b + 1):
                for col in range(M):
                    if arr[row][col] != 'B':  # 파란색이 아닌 경우
                        count += 1  # 다시 칠해야 하므로 +1

            # 빨간색 줄 : b+1번 줄 - N 줄
            for row in range(b + 1, N):
                for col in range(M):
                    if arr[row][col] != 'R':  # 빨간색이 아닌 경우
                        count += 1  # 다시 칠해야 하므로 +1

            # 지금까지 구한 count 값이 현재까지의 최소값보다 작다면
            if count < min_count:
                min_count = count       # 최솟값 갱신

    print(f"#{tc} {min_count}")
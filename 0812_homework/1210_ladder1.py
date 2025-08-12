import sys

sys.stdin = open('1210_ladder_input.txt')

T = 10
for tc in range(1, T + 1):
    Test = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    for start_c in range(N): # 출발 위치 설정 0 행에서 1 찾기 => 1번 막힘 : 시작 위치를 문제 잘 안읽고 0,0으로 고정함
        if arr[0][start_c] == 1:
            r = 0
            c = start_c

            while r < N - 1:  # 마지막 줄 전까지만 반복 => 두 번째 막힘 : 와일문을 써야하는 건 알겠는데 어떻게 이동시켜야하는지 모르겠었음
                # 왼쪽 먼저 확인
                if c > 0 and arr[r][c - 1] == 1:
                    while c > 0 and arr[r][c - 1] == 1: # 이거 어려움
                        c -= 1
                # 오른쪽 확인
                elif c < N - 1 and arr[r][c + 1] == 1:  # c가 0 - 99까지 봤을 때 오른쪽이 이동 가능한지, 오른쪽에 1 값이 있는지
                    while c < N - 1 and arr[r][c + 1] == 1:
                        c += 1
                # 한 줄 아래로 이동
                r += 1

            # r이 N-1에 도달 (마지막 줄) 목적지 도착 후 값이 2인지 확인
            if arr[r][c] == 2:
                print(f"#{tc} {start_c}")
                break
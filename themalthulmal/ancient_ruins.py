import sys
sys.stdin = open('ancient_ruins_inputtxt')
'''
각 칸이 선분의 시작점인지 먼저 판별
시작점이면 오른쪽(가로) 또는 아래(세로)로 연속된 1의 길이를 계산
모든 시작점에 대해 최댓값을 갱신한다.각 칸이 선분의 시작점인지 먼저 판별한 뒤(왼쪽이나 위가 0이거나 경계 밖),
시작점이면 오른쪽(가로) 또는 아래(세로)로 연속된 1의 길이를 센다.
모든 시작점에 대해 최댓값을 갱신한다.
'''
T = int(input())
#print(T)
for tc in range(1, T + 1):
    N, M = input().split()
    N = int(N)
    M = int(M)
    #print(N)
    #print(M)
    arr = [list(map(int, input().split())) for _ in range(N)]
    #print(arr)

    max_len = 0

    for r in range(N):
        for c in range(M):
            if arr[r][c] != 1:
                continue

            # 가로 선분 시작점인지 판단: 왼쪽이 경계 밖이거나 0
            if c == 0 or arr[r][c - 1] == 0:
                length = 0
                nc = c
                # 오른쪽으로 쭉 센다
                while nc < M and arr[r][nc] == 1:
                    length += 1
                    nc += 1
                if length >= 2:
                    if length > max_len:
                        max_len = length

            # 세로 선분 시작점인지 판단: 위쪽이 경계 밖이거나 0
            if r == 0 or arr[r - 1][c] == 0:
                length = 0
                nr = r
                # 아래로 쭉 센다
                while nr < N and arr[nr][c] == 1:
                    length += 1
                    nr += 1
                if length >= 2:           # 1×1 노이즈 제거
                    if length > max_len:
                        max_len = length

    print(f"#{tc} {max_len}")
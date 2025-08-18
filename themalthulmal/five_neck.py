'''
델타 탐색으로 경우의 수 3번 돌려서 찾기
'''

import sys
sys.stdin = open('five_neck.txt')

T = int(input())
#print(T)

# 8방향 델타: 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

for tc in range(1, T + 1):
    N = int(input())
    N = int(N)
    #print(N)
    #print(M)
    arr = [list(map(str, input().split())) for _ in range(N)]
    print(arr)

    found = False  # 오목 여부

    for r in range(N):
        for c in range(N):
            if arr[r][c] != 'o':
                continue
            for i in range(8):
                # 8방향 탐색
                for i in range(8):
                    cnt = 1  # 현재 돌 포함
                    nr, nc = r, c
                    for _ in range(4):  # 이미 1개 포함했으니 나머지 4개 확인
                        nr += dr[i]
                        nc += dc[i]
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':
                            cnt += 1
                        else:
                            break
                    if cnt >= 5:
                        found = True
                        break
                if found:
                    break
            if found:
                break



#===========================
import sys

sys.stdin = open('five_neck.txt')

T = int(input())

# 4방향만 검사 (우, 하, 우하, 좌하) — 반대방향은 중복이므로 생략
dr = [0, 1, 1, 1]
dc = [1, 0, 1, -1]


def has_five(r, c):
    """
    (r, c) 위치에서 시작해 4방향 중 하나로
    연속된 'o' 돌이 5개 이상 있는지 확인하는 함수
    """
    if arr[r][c] != 'o': # 현재 좌표에 돌이 없으면 검사 불필요
        return False

    for i in range(4):  # 각 방향별 검사
        nr, nc = r, c # 현재 위치 초기화
        cnt = 1  # 시작점 포함

        # 범위 체크에서 true면 무한반복, 한 방향으로 계속 전진하며 검사
        while True:
            # 1) 다음 위치 계산
            next_r = nr + dr[i]
            next_c = nc + dc[i]

            # 2) 범위 체크
            if not (0 <= next_r < N and 0 <= next_c < N):
                break

            # 3) 돌('o') 여부 확인
            if arr[next_r][next_c] == 'o':
                nr, nc = next_r, next_c
                cnt += 1
                if cnt >= 5:
                    return True
            else:
                break  # 돌이 아니면 종료

    return False


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]

    # any()로 전체 좌표를 돌며 하나라도 조건 만족하면 바로 True
    found = any(has_five(r, c) for r in range(N) for c in range(N))

    print(f"#{tc} {'YES' if found else 'NO'}")



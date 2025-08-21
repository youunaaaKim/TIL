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
        for c in range(N): # 처음에 베열을 돌면서
            if arr[r][c] == 2:  # 괴물 발견함
                for i in range(4):  # 괴물을 만났을 때 4방향으로 퍼뜨리기
                    nr = r + dr[i]
                    nc = c + dc[i]

                    while 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == 1:  # 벽이면 stop
                            break
                        if arr[nr][nc] == 0:
                            arr[nr][nc] = 1
                        nr += dr[i]
                        nc += dc[i]

    print(arr)
        # 살아남은 0의 개수 세기
    safe_count = sum(row.count(0) for row in arr)
    print(safe_count)








import sys

sys.stdin = open('01_input.txt')

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    #2차원 배열을 돌아야 함
    for r in range(N):
        for c in range(N):

            #4 => 상하좌우를 확인하기 위함
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                #상하좌우를 확인했을 때 절댓값을 구하기
                #벽이 아니라면
                if 0<= nr < N and 0 <= nc < N:
                    result += abs(arr[nr][nc] - arr[r][c])
                else:
                    continue
    print(result)
import sys
sys.stdin = open('18405_viros_input.txt')

T = int(input())



for tc in range(1, T+1):
    N, K = input().split()
    N = int(N) # N*N의 배열
    K = int(K) # 1번부터 K번까지의 바이러스 종류
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)

    S, X, Y = input().split()
    S = int(S)
    X = int(X)
    Y = int(Y)
    print(S)
    print(X, Y)

    # 시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식해 나간다.
    # 단, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다.
    # 또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.
    # S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오.
    # 만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.
    # 이 때 X와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1,1)에 해당한다.
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    for second in range(1, S+1):
        for viros in arr:

            nr, nc = r, c

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < N and 0 <= nc < N:
                    if arr[nr][nc] == 0:
                        arr[nr][nc] = viros










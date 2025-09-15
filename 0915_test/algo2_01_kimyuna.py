# import sys
# sys.stdin = open('algo2_sample_in.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #print(arr)
    # 최소한의 거리 카운트
    min_count = 0

    # 사과를 수확했는지 확인
    visited = [False] * N

    # 로봇은 창고에서 출발. 초기 위치 지정
    r, c = 0, 0

    # 이동한 충 거리
    d = 0

    # 좌표 설정
    for i in range(len(arr)): # 사과들을 돌면서
        nr = arr[i][0] # 사과의 위치를 지정
        nc = arr[i][1]

        d += (abs(r - arr[i][0]) + abs(c - arr[i][1])) # 현재 위치와 새로운 사과의 위치까지의 거리 구하기
        r, c = nr, nc # 사과를 수확한 위치로 현재 위치를 업데이트하고, 그 위치부터 다음 사과 찾기
        visited[i] = True # 사과를 수확했다면 True로 바꿔주기

        # 사과를 모두 수확하고 다시 돌아오기
        if all(apple == True for apple in visited): # 모든 사과를 수확했다면
            nr, nc = 0, 0 # 새로운 위치를 창고로 지정해주기
            d += (abs(r - nr) + abs(c-nc)) # 창고로 돌아왔을 때 까지 거리 업데이트하기

            min_count = d # 백트래킹을 하고 거리를 비교해야 함

    print(f'#{tc} {min_count}')
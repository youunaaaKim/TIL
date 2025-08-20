import sys
sys.stdin = open('traking_road.txt')
'''
지도에서 가장 높은 봉우리는 최대 5개
등산로는 가장 높은 봉우리에서 시작해야 함
등산로는 올라갈 수 있도록 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결
높이가 같은 곳 혹은 낮은 지형이나, 대각선 방향의 연결은 불가능

지도 지형의 높이는 1이상 20 이하의 정수
지형을 깎아 높이를 1보다 작게 만드는 것도 가능
가장 긴 등산로의 길이를 출력

[시나리오]
모든 위치에서 상하좌우 탐색해서 등산로 만들고, 리스트에 길이 저장하기
등산로 깎는 경우 따로 계산해서 리스트에 같이 저장하기
=> 어떻게 깎아?????????????????????

그리고 맥스 꺼내기



'''
# 델타: 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input()) # 테스트케이스
for tc in range(1, T+1):
    N, K = input().split()
    N = int(N) # 지도의 크기
    K = int(K) # 최대 공사 가능 깊이 K는 1 이상 5 이하의 정수
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(K)
    # print(arr)

    # 지도를 돌아가며 시작 위치 찾기, 델타 탐색
    for i in range(4):  # 각 방향별 검사
        nr, nc = r, c  # 현재 위치 초기화

        # 범위 체크에서 범위 안에 있으면 while 반복, 한 방향으로 계속 전진하며 검사
        while 0 <= next_r < N and 0 <= next_c < N:
            # 다음 위치 계산
            next_r = nr + dr[i]
            next_c = nc + dc[i]

            # 현재 숫자 기준으로 등산로 조성 가능한지 검사.
            # 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결이 되어야 한다
            # 가장 높은 수를 찾기
            if arr[next_r][next_c] == max(arr):
                # 현재위치와 델타탐색 위치의 차를 저장할 리스트
                chai = []
                chaichai = arr[nr][nc] - arr[next_r][next_c]
                # 등산로의 높이가 작거나 같으면 안됨
                if 0 < chaichai:
                    chai.append(chaichai)
                # 델타로 돌면서 차가 최소가 되는 위치 찾기
                min(chai) # ??????????????



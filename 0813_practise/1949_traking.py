import sys
sys.stdin = open('1949_Tracking_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = input().split() # N : 등산로를 위한 부지. K : 최대 공사 가능 깊이
    N = int(N)
    K = int(K)
    arr = [list(map(int, input().split())) for _ in range(N)]
    #print(arr)

    # 가장 높은 봉우리에서 시작하기
    # 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결이 되어야 한다.
    # 높이가 같은 곳, 혹은 낮은 지형이나 대각선 방향의 연결은 불가능하다.
    # 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.
    # 최대 공사 가능 길이 출력하기
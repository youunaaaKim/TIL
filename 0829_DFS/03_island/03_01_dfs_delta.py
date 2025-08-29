import sys

sys.stdin = open("input.txt")


# 입력 처리
N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]

# 방문 여부
visited = [[False] * M for _ in range(N)]

# 상, 하, 좌, 우, 대각선 4방향을 포함한 8방향 델타
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]



# DFS 함수 정의 (재귀 방식)
def dfs(r, c):
    '''
    깊이 우선 탐색(DFS)을 이용해 주어진 위치 (r, c)로부터 
    연결된 모든 땅(1) 영역을 방문 처리하는 함수

    8방향(상, 하, 좌, 우, 대각선 포함)으로 연결된 땅들을 
    재귀적으로 탐색하여 하나의 연결된 컴포넌트로 처리

    매개변수:
    r (int): 현재 탐색 중인 행 인덱스
    c (int): 현재 탐색 중인 열 인덱스

    반환값:
    visited 배열을 통해 상태가 저장됨
    '''
    # 현재 위치 방문 처리
    visited[r][c] = True

    # 현재 위치에서 8방향 이웃을 확인
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]

        # 다음 이동 위치가 격자 범위 안에 있고, 
        if 0 <= nr < N and 0 <= nc < M:
            # 그리고 그곳이 땅(1)이며, 아직 방문하지 않았다면
            if grid[nr][nc] == 1 and not visited[nr][nc]:
                # 재귀적으로 탐색을 이어감
                dfs(nr, nc)



# --- 메인 로직 ---
island_count = 0

# 모든 셀을 순회하며 DFS 실행
for i in range(N):
    for j in range(M):
        # 현재 위치가 땅(1)이고, 아직 방문하지 않았다면
        if grid[i][j] == 1 and not visited[i][j]:
            # 새로운 섬을 발견한 것이다
            island_count += 1
            # 이 섬과 연결된 모든 땅을 방문 처리 하기 위해 DFS 실행
            dfs(i, j)
            
# 최종 섬의 개수를 출력합니다.
print(island_count)

import sys
sys.stdin = open("4875_input_maze.txt")
# 상, 하, 좌, 우, 대각선 4방향을 포함한 8방향 델타
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# # DFS 함수 정의 (재귀 방식)
# def dfs(r, c):
#     '''
#     깊이 우선 탐색(DFS)을 이용해 주어진 위치 (r, c)로부터
#     연결된 모든 땅(1) 영역을 방문 처리하는 함수
#
#     8방향(상, 하, 좌, 우, 대각선 포함)으로 연결된 땅들을
#     재귀적으로 탐색하여 하나의 연결된 컴포넌트로 처리
#
#     매개변수:
#     r (int): 현재 탐색 중인 행 인덱스
#     c (int): 현재 탐색 중인 열 인덱스
#
#     반환값:
#     visited 배열을 통해 상태가 저장됨
#     '''
#     # 현재 위치 방문 처리
#     visited[r][c] = True
#
#     # 현재 위치에서 8방향 이웃을 확인
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#
#         # 다음 이동 위치가 격자 범위 안에 있고,
#         if (0 <= nr < N and 0 <= nc < N) and maze[nr][nc] == 0:
#
#             # 그리고 그곳이 땅(1)이며, 아직 방문하지 않았다면
#             if maze[nr][nc] == 0 and not visited[nr][nc]:
#                 # 재귀적으로 탐색을 이어감
#                 r, c = nr, nc   # 좌표값 업데이트
#                 dfs(nr, nc)
#
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     # 입력 처리
#     N = int(input())
#     maze = [list(map(int, input().strip())) for _ in range(N)]
#
#     # 방문 여부
#     visited = [[False] * N for _ in range(N)]
#

#
#     # --- 메인 로직 ---
#     # 모든 셀을 순회하며 DFS 실행
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2: # 2인 곳에서 탐색 시작
#                 # 이 섬과 연결된 모든 땅을 방문 처리 하기 위해 DFS 실행
#                 dfs(i, j)
#                 # 못찾는 조건 어떻게 하지?
#                 if maze[i][j] == 3:
#                     print(f'#{tc} 1')
#                 else:
#                     print(print(f'#{tc} 0'))


T = int(input())
for tc in range(1, T+1):
    # 입력 처리
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    # 방문 여부를 저장할 2차원 리스트 초기화 (모두 False로 시작)
    visited = [[False] * N for _ in range(N)]

    # 시작점(값이 2인 위치) 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j  # 시작점 좌표 저장

    # DFS를 위한 스택 초기화, 시작점을 스택에 넣음
    stack = [(r, c)]

    # 시작점 방문 처리
    visited[r][c] = True

    # 도착 여부를 저장할 변수 (기본값은 False)
    found = False

    # 스택이 빌 때까지 반복 - DFS
    while stack:
        # 현재 위치 꺼냄 - 후입선출
        r, c = stack.pop()

        # 4방향으로 이동 가능한지 확인
        for i in range(4):
            nr = r + dr[i]  # 새 행 위치
            nc = c + dc[i]  # 새 열 위치

            # 새 위치가 범위 내이고 아직 방문하지 않았을 때만 진행
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                # 길(0)인 경우
                if maze[nr][nc] == 0:
                    visited[nr][nc] = True  # 방문 표시
                    stack.append((nr, nc))  # 다음 탐색을 위해 스택에 추가

                # 도착점(3)을 찾은 경우
                elif maze[nr][nc] == 3:
                    found = True
                    break  # for문 탈출

        # while문 탈출
        if found:
            break

    # 결과 출력: 도착 가능하면 1, 아니면 0
    print(f'#{tc} {1 if found else 0}')




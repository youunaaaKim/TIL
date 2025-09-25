import sys
import heapq

sys.stdin = open('input.txt')

# 상, 하, 좌, 우 네 방향 이동 (델타 배열)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dijstra(N, grid):
    # 각 칸까지의 최소 비용을 기록할 2차원 배열
    # 처음에는 전부 무한대(inf)로 초기화
    costs = [[float('inf')] * N for _ in range(N)]

    # 우선순위 큐(힙) 생성
    # (현재까지의 비용, 행, 열) 형태로 저장
    # 시작점 (0,0)에서 비용은 0
    pq = [(0, 0, 0)]
    costs[0][0] = 0  # 시작점 비용은 0으로 설정

    # 다익스트라 알고리즘 시작
    while pq:
        # 현재 위치에서 비용이 가장 적은 노드를 꺼냄
        cost, r, c = heapq.heappop(pq)

        # 이미 더 적은 비용으로 방문한 적 있다면 무시
                     if cost > costs[r][c]:
            continue

        # 네 방향으로 이동 시도
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # 격자 범위 안에 있는지 확인
            if 0 <= nr < N and 0 <= nc < N:
                # 새로운 위치까지의 비용 = 지금까지 비용 + 새 칸의 값
                new_cost = cost + grid[nr][nc]

                # 만약 더 적은 비용으로 갈 수 있다면 갱신
                if new_cost < costs[nr][nc]:
                    costs[nr][nc] = new_cost
                    # 우선순위 큐에 새로운 경로 추가
                    heapq.heappush(pq, (new_cost, nr, nc))

    # 목적지 (N-1, N-1)까지 가는 최소 비용 반환
    return costs[N - 1][N - 1]

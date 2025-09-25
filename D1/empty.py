import sys
import heapq

sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dijstra(N, grid):
    costs = [[float('inf')] * N for _ in range(N)]

    pq = [(0,0,0)]
    costs[0][0] = 0

    while pq:
        cost, r, c = heapq.heappop(pq)

        if cost > costs[r][c]:
            continue
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0<= nr < N and 0<= nc < N:
                new_cost = cost + grid[nr][nc]

                if new_cost < costs[nr][nc]:
                    costs[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))
    return costs[N-1][N-1]















T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, list(input()))) for _ in range(N)]
    result = dijstra(N, data)
    print(f'#{tc} {result}')
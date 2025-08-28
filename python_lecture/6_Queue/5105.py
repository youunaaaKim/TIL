def bfs(i, j, N):
    # 준비
    visited = [[0]*N for _ in range(N)] # visited 생성
    q = []      # 큐생성
    q.append([i,j])# 시작점 인큐
    visited[i][j] = 1# 시작점 인큐 표시
    # 탐색
    while q:
        ti, tj = q.pop(0)   # 디큐
        if maze[ti][tj] == 3:   # visit(t)
            return visited[ti][tj] - 1 - 1 # 경로의 빈칸 수, -1 추가
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 미로내부고, 인접이고 벽이아니면,
            wi, wj = ti+di, tj+dj
            if 0<=wi<N and 0<=wj<N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])# 인큐
                visited[wi][wj] = visited[ti][tj] + 1   # 인큐 표시
    return 0

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

N = int(input())
maze = [list(map(int, input())) for _ in range(N)]
sti, stj = find_start(N)
ans = bfs(sti, stj, N)
print(ans)

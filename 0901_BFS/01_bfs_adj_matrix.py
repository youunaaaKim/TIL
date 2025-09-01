import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs_matrix(start_node, V, adj_matrix):
    """
    큐(deque)와 인접 행렬을 사용한 BFS
    """
    visited = [False] * (V + 1)  # 각 노드의 방문 여부를 기록
    path = []  # 최종 탐색 경로를 저장
    # BFS는 큐를 사용. 파이썬 list의 pop(0)은 비효율적이므로 deque 사용
    q = deque()

    # --- BFS 시작 처리 ---
    pass






    while q:
        current_node = q.popleft()
        path.append(current_node)

        for next_node in range
# --- 그래프 구성 ---
V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

# --- BFS 실행 ---
result_path = bfs_matrix(1, V, adj_matrix)
print(''.join(map(str, result_path)))

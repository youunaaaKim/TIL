import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs_list(start_node, V, adj_list):
    """
    큐(deque)와 인접 리스트를 사용한 BFS
    """
    visited = [False] * (V + 1)
    path = []
    q = deque()

    # --- BFS 시작 처리 ---
    pass


# --- 그래프 구성 ---
V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

# --- BFS 실행 ---
result_path = bfs_list(1, V, adj_list)
print(''.join(map(str, result_path)))

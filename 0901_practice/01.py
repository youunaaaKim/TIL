import sys
from collections import deque

sys.stdin = open('01_input.txt')


def bfs_list(start_node, adj_list, visited, path):
    """
    시작 노드(start_node)부터 그래프를 너비 우선 방식으로 탐색
    탐색 순서를 path 리스트에 저장
    탐색 중 방문한 노드는 visited 리스트를 통해 표시

    Args:
        start_node 탐색을 시작할 시작 노드 번호
        adj_list[i] 노드 i와 연결된 인접 노드들의 리스트
        visited 각 노드의 방문 여부를 저장하는 리스트
        path 탐색한 노드들의 순서를 저장할 리스트

    return:
        없음
    """
    queue = deque() # 큐 생성
    queue.append(start_node) # 시작 노드를 큐에 삽입
    visited[start_node] = True  # 시작 노드 방문 처리

    while queue: # 큐가 빌 때 까지 반복(모든 노드를 방문할 때 까지)
        current_node = queue.popleft() # 선입선출
        path.append(current_node) # 방문 노드를 탐색 경로에 추가

        # 현재 노드와 연결된 모든 인접 노드 순회
        for next_node in adj_list[current_node]:
            if not visited[next_node]: # 아직 방문하지 않은 노드라면
                visited[next_node] = True # 방문 처리
                queue.append(next_node)  # 다음 노드를 큐에 추가


# --- 그래프 구성 ---
V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

# --- BFS 실행 ---
visited = [False] * (V + 1) # 방문 여부를 저장하는 리스트
traversal_path = [] # BFS 순서를 저장할 리스트

bfs_list(1, adj_list, visited, traversal_path) # BFS 실행

print(''.join(map(str, traversal_path)))
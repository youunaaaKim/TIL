import sys

sys.stdin = open('input.txt')


def dfs_recursive_list(current_node, adj_list, visited, path):
    """
    인접 리스트와 재귀를 이용한 DFS
    """
    # 1. 현재 정점을 방문 처리 / 경로에 추가
    visited[current_node] = True
    path.append(current_node)

    # 2. 현재 정점에 인접한 노드들을 직접 순회
    # 인접 행렬 처럼 모든 노드를 확인할 필요 없이, 인접한 노드를 바로 탐색 가능
    for next_node in adj_list[current_node]:
        # 인접 정점이 아직 방문하지 않았다면 재귀호출 진행
        if not visited[next_node]:
            dfs_recursive_list(next_node, adj_list, visited, path)


# --- 그래프 구성 ---
# 정점과 간선의 개수를 입력받기
V, E = map(int, input().split())

#간선 정보를 리스트 하나로 입력받기
edge_data = list(map(int, input().split()))

# 1. V+1 * V+1 크기의 이차원 리스트를 0으로 초기화
adj_list = [[0] * (V + 1) for _ in range(V + 1)]

# 2. 간선 정보를 바탕으로 인접 리스트를 구성
for i in range(E):
    n1, n2 = edge_data[i * 2], edge_data[i * 2 + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)
# --- DFS 실행 ---
# 방문 여부를 기록할 리스트
visited = [False] * (V + 1)
# 전체 탐색 경로를 기록할 리스트
result_path = [] # 전체 탐색 경로를 저장할 리스트


# 1번 노드부터 시작
dfs_recursive_list(1, adj_list, visited, result_path)

# 전체 탐색 경로 출력
print(result_path)
# --- 모든 노드를 시작점으로 시도하는 경우 (그래프가 비연결일 경우를 대비) ---
# 그래프가 {1-2}, {3-4} 처럼 나뉘어 있다면 3, 4번 노드는 절대 방문하지 못함
# for i in range(1, V + 1):
#     if not visited[i]:
#         # i번 노드를 시작으로 하는 DFS 수행
#         dfs_recursive_matrix(i, adj_matrix, visited, traversal_path)
# print(''.join(map(str, traversal_path)))
# --- DFS 실행 ---

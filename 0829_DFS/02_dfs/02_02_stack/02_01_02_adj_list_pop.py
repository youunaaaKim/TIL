import sys

sys.stdin = open('input.txt')


def DFS_stack_pop_style(start):
    """
    스택과 인접 리스트를 사용한 DFS (Pop 시점 방문 처리)
    """
    visited = [False] * (V + 1)  # 방문 여부 기록
    stack = [start]  # 시작 노드를 스택에 추가
    result_path = []  # 탐색 경로 기록

    # 탐색 시작 (스택이 빌 때까지)
    while stack:
        current_node = stack.pop()

        # 이 정점을 방문한 적이 있는지 확인
        if not visited[current_node]:
            # 방문한 적이 없다면 방문 처리 및 경로 추가
            visited[current_node] = True
            result_path.append(current_node)

            # 현재 정점과 인접한 정점들을 스택에 추가
            for next_node in adj_list[current_node]:
                if not visited[next_node]:
                    stack.append(next_node)

    return result_path


# --- 그래프 구성 ---
V, E = map(int, input().split())
data = list(map(int, input().split()))

# 인접 리스트(Adjacency List) 생성
adj_list = [[] for _ in range(V + 1)]

# 간선 정보 입력 (양방향)
for i in range(E):
    n1, n2 = data[2 * i], data[2 * i + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

# 방문 순서를 결정하기 위해, 인접 리스트를 각 노드별로 내림차순 정렬
# 내림차순 정렬해두면, 스택에서 pop할 때 작은 번호를 먼저 방문하도록 유도 가능
# 문제 요구사항(‘노드를 작은 번호부터 방문해야 한다’)과 스택의 LIFO 구조를 맞추기 위함
for i in range(1, V + 1):
    adj_list[i].sort(reverse=True)


# --- DFS 실행 ---
result_path = DFS_stack_pop_style(1)
print(''.join(map(str, result_path)))

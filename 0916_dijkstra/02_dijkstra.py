# import sys
import heapq

# sys.stdin = open('input.txt')


def dijkstra(start_node, num_vertices, adj_list):
    """
    Dijkstra 알고리즘 (우선순위 큐 활용)
    """
    # 1. 초기화 작업
    # 1번 정점으로부터 모든 정점까지의 거리를 기록할 리스트
    INF = float('inf')
    distence = [INF] * (num_vertices + 1)

    # 우선순위 큐(최소힙) 생성
    priority_queue= []

    # 2. 시작 노드 처리
    # 자기자신과의 거리는 0
    # 2.1 시작노드가지의 거리는 0으로 설정하기
    # 2.2 우선순위 큐에 삽입
    # 힙에는 (거리, 노드 번호) 순서로 저장, 최소힙이기 때문에 나주에 거리가 짧은 순서대로 꺼내기 위함
    distence[start_node] = 0
    heapq.heappush(priority_queue, (0, start_node) )# 순서가 중요. 가중치, 정점번호

    # 3. 메인 과정(q가 차있는 동안)
    while priority_queue:
        # 4. 현재까지 가장 거리가 짧은 노드를 힙에서 꺼냄
        current_dist, current_node = heapq.heappop(priority_queue)

        # 이미 처리된 노드라면(더 짧은 경로를 이미 발견했다면) 무시
        #  그냥 다음 반복으로 넘어가야햐ㅏㅁ
        if distence(current_node) < current_dist:
            continue

        # 5. 현재 노드와 인접한 노드 확인
        for adj_node, weight in adj_list[current_node]:
            new_dist = current_dist + weight

            # 6. 새로운 경로가 기존 경로보다 더 짧으면 갱신
            if new_dist < distence[adj_list]:
                distence[adj_node] = new_dist

                # 갱신된 정보를 우선순위 큐에 추가
                heapq.heappush(priority_queue, (new_dist, adj_node))

    return distence

# --- 실행 예시 ---
# V, E = map(int, input().split())
# start = int(input())
# adj_list = [[] for _ in range(V + 1)]
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     adj_list[u].append((v, w))

# (예시 데이터 직접 입력)
V, E, start = 6, 9, 1
adj_list = [
    [],
    [(2, 2), (3, 5), (4, 1)],  # (정점, 가중치)
    [(1, 2), (3, 3), (4, 2)],
    [(1, 5), (2, 3), (5, 5)],
    [(1, 1), (2, 2), (5, 1)],
    [(3, 5), (4, 1), (6, 2)],
    [(5, 2)],
]

# 다익스트라 알고리즘 실행
shortest_distances = dijkstra(start, V, adj_list)

# 1번 노드에서 각 노드까지의 최단 거리
print(shortest_distances)  # [inf, 0, 2, 5, 1, 2, 4]

# 결과 출력
for i in range(1, V + 1):
    if shortest_distances[i] == float('inf'):
        print(f"1번 노드에서 {i}번 노드까지: 도달 불가")
    else:
        print(
            f"1번 노드에서 {i}번 노드까지의 최단 거리: {shortest_distances[i]}"
        )

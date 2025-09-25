# import sys
import heapq

# sys.stdin = open('input.txt')


def dijkstra(start_node, num_vertices, adj_list):
    """
    Dijkstra 알고리즘 (우선순위 큐 활용)
    """
    # 1. 초기화
    # 모든 정점까지의 거리를 무한대(INF)로 초기화
    INF = float('inf')
    distance = [INF] * (num_vertices + 1)

    # 우선순위 큐(최소 힙) 생성
    priority_queue = []

    # 2. 시작 노드 처리
    # 시작 노드까지의 거리는 0으로 설정하고, 우선순위 큐에 삽입
    # 힙에는 (누적 거리, 노드 번호) 순서로 저장하여, 거리가 짧은 순으로 정렬되도록 함
    distance[start_node] = 0
    heapq.heappush(priority_queue, (0, start_node))

    # 3. 메인 루프: 큐가 빌 때까지 반복
    while priority_queue:
        # 4. 현재까지 가장 거리가 짧은 노드를 힙에서 꺼냄
        current_dist, current_node = heapq.heappop(priority_queue)

        # [가지치기] 만약 꺼낸 경로의 거리가 이미 기록된 최소거리보다 크다면,
        # 내가 과거에 이 현재 노드에 더 짧게 방문한 적이 있다면 더이상의 탐색은 무의미(더 탐색할 필요가 없는, 돌아온 경로이므로 무시)
        if distance[current_node] < current_dist:
            continue

        # 5. 현재 노드와 인접한 노드들을 확인
        for adj_node, weight in adj_list[current_node]:
            # 현재 정점을 거쳐 이웃 정점으로 가는 새로운 경로의 거리를 계산
            new_dist = current_dist + weight

            # 6. 간선 완화(Relaxation): 새로운 경로가 기존 경로보다 더 짧다면,
            if new_dist < distance[adj_node]:
                # 최소 거리를 갱신하고, 우선순위 큐에 새로운 경로 정보(거리, 정점)를 추가
                distance[adj_node] = new_dist
                heapq.heappush(priority_queue, (new_dist, adj_node))

    return distance
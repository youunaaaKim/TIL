import sys
import heapq

sys.stdin = open("5249_input.txt")
T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V: 마지막 노드 번호, E: 간선의 개수
    # 노드 번호가 0번부터 시작하므로 총 노드 수는 V + 1개

    # 각 노드에 대해 연결된 간선 정보를 저장할 리스트
    adj_list = [[] for _ in range(V + 1)]

    # E개의 간선 정보를 입력받아 리스트에 저장
    for _ in range(E):
        n1, n2, w = map(int, input().split())  # n1, n2: 연결된 노드, w: 가중치
        adj_list[n1].append((w, n2))  # n1에서 n2로 가는 간선 저장 (가중치, 도착노드)
        adj_list[n2].append((w, n1))  # n2에서 n1로 가는 간선 저장

    visited = [False] * (V + 1) # 방문 체크 배열: 해당 노드가 MST에 포함되었는지 여부를 저장
    min_heap = [(0, 0)] # 우선순위 큐 초기화
    mst_weight = 0 # 가중치 초기화
    count = 0 # 최소신장트리에 포함된 노드의 수를 세는 변수

    # 최소 힙이 빈공간이 아닌 동안 모든 노드를 선택하는 동안안 반복
    while min_heap and count < V + 1:
        weight, node = heapq.heappop(min_heap)  # 가중치가 가장 작은 간선을 선택

        if visited[node]:       # visited가 true면
            continue            # 무시하고 다음 간선으로 넘어감

        visited[node] = True    # 노드를 방문 처리 (최소신장트리에 포함시킴)
        mst_weight += weight    # 최소신장트리의 총 가중치에 현재 간선 가중치 추가
        count += 1              # 포함된 노드 개수 증가

        # 현재 노드에서 갈 수 있는 다른 노드들을 우선순위 큐에 추가
        for edge in adj_list[node]:
            if not visited[edge[1]]:        # 아직 최소신장트리에 포함되지 않은 노드만
                heapq.heappush(min_heap, edge)  # (가중치, 노드) 형태로 추가

    print(f"#{tc} {mst_weight}")
    print(adj_list)
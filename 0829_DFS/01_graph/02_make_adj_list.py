import sys

sys.stdin = open('input.txt')


# --- 그래프 구성 (인접 리스트) ---
# 정점과 간선의 개수를 입력받기
V, E = map(int, input().split())

#간선 정보를 리스트 하나로 입력받기
edge_data = list(map(int, input().split()))

# 1. V+1 크기의 리스트를 0으로 초기화
adj_list = [[] for _ in range(V + 1)]
# 간선의 개수만큼 반복하면서 2개씩 짝지어서 표기
for i in range(E):
    # 두 정점을 저장(n1과 n2는 서로 인접한 두 정점을 의미)
    n1, n2 = edge_data[2 * i], edge_data[2 * i + 1]

    # 인접 리스트에 간선 정보를 추가
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)  # 무향 그래프이기 때문에 반대 방향도 연결되었음을 표기

# --- 결과 확인 ---
for i in range(1, V + 1):
    print(f"정점 {i}의 인접 리스트: {adj_list[i]}")

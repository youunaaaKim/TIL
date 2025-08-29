import sys

sys.stdin = open('input.txt')


# --- 그래프 구성 (인접 행렬) ---
# 정점과 간선의 개수를 입력받기
V, E = map(int, input().split())

#간선 정보를 리스트 하나로 입력받기
edge_data = list(map(int, input().split()))

# 1. V+1 * V+1 크기의 이차원 리스트를 0으로 초기화
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

# 2. 간선 정보를 바탕으로 두 개씩 짝지어서 인접 행렬에 표기
# 총 표기 횟수는 간선의 개수 E와 동일
for i in range(E):
    # 정점의 번호를 저장(인접 행렬의 인덱스 값으로 쓰임)
    n1, n2 = edge_data[2 * i], edge_data[2 * i + 1]

    # 두 정점이 인접해있다는 것을 1로 표기
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1  # 무향 그래프이기 때문에 반대 방향도 연결되었음을 표기

# --- 결과 확인 ---
for row in adj_matrix:
    print(row)

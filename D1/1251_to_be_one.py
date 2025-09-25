# 모든 섬을 연결하는 최소 비용의 해저터널을 설계하라
import sys
sys.stdin = open('1251_input.txt')  # '1251_input.txt' 파일을 입력으로 사용

# --- 유니온 파인드 함수 정의 (Union-Find / Disjoint Set) ---

def find_set(x):
    """
    x가 속한 집합의 대표자(루트)를 찾는 함수
    - 경로 압축(Path Compression) 기법 사용
    """
    if parent[x] != x:  # x가 자기 자신이 대표자가 아니라면
        # 재귀적으로 부모를 따라가며 대표자를 찾고, x의 부모를 바로 대표자로 갱신
        parent[x] = find_set(parent[x])
    return parent[x]  # x의 최종 대표자를 반환

def union(x, y):
    """
    두 섬 x와 y를 같은 집합으로 합치는 함수
    - 이미 같은 집합이면 False 반환
    - 다른 집합이면 합치고 True 반환
    """
    root_x = find_set(x)  # x의 대표자 찾기
    root_y = find_set(y)  # y의 대표자 찾기

    if root_x != root_y:  # 서로 다른 집합이면 합치기 가능
        parent[root_y] = root_x  # y의 대표자를 x의 대표자로 연결
        return True  # 합치기에 성공했음을 의미
    return False  # 이미 같은 집합이면 합치지 않음

# --- 메인 로직 ---

T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T + 1):  # 각 테스트 케이스 반복
    N = int(input())  # 섬의 개수 입력
    x_coords = list(map(int, input().split()))  # 각 섬의 X좌표
    y_coords = list(map(int, input().split()))  # 각 섬의 Y좌표
    E = float(input())  # 환경 부담 세율

    # --- 모든 섬 쌍에 대해 "간선"과 "비용" 계산 ---
    edges = []  # (비용, 섬1, 섬2) 형태를 저장할 리스트
    for i in range(N):
        for j in range(i + 1, N):  # i < j인 쌍만 계산 (중복 방지)
            # 터널 길이 L^2 = (x1-x2)^2 + (y1-y2)^2
            # 환경 부담금 = E * L^2
            cost = E * ((x_coords[i] - x_coords[j]) ** 2 + (y_coords[i] - y_coords[j]) ** 2)
            edges.append((cost, i, j))  # 리스트에 추가

    edges.sort()  # 비용이 작은 순서대로 정렬 (작은 비용부터 MST 구성)

    parent = list(range(N))  # 각 섬을 자기 자신 대표자로 초기화 (make_set)

    mst_cost = 0  # MST(최소 신장 트리) 전체 비용
    edge_count = 0  # MST에 선택된 간선 개수

    # --- 크루스칼 알고리즘으로 MST 구성 ---
    for cost, n1, n2 in edges:
        if union(n1, n2):  # 사이클이 생기지 않으면 간선 선택
            mst_cost += cost  # 비용 누적
            edge_count += 1  # 간선 개수 증가

            if edge_count == N - 1:  # MST는 N-1개의 간선이면 완성
                break

    # --- 출력 ---
    # 소수 첫째 자리에서 반올림하여 정수로 출력
    print(f'#{tc} {round(mst_cost)}')

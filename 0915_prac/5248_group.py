import sys
sys.stdin = open('5248_input.txt')

# 부모 노드 찾기 (경로 압축)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 집합을 합치기
def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 총 사람 수, M: 신청서 개수
    arr = list(map(int, input().split()))  # M쌍의 신청서 (2*M 길이의 리스트)

    parent = [i for i in range(N + 1)]  # 1번부터 N번까지, 자기 자신이 부모로 시작

    # M개의 쌍을 이용해 union 수행
    for i in range(0, len(arr), 2):
        a, b = arr[i], arr[i + 1]
        union(a, b)

    # 모든 사람의 대표 노드를 찾아서 집합 수 세기
    group_set = set()
    for i in range(1, N + 1):
        group_set.add(find(i))

    print(f"#{tc} {len(group_set)}")

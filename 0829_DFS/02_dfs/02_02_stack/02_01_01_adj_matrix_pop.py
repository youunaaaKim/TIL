import sys

sys.stdin = open('input.txt')


def DFS_stack_pop_style(start):
    '''
    스택을 활용한 DFS (Pop 시점 방문 처리)
    '''
    pass


# --- 그래프 구성 ---
V, E = map(int, input().split())
data = list(map(int, input().split()))

# 인접행렬(Adjacency Matrix) 생성
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

# 간선 정보를 인접행렬에 기록 (양방향)
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

# --- DFS 실행 ---
result_path = DFS_stack_pop_style(1)
print(''.join(map(str, result_path)))

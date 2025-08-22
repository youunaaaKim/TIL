'''
 주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램을 만드시오.
 서브 트리의 노드 수 : 자기 자신 + 왼쪽 자식 + 오른쪽 자식
'''

import sys

sys.stdin = open('02_input.txt')

# 전위 순회(Preorder Traversal)
# 루트 노드를 먼저 방문하고, 왼쪽 자식 노드를 방문하고, 오른쪽 자식 노드를 방문하는 순서
def preorder(node):
    global count
    # node가 0이 아닐 때만(유효한 노드일 때만) 실행
    if node != 0:
        # 1. 나 먼저 처리 (V)
        #print(node, end=' ')
        # 2. 왼쪽 자식으로 이동 (L)
        preorder(left[node])
        # 3. 오른쪽 자식으로 이동 (R)
        preorder(right[node])
        # 자기 자신 포함
        count += 1

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split()) # E : 간선(부모-자식 쌍)의 개수 | N : 서브트리의 루트 노드 번호
    edge = list(map(int, input().split()))  # E개의 부모 자식 노드 번호 쌍이 주어진다.

    # 트리 구조 저장 배열 준비
    # 노드 번호를 인덱스로 사용하기 위해 E+2 크기로 생성
    # 노드 수는 간선 수보다 1 많기 때문에 E+2
    left = [0] * (E + 2)
    right = [0] * (E + 2)

    #간선 정보를 순회하며 트리 만들기
    for i in range(E):
        parent, child = edge[i*2], edge[i*2+1] # 부모와 자식 리스트 만들기

        if left[parent] == 0: # 부모 자리에 왼쪽이 비어있으면 왼쪽 자식으로 저장
            left[parent] = child
        else:
            right[parent] = child

    # print('왼', left)
    # print('오', right)
    count = 0
    # 루트 노드 N부터 시작하여 순회하며 노드 수 세기
    preorder(N)
    print(f'#{tc} {count}')






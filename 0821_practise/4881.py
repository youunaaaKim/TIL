import sys
from itertools import permutations  # N×N 배열에서 행과 열이 겹치지 않게 하나씩 선택

sys.stdin = open('4881_input')
'''
NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 
단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 합 구하는 리스트
    results = []
    # 각 행에 대해 겹치지 않는 열 하나씩을 매칭하는 모든 방법을 다 시도
    for perm in permutations(range(N)):  # 열 인덱스 순열 생성
        selected = [arr[i][perm[i]] for i in range(N)] # i는 행 인덱스, perm[i]는 열 인덱스
        result = sum(selected)
        results.append(result)
    print(f'#{tc} {min(results)}')
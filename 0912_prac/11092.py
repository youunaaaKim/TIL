'''
주어진 정수 리스트를 순회하며 최대/최소값을 가진 인덱스을 갱신
최소가 어러개일 때는 먼저 나오는 위치
최대가 여러개일 때는 나중에 나오는 위치
최대/ 최소 위치의 차이를 절댓값으로 출력
'''

import sys
sys.stdin = open('11092.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 최대/최소값의 인덱스 0으로 초기화
    max_i = 0
    min_i = 0

    for i in range(1, N):
        if arr[max_i] <= arr[i]:
            max_i = i
        if arr[min_i] > arr[i]:
            min_i = i
    result = abs(max_i - min_i)
    print(f'#{tc} {result}')
'''
상자들이 쌓여있는 방이 있다.
방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때, 낙차가 가장 큰 상자를 구하여 그 낙차를 리턴하는 프로그램을 작성하시오.
중력은 회전이 완료된 후 적용된다.
상자들은 모두 왼쪽 벽면에 붙여 쌓여 있는 상태로, 2차원의 형태를 이루며 벽에서 떨어져 쌓일 수는 없다.
방의 가로 길이는 항상 100이며, 세로 길이도 항상 100이다.
즉, 상자는 최소 0, 최대 100 높이로 쌓을 수 있다.
'''

import sys
sys.stdin = open('gravity_input')

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 가로 길이
    arr = list(map(int, input().split()))
    print(arr)

    many_zero = [] # 낙차 저장
    for i in range(N):
        diff = 0
        for n in arr[i + 1:]:  # 현재 상자 arr[i] 오른쪽에 있는 모든 상자 높이 확인 # 생각을 구현하는 부분에서 막힘
            if arr[i] > n:  # 현재 상자 높이가 비교 대상보다 크면
                diff += 1  # 낙차 가능 칸 하나 추가
        many_zero.append(diff)

    max_result = max(many_zero)
    print(f'#{tc} {max_result}')



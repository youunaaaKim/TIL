from itertools import combinations
import sys
sys.stdin = open('1486_input.txt')  # '1251_input.txt' 파일을 입력으로 사용

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N명의 점원 / B: 탑의 높이
    # B 이상의 높이의 탑 중에 가장 낮은 탑
    arr = list(map(int, input().split()))  # 점원의 키
    # print(arr)
    cha = 99
    # N 명의 점원의 키의 합 만큼 탑을 쌓을 수 있음
    # B 랑 가장 가까운 높이의 탑을 구해야 함

    result = 99
    for r in range(N + 1):
        # combinations를 사용하여 크기가 r인 모든 부분집합을 생성합니다.
        for subset in combinations(arr, r):
            # 현재 부분집합의 합을 계산합니다.
            current_sum = sum(subset)
            if current_sum >= M:
                answer = current_sum - M
                if result > answer:
                    result = answer

    print(f'#{tc} {result}')
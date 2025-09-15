import sys

sys.stdin = open('1206_view_sample_input.txt')

# 총 10개의 테스트 케이스
T = 10

for test_case in range(1, T + 1):
    # 건물의 개수 N
    N = int(input())
    # 건물의 높이 height
    height = list(map(int, input().split()))

    # 조망권이 확보된 세대의 수를 담을 변수 초기화
    count = 0

    # 범위 내 인덱스를 찾음
    for i in range(2, N - 2):  # 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않으므로 range(2, N - 2)

        # 현재 건물의 위치
        current_building = height[i]

        # 다섯 개의 건물 중 가장 높은 건물의 값 (높이) 초기화
        highest_building = 0

        # 제한된 범위 내 건물 간의 높이 비교
        # 현재 위치의 건물 포함, 총 다섯 개의 건물 중 가장 높은 건물을 찾는다
        for idx in range(i - 2, i + 3):  # i - 2에서 i + 2 까지 봐야하므로 range(i - 2, i + 3)
            if idx == i:  # 현재 건물일 경우
                continue  # 그냥 지나간다
            # 제한된 범위 내에 더 높은 건물이 있다면
            if highest_building < height[idx]:
                # 최댓값을 그 건물로 갱신
                highest_building = height[idx]

        # 현재 건물과 가장 높은 건물의 높이의 차를 구해서
        if current_building - highest_building > 0:
            # 그 값이 0보다 클 경우에만 세대 수를 카운팅 한다
            count += current_building - highest_building

    print(f'#{test_case} {count}')

'''
Scenario

최소 양 옆의 두 칸이 현재 빌딩의 높이보다 낮으면 됨
빌딩의 높이를 리스트로 받아 오니까, 인덱스를 활용할 수 있지 않을까?

현재 빌딩의 높이의 인덱스 i
양 옆 두 칸 빌딩의 높이의 인덱스 i-2, i-1, i+1, i+2

현재의 위치를 가장 높은 건물이라고 가정
'''
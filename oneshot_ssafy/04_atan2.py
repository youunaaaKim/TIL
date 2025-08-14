import math

# 기준점(A)의 좌표를 (0, 0)으로 설정
origin_x, origin_y = 0, 0

# 목표 지점들의 좌표 리스트
target_points = [(1, 2), (-2, -3), (3, 1), (-1, 4)]

# 각 목표 지점의 정보를 저장할 리스트
point_info_list = []

# 모든 목표 지점을 순회하며 정보 계산
for point_x, point_y in target_points:
    # 1. 거리 계산 (피타고라스의 정리)
    distance_from_origin = math.sqrt(
        (point_x - origin_x) ** 2 + (point_y - origin_y) ** 2
    )

    # 2. 각도 계산 (atan2 함수 활용)
    # atan2(y, x) 순서로 인자를 전달하여 정확한 각도(라디안) 계산
    angle_radians = math.atan2(point_y - origin_y, point_x - origin_x)
    # 라디안 단위를 도(degree) 단위로 변환
    angle_degrees = math.degrees(angle_radians)

    # 3. 계산된 정보를 리스트에 추가
    # 데이터 구조를 튜플로 명시적으로 표현
    point_data = (distance_from_origin, angle_degrees, (point_x, point_y))
    point_info_list.append(point_data)

# 4. 거리순으로 정렬
# 리스트의 각 튜플은 첫 번째 요소(거리)를 기준으로 자동 정렬됨
point_info_list.sort()

# 5. 두 번째로 가까운 점의 정보 선택
second_closest_point = point_info_list[1]

# 6. 결과 출력
distance = second_closest_point[0]
angle = second_closest_point[1]
point_coords = second_closest_point[2]

print(f'점의 위치: {point_coords}, 거리: {distance:.2f}, 각도: {angle:.2f}°')

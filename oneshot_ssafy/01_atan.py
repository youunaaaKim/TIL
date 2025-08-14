import math

# 기준점과 목표 지점의 좌표 정의
origin_point = (1, 1)
target_point = (2, 2)

# 1. 두 점 사이의 거리 계산 (피타고라스의 정리)
# x좌표의 차이와 y좌표의 차이를 각각 제곱하여 더한 후 제곱근을 구함
delta_x = target_point[0] - origin_point[0]
delta_y = target_point[1] - origin_point[1]
distance = math.sqrt(delta_x**2 + delta_y**2)

# 2. 두 점 사이의 각도 계산 (atan 함수 활용)
# atan 함수는 기울기(y변화량 / x변화량)를 인자로 받아 각도를 라디안으로 반환
# x좌표의 차이가 0일 경우 ZeroDivisionError가 발생할 수 있음
if delta_x == 0:
    # x의 변화가 없을 때 (수직선), 각도는 90도
    angle_radians = math.pi / 2
else:
    slope = delta_y / delta_x
    angle_radians = math.atan(slope)

# 라디안 단위를 도(degree) 단위로 변환
angle_degrees = math.degrees(angle_radians)

# 3. 결과 출력
print(f'거리: {distance:.2f}, 각도: {angle_degrees:.2f}°')

import math

# 기준점 (원점)
origin_x, origin_y = 0, 0

# 1사분면의 점 A
point_ax, point_ay = 2, 2
# 3사분면의 점 B
point_bx, point_by = -2, -2

# 점 A의 기울기와 각도 계산
slope_a = (point_ay - origin_y) / (point_ax - origin_x)  # 기울기: 2 / 2 = 1.0
angle_a = math.degrees(math.atan(slope_a))

# 점 B의 기울기와 각도 계산
slope_b = (point_by - origin_y) / (point_bx - origin_x)  # 기울기: -2 / -2 = 1.0
angle_b = math.degrees(math.atan(slope_b))

print(f'점 A ({point_ax}, {point_ay})의 각도: {angle_a:.2f}°')
print(f'점 B ({point_bx}, {point_by})의 각도: {angle_b:.2f}°')
print('\n문제점: 서로 정반대 방향인데 같은 각도가 나옵니다!')

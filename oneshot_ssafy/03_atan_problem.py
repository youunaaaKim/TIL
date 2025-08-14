import math

# 기준점 (원점)
origin_x, origin_y = 0, 0

# y축 위의 점 C
point_cx, point_cy = 0, 5

try:
    # 기울기 계산 시 5 / 0 이 되어 에러 발생
    slope_c = (point_cy - origin_y) / (point_cx - origin_x)
    angle_c = math.degrees(math.atan(slope_c))
except ZeroDivisionError:
    print('\n문제점: 수직 방향의 점은 기울기를 계산할 수 없어 에러가 발생합니다.')

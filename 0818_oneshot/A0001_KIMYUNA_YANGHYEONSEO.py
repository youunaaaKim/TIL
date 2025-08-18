import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '서울1반_김유나_양현서'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

# 어떤 전략으로 알고리즘을 구현했는지
#-----------------------------
    # 1. 목적구 선정
        # 선공(1)은 1번과 3번 공을, 후공(2)은 2번과 4번 공을 목표로 설정
        # 만약 모든 내 공이 빠졌다면, 8번 공(5번 인덱스)을 목표로 선택
    # 2. 가장 가까운 목적구 선택
        # 수구(흰 공)와 각 목적구 간의 최단 거리를 계산하여 가장 가까운 목적구를 선택
    # 3. 각도 및 파워 설정
        # 선택된 목적구를 향한 각도를 수학적으로 계산하고, 고정된 파워(100)로 공 침
# -----------------------------
    # 목적공 찾는 함수
    # ----------------------------
    # 목적구 판별/선택
    # ----------------------------
    def is_on_table(x, y):
        """좌표가 유효하면 True ([-1,-1]이면 포켓된 상태)."""
        return not (x == -1.0 and y == -1.0)

    def get_my_target_indices(order_val, balls_arr):
        """
        현재 플레이어(order)에 맞는 목적구 인덱스를 반환한다.
        선공(1) → 1, 3번
        후공(2) → 2, 4번
        내 공이 모두 빠졌으면 8번(5번 인덱스)을 반환
        """
        # order 값에 따라 내 목적구 후보 결정
        if order_val == 1:
            my_targets = [1, 3]
        else:
            my_targets = [2, 4]

        # 내 공 중 테이블 위에 남아 있는 것만 고르기
        alive = []
        for i in my_targets:
            x, y = balls_arr[i]
            if is_on_table(x, y):
                alive.append(i)

        # 내 공이 있으면 그 공들을 반환
        if len(alive) > 0:
            return alive

        # 내 공이 하나도 없으면 8번(인덱스 5)을 반환 (단, 테이블 위에 있을 때만)
        x8, y8 = balls_arr[5]
        if is_on_table(x8, y8):
            return [5]

        # 아무 것도 없으면 빈 리스트
        return []

    # ============================
    # 0) 기본 상수
    # ============================
    BALL_DIAMETER = 5.73
    POWER_FIXED = 100

    # ============================
    # 1) 유틸 함수
    # ============================
    def dist2(ax, ay, bx, by):
        """두 점 사이 거리의 제곱"""
        dx, dy = ax - bx, ay - by
        return dx * dx + dy * dy

    def cue_to_target_angle_deg(cue_x, cue_y, tar_x, tar_y):
        """
        일타싸피 각도 규칙에 맞춘 변환:
          - 수학각도: atan2(dy, dx) 결과는 라디안, 기준은 +x축, 반시계방향 증가
          - 일타싸피: 0°가 '위쪽(+y축)', 시계방향 증가
            변환식: degree = (90 - deg(atan2(dy, dx))) % 360
        """
        rad = math.atan2(tar_y - cue_y, tar_x - cue_x)  # 라디안
        deg = math.degrees(rad)  # 도(degree)
        aim = (90 - deg) % 360
        return aim

    # ============================
    # 2) 메인 로직 (심플 버전)
    #   - 가장 가까운 목적구를 고른 뒤 그 중심을 향해 조준
    #   - 충돌/파이프라인 미고려(진짜 간단 전략)
    # ============================
    def choose_nearest_target(cue_x, cue_y, balls_arr, cand_indices):
        """
        cand_indices로 주어진 후보 중에서 수구에 가장 가까운 목적구를 선택.
        """
        best_idx, best_d2 = None, float('inf')
        for i in cand_indices:
            x, y = balls_arr[i]
            if not is_on_table(x, y):
                continue
            dx, dy = cue_x - x, cue_y - y
            d2 = dx*dx + dy*dy
            if d2 < best_d2:
                best_d2 = d2
                best_idx = i
        return best_idx

    # ============================
    # 3) 실행부
    # ============================
    def decide_shot(balls_arr):
        # 3-1) 수구 좌표
        cue_x, cue_y = balls_arr[0]

        # 3-2) 선/후공 규칙으로 목적구 후보 뽑고, 그중 최단거리 선택
        cand = get_my_target_indices(order, balls_arr)
        idx = choose_nearest_target(cue_x, cue_y, balls_arr, cand)

        # 만약 남은 목적구가 없으면(이례적) 수구를 위쪽으로 보냄
        if idx is None:
            angle_local = 0.0  # 위쪽
            power_local = POWER_FIXED
            print(f'Power: {power_local}, Angle: {angle_local}')
            return angle_local, power_local

        tar_x, tar_y = balls_arr[idx]

        # 3-3) 각도 계산: atan2 + degrees
        angle_local = cue_to_target_angle_deg(cue_x, cue_y, tar_x, tar_y)

        # 3-4) 파워 고정
        power_local = POWER_FIXED

        # 일타싸피 전송(or 출력)
        print(f'Power: {power_local}, Angle: {angle_local}')
        return angle_local, power_local

    # === 호출 ===
    angle, power = decide_shot(balls)

    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    #
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')

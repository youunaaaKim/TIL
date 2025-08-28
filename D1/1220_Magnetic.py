import sys

sys.stdin = open('1220_input.txt')

# 1은 N극 (아래로 움직임), 2는 S극 (위로 움직임)

T = 10  # 총 테스트 케이스 수
for tc in range(1, T + 1):
    bayul = int(input())  # 배열 크기 (100)
    arr = [list(map(int, input().split())) for _ in range(bayul)]

    result = 0  # 교착 상태 개수

    # 각 열마다 확인
    for c in range(bayul):
        magnet = 0  # 현재 상태

        # 위에서부터 아래로 탐색
        for r in range(bayul):
            if arr[r][c] == 1:  # N극 발견
                magnet = 1  # 아래쪽 S극을 기다리는 상태
            elif arr[r][c] == 2:
                if magnet == 1:
                    result += 1  # N극 이후 S극 => 교착 상태 발생
                    magnet = 0  # 초기화 (한 쌍만 계산)

    print(f'#{tc} {result}')

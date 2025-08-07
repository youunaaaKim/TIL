import sys

sys.stdin = open('03_input.txt')


T = int(input())
#4방향 델타 정의(상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 풍선 하나를 터뜨렸을 때 얻을 수 있는 꽃가루의 최대값 저장 변수
    max_total = 0

    # 모든 풍선(위치)에 대해 반복
    for r in range(N):
        for c in range(M):
            power = arr[r][c]   # 현재 풍선에 든 꽃가루 수 (터뜨렸을 때 영향 범위)
            total = arr[r][c]   # 현재 위치 풍선의 꽃가루 수로 시작

            # 4방향으로 각각 power 만큼 이동하면서 터지는 풍선 누적
            for i in range(4):
                for j in range(1, power + 1):  # power 만큼 반복
                    nr = r + dr[i] * j
                    nc = c + dc[i] * j

                    # 만약 범위를 벗어나지 않았다면
                    if 0 <= nr < N and 0 <= nc < M:
                        total += arr[nr][nc]  # 꽃가루 수 누적

            # 최대값 갱신
            if total > max_total:
                max_total = total

    # 결과 출력
    print(f'#{tc} {max_total}')
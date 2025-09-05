import sys

sys.stdin = open('1588_minsum_input.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)


    def dfs(x, y, current_sum):
        """
        x와 y의 좌표를 받아서 시작점 부터 현재 위치까지의 합을 구하는 함수
        x, y: 현재 위치 좌표
        current_sum: 시작점부터 현재 위치까지의 합
        """
        global min_value

        # 가지치기: 현재 합이 이미 찾은 최소값보다 크면 더 이상 탐색 하지 않음(백트래킹)
        if current_sum >= min_value:
            return

        # 목표 지점 도착
        if x == N - 1 and y == N - 1:
            # 현재 합이 최소값보다 작으면 갱신
            if current_sum < min_value:
                min_value = current_sum
            return

        # 재귀 호출을 통해 다음 경로 탐색
        # 오른쪽 또는 아래로만 이동 가능
        for dx, dy in [(0, 1), (1, 0)]:  # 우, 하
            nx, ny = x + dx, y + dy
            # 배열 범위 확인
            if 0 <= nx < N and 0 <= ny < N:
                # 다음 위치로 이동하며 합 누적
                dfs(nx, ny, current_sum + arr[nx][ny])


    # 최소값을 저장할 변수, 충분히 큰 값으로 초기화
    min_value = float('inf')

    # (0, 0) 위치에서 시작, 시작점의 값으로 초기 합 설정
    dfs(0, 0, arr[0][0])

    print(f'#{tc} {min_value}')


import sys
sys.stdin = open('20230_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    answer = 0  # 전체 최대값 저장용

    for r in range(N):
        for c in range(M): # 2차원 배열을 돌면서
            k = arr[r][c] # 해당 위치의 풍선 숫자 확인
            result = k  # 현재 풍선을 터뜨릴 때 총 꽃가루 수
            for i in range(4):  # 4방향으로 돌면서
                for far in range(1, k+1): # 얼마나 멀리 갈지 생각해야 함
                    nr = r + dr[i] * far # 1*1, 1*2, 1*3 ... 각 방향대로 K 만큼 멀리 가기
                    nc = c + dc[i] * far

                    if 0 <= nr < N and 0 <= nc < M: # 벽 안의 범위에서
                        result += arr[nr][nc]  # 누적합 구하기
            if answer < result:
                answer = result  # 최대값 갱신

    print(f'#{tc} {answer}')

    # 막힌 부분 1 : 델타로 도는 것 까지는 이해했는데, 어떻게 풍선의 값만큼 멀리 가면서 합을 구해야할지 고민함.
    # 더해야 한다고 생각했는데 그러면 답이 안나왔음
        # => 델타로 돌면서 반복문을 하나 더 주어서, 얼마나 멀리 가야하는지 한 개씩 델타를 따라서 한 칸씩 K만큼 멀리 감 -> 곱하기

import sys
sys.stdin = open('1220_input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

T = 10
for tc in range(1, T+1):
    bayul = int(input())
    arr = [list(map(int, input().split())) for _ in range(bayul)]
    print(arr)

    # r이 0이면 N극과 가까움 / r이 bayul이면 S극과 가까움
    # 자성체들이 서로 충돌하여 테이블 위에 남아있는 교착 상태의 개수를 구하라.
    # 별일 없으면 0행 배열행 가서 없어지는데 중간에 숫자가 다른 자석 - 벽(다른 극자석이 있으면)살아남는다

    # 초기 위치 찾기
    r, c = 0, 0
    # 상자 찾기
    for r in range(bayul):
        for c in range(bayul):
            # 0이 아니라면!!!!
            if arr[r][c] != 0:
                for i in range(4):
                    nr = r + dr[i]  # next_row
                    nc = c + dc[i]  # next_column

                    # [핵심] 벽(경계) 체크: 이동 후 위치가 배열 범위를 벗어나지 않는지 확인
                    if 0 <= nr < bayul and 0 <= nc < bayul:
                        print(arr[nr][nc], end=' ')











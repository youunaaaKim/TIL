import sys

# sys.stdin = open('Sample_input.txt')
sys.stdin = open('portal.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # N 개의 방. 1번 부터 N 번까지 번호가 순서대로 붙어있음
    arr = list(map(int, input().split()))

    # 1번 방에는 1개의 포탈이 있고 포탈을 통해서 2번 방으로 이동할 수 있다.
    # 2번부터 N-1번까지 방 각각에는 포탈이 2개 있는데,
    # 처음 그 방을 들어갔을 땐 반드시 왼쪽의 인덱스 값으로, 이후 같은 방을 방문했을 때 오른쪽으로 한 칸
    # 1번 방에서 시작하여 게임이 끝날 때까지 몇 번 포탈을 사용하게 되는지 계산

    # 빈 배열 생성
    visit = [0] * (N + 1) # 방문 여부를 표시하기 위한 배열
    count = 0 # 포털을 이용한 횟수
    where_am_i = 1 # 현재 방 위치를 확인하기 -> 1번 방 부터 시작

    # 2번 방 부터 끝 까지
    while where_am_i < N:
        if where_am_i == 1: # 1번 위치에 있으면 무조건 한 칸 오른쪽
            where_am_i = 2
            count += 1
            visit[1] = 1
        if visit[where_am_i] == 0: # 방문한 적 없으면
            visit[where_am_i] = 1 # 해당 위치의 방문 여부를 1로 변경
            where_am_i = arr[where_am_i - 1]  # 해당 위치의 배열의 값(왼쪽 포털 방 번호)로 이동
            count += 1
        if visit[where_am_i] == 1: # 방문한 곳이면
            where_am_i += 1 # 한 칸 오른쪽으로
            count +=1

    print(f'#{tc} {count}')

    # 오늘은 지피티를 쓰지 않았습니다!
    # 막혔던 부분 1. 포문으로 1부터 N까지 돌면서 계산하려고 했었는데 포문으로 돌게 되면, 조건에 상관 없이 옆으로 한 칸씩 이동하게 되었음
    # 막혔던 부분 2. 처음 위치에선 무조건 한 칸 옆으로 가야한다는 조건에 1번 위치에 있을 때를 while문 밖에 두어서 헤맴
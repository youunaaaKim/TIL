import sys

sys.stdin = open('input.txt')

'''
1번 방에는 2번 방으로 가는 한 개의 포탈
2번 부터 N-1번 방에는 바로 오른쪽, 왼쪽방 중 하나로 가는 두 개의 포탈
방의 번호는 P[i]로 주어지고 제일 오른쪽 방에 도착하면 게임 끝
어떤 방에 처음 들어갔을 때에는 반드시 왼쪽으로 가는 포탈을 사용, 이후에 들어갔을 때에는 오른쪽으로 가는 포탈을 사용
1번 방에서 시작하여 게임이 끝날 때 까지 포탈을 몇 번 사용하게 되는지 계산
P[i], P[N]은 의미가 없음에 주의
P[i]의 값은 반드시 i번째 방의 왼쪽에 있는 방 중 하나의 번호
4<=N<500

[시나리오]
오른쪽으로 한 칸씩 이동하면서 방문 여부 확인
방문했다면 오른쪽 한 칸
방문하지 않았다면 i번째 방으로 이동, 방문 여부 확인

'''

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N개의 방
    P = input().split()

# print(P)

#몇 번 포탈을 사용하는지 계산
count = 0
# 몇 번째 방문인지 카운트할 리스트
visit = [0] * N # visit 안에 방문 여부 확인하는 portal

for i in range(1, len(P)-1): # 1번 부터 N-1번 방까지
    while i != (N - 1):
        # print(range(1, len(P)-1))
        if i == 1: # 1번 방에는 2번 방으로 가는 한 개의 포탈 -> 2번 방에 도착하면 두 개의 포탈
            count += 1
            visit[i-1] = 1
            i += 1

        if (N-1) > i >= 2: # 2번째 방 부터는 오른쪽으로 가는 포탈, 왼쪽 방 중 하나로 가는 포탈 P[2]
            # 두 번째 방문이라면 왼쪽으로 (P[i]의 값은 반드시 i번째 방의 왼쪽에 있는 방 중 하나의 번호)
            for i in range(2, len(P)-1):
                    # 두 번째 방문이라면 바로 오른쪽의 방으로
                    if visit[i-1] >= 1:
                        i += 1
                        count += 1

                    # 첫 번째 방문이라면 p[i] = answer일 때, answer-1 부터 i-1 까지의 visit의 값을 모두 +1
                    else:
                        answer = 0
                        #P[i]의 값 확인
                        answer = P[i]
                        answer = int(answer)
                        for plus in range(answer, i):
                            visit[plus] += 1# 방문 여부를 1로 전환
                            count += (i-answer+1)

    print(f'#{tc} {count}')
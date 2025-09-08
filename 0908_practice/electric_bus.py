import sys

sys.stdin = open('electric_bus_input.txt')
T = int(input())
for tc in range(1, T+1):
    K, N, M = input().split()
    N = int(N) # 종점
    K = int(K) # 한 번 충전으로 최대한 이동할 수 있는 정류장 수
    M = int(M) # 충전기 설치 대 수
    charge = list(map(int, input().split())) # 충전기가 설치된 M 개의 정류장 번호
    #print(charge)

    # 전기 버스는 0번에서 출발
    # 한 번 충전으로 K 만큼 이동
    # K 만큼 이동했을 때 그 범위 안에서 k와 가장 가까운 충전기에서 충전

    road = [0]*(N+1) # 0부터 N 까지 충전소가 있는 위치를 100으로 표시
    for i in charge:
        road[i] = 100
    #print(road)


    count = 0 # 버스가 충전한 횟수
    current = 0 # 버스의 현재 위치는 0
    while current + K < N: # 현재 위치에서 최대한 갈 수 있는 거리를 합 한 것이 N보다 작을 때 까지
        for step in range(K, 0, -1): # 최대한 갈 수 있는 끝 부터 거꾸로 충전소가 있는지 탐색
            if road[current + step] == 100: # 최대한 갈 수 있는 K 부터 현재 위치까지 충전소가 있다면
                current += step # 현재 위치를 그 충전소가 있는 위치로 업데이트
                count += 1 # 충전 한 횟수 +1
                break
        else: # 충전할 곳 없음
            count = 0
            break

    print(f"#{tc} {count}")





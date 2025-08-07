import sys
sys.stdin = open('electric.txt')  # input.txt 파일에서 입력을 읽도록 설정

T = int(input())
for tc in range(1, T):
    K, N, M = map(int, input().split())  # N: 종점 정류장, K: 한 번 충전으로 가능한 이동 거리 M: 충전기 설치 정류장 개수
    charg = list(map(int, input().split())) # 충전기 설치 정류장 번호
    #print(arr)
    #종점에 갈 수 있는 최소한의 충전 횟수 구하기

    #주유소 위치 표시
    charging_station = [0] * (N+1)
    for charging in charg:
        charging_station[charging] += 1

    bus = 0 # 버스 위치
    last_charge_pos = 0 # 마지막 충전 위치
    charge_count = 0 # 충전 횟수

    while bus < N:
        bus += K

        if bus >= N:
            break

        #연료 없으면 주유소 찾아야 함
        bus_dying = bus
        while bus_dying > last_charge_pos:
            if charging_station[bus_dying] == 1:
                charge_count +=1
                bus = bus_dying
                last_charge_pos = bus
                break
            bus_dying -= 1

        else:
            charge_count = 0
            break


    print(f"#{tc} {charge_count}")



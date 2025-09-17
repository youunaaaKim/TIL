import sys
sys.stdin = open('0860_premiun_bungeoppang_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = input().split() #N: 붕어빵을 먹을 수 있는 사람 M:붕어빵 만드는 시간(초) K:만드는 붕어빵 수
    N = int(N)
    M = int(M)
    K = int(K)

    arr = sorted(map(int, input().split())) # 손님이 오는 초
    total_time = 11111
    #print(arr)

    # 0초 손님 있으면 바로 불가능
    if arr[0] == 0:
        print(f"#{tc} Impossible")
        continue

    # 사람 도착하는 리스트
    arrive = list([0] * (total_time+1))
    # 붕어빵 만드는 리스트
    make = list([0] * (total_time+1))

    # 초마다 사람 카운팅
    for i in arr:
        arrive[i] += 1
    #print(arrive)
        # => [0,0,1,1,0,0,0 ...]

    # 초마다 붕어빵 카운팅
    for t in range(1, total_time + 1):
        if M>0 and t % M == 0:  # M초마다
            make[t] = K  # K개 생산
    #print(make)

    # for 초마다
    # M*K = M 초 동안 만들 수 있는 붕어빵의 수
        # if 사람 > 붕어빵 갯수 : Impossible
        # if 사람 < 붕어빵 갯수 : Possible
    stock = 0
    possible = True
    for t in range(1, total_time + 1):
        stock += make[t]  # 생산 반영
        if arrive[t] > 0:  # 손님 도착 시
            stock -= arrive[t]
        if stock < 0:  # 재고 부족 시 불가능
            possible = False
            break

    print(f"#{tc} {'Possible' if possible else 'Impossible'}")
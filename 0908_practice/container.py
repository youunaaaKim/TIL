import sys

sys.stdin = open('container_input')
T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    N = int(N) # 컨테이너 수
    M = int(M) # 트럭 수
    w = list(map(int, input().split())) # N 개의 화물의 무게
    t = list(map(int, input().split()))  # M 개 트럭의 적재용량
    w.sort(reverse=True)
    t.sort(reverse=True)
    # print(w)
    # print(t)

    # N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반
    # 트럭당 한 개의 컨테이너를 운반
    # 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없음
    # A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행
    # 이때 이동한 화물의 총 중량이 최대가 되도록 하는 화물의 전체 무게 출력

    total = 0 # 옮긴 컨테이너의 총 무게
    used = [False] * N # 컨테이너 옮긴 것인지 아닌지
    for truck in t: # 트럭마다
        for weight in range(len(w)): # 트럭마다 내가 옮길 수 있는 무게인지 확인하기
            # 정렬이 되어있으니, 순서대로 확인하면 무거운 것 부터 확인 가능
            if truck >= w[weight] and not used[weight]: # 옮기지 않은 컨테이너이고 무게가 트럭이 수용 가능한 무게 보다 작거나 같으면
                total += w[weight] # 옮긴 컨테이너의 총 무게에 더하기
                # 활용한 트럭과 컨테이너 true로 바꾸기
                used[weight] = True
                break
    # print(w)
    print(f'#{tc} {total}') # total 출력











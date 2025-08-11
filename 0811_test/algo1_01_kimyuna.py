import sys

sys.stdin = open('algo1_sample_in.txt')
#테스트케이스 입력 받기
T = int(input())
# print(T)
for tc in range(1, T+1):
    # M : 탐색할 수 있는 범위 , N : 우주 공간 , K :  별의 갯수
    N, M, K = input().split()
    N = int(N)
    M = int(M)
    K = int(K)
    # print(N)
    # print(M)
    # print(K)

    # N*N의 배열 입력 받기
    arr = [list(input().strip()) for _ in range(N)]
    # print(arr)

    #좌표의 이동 (사용하지 않지만 기존 코드 보존)
    dr = [-1,-1,0,0]
    dc = [0,0,-1,-1]

    # 탐색할 수 있는 영역
    # 영역 안에 K 개의 별을 포함해야 함
    found = False
    for serch in range(N - M + 1):         # 행 방향(좌상단 r)
        #별의 갯수를 세기 위한 변수는 각 열 시작 시 초기화
        for see in range(N - M + 1):       # 열 방향(좌상단 c)
            number_of_star = 0
            #좌표의 초기 위치 설정 = 현재 MxM 윈도우 좌상단
            r0, c0 = serch, see

            # serch가 움직일 때 마다 see가 별 갯수 확인 (MxM 내부 스캔)
            for r in range(r0, r0 + M):
                for c in range(c0, c0 + M):
                    if arr[r][c] == '*':
                        number_of_star += 1

            # 별의 갯수가 K와 같아질 때 정답 출력
            if number_of_star == K:
                print(f'#{tc} {r0} {c0}')
                found = True
                break

        if found:
            break

    # K 개의 별의 갯수를 찾을 수 없다면 -1 -1 출력
    if not found:
        print(f'#{tc} -1 -1')

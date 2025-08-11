# import sys
#
# sys.stdin = open('algo1_sample_in.txt')
#테스트케이스 입력 받기
T = int(input())
# print(T)
for tc in range(1, T+1):
    # M : 탐색할 수 있는 범위 , N : 우주 공간 , K :  별의 갯수
    N, M, K = input().split()
    # N = int(N)
    # M = int(N)
    # K = int(N)
    # print(N)
    # print(M)
    # print(K)
    arr = [list(input()) for _ in range(N)] # N*N의 배열 입력 받기
    # print(arr)

    #좌표의 이동
    dr = [-1,-1,0,0]
    dc = [0,0,-1,-1]


    # 탐색할 수 있는 영역
    # 영역 안에 K 개의 별을 포함해야 함
    for serch in round(N):
        #별의 갯수를 세기 위한 변수 초기화
        number_of_star = 0
        for see in round(serch):
            #좌표의 초기 위치 설정
            serch_area = arr[0][0]
            # serch가 움직일 때 마다 see가 별 갯수 확인
            if '*' in serch_area:
                number_of_star += 1
                # 별의 갯수가 K와 같아질 때 정답 출력
                if number_of_star == K:
                    print(f'#{tc} {dr} {dc}')
                #K 개의 별의 갯수를 찾을 수 없다면 -1 -1 출력
                elif number_of_star == 0:
                    print(f'#{tc} -1 -1')







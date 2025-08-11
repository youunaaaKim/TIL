# import sys
#
# sys.stdin = open('algo2_sample_in.txt')
#테스트케이스 입력 받기
T = int(input())
# print(T)
for tc in range(1, T+1):
    # M , N : 2차원 배열
    N, M = input().split()
    N = int(N)
    M = int(N)
    # print(N)
    # print(M)
    arr = [list(input().split()) for _ in range(N)] #배열의 값
    # print(arr)

    #N과 M의 배열에 대해서 안전 구역을 돌면서 안전 구역의 수 확인
    for i in range(N):
        for j in range(M):
            #현재 위치 표시
            present_area = arr[i][j]
            #안전 구역의 수 계산을 위한 변수
            number_of_safe_area = 0
            # 만약 현재 위치의 값이 인접 위치의 값보다 크다면
            if present_area > present_area[i+1][j+1]:
                if present_area > present_area[i+1][j-1]:
                    if present_area > present_area[i-1][j+1]:
                        if present_area > present_area[i-1][j-1]:
                            #안전 구역 갯수 더하기
                            number_of_safe_area += 1
            #정답 출력
            print(f'#{tc} {number_of_safe_area}')
            if i < 0 or i > M:
                break
            elif i < 0 or i > M:
                break





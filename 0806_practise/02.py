import sys
sys.stdin = open('02_input.txt')
T = int(input())

# 방향 벡터 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())

    #이차원 배열 설정
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    #모든 요소에서 꽃가루가 터지는 횟수 더해서 저장
    result = []

    # 이차원 배열 모든 요소를 순회
    # r은 행의 인덱스, c는 열의 인덱스
    # 첫 두 개의 for문은 이동을 위한 for문
    for r in range(N):
        for c in range(N):
            # 탐색을 위한 반복
            # 현재 위치 (r, c)의 상하좌우 인접한 요소를 확인
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                total = [r][c]

                # 인접한 요소의 좌표가 벽이 아닐때만
                if 0 <= nr < N and 0 <= nc < N:
                    total += arr[nr][nc]  # 상하좌우 값 더하기
                    result.append(total)  # 해당 위치의 합을 결과에 추가
                for i in total:
                    if i < total[i]:
                        i = total[i]


                print(f'#{tc} {i}')
















# import sys
# sys.stdin = open('02_input.txt')
#
# def bubble_sort(arr):
#     n = len(arr) #arr의 길이를 n이라고 정의
#     for i in range(n-1, 0, -1): #맨 뒤에서 두 번째 에서 0까지 거꾸로 한 단계씩 진행
#         for j in range(0, i): # 0부터 i까지 진행
#             if arr[j] > arr[j+1]: #j 번째 인덱스와 j+1번째 인덱스 숫자 비교
#                 arr[j], arr[j+1] = arr[j+1], arr[j] # sort
#     return arr #sort 완료된 배열 반환
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # print(arr)
#
#     # arr에서 첫 번째, 세 번째 숫자만 모아서 sort
#     # arr에서 두 번째, 네 번째 숫자만 모아서 sort
#     # 그 때의 중간 숫자들이 중첩박스
#
#     # 행 값과 열 값을 저장할 리스트
#     dr = []
#     dc = []
#     # 각각 리스트에 홀수 번째 값과 짝수 번째 값을 append
#     for i in range(N):
#         dr.append(arr[i][0])
#         dr.append(arr[i][2])
#         dc.append(arr[i][1])
#         dc.append(arr[i][3])
#     # print(dr)
#     # print(dc)
#
#     # bubble_sort로 정렬
#     dr = bubble_sort(dr)
#     dc = bubble_sort(dc)
#
#     #중앙값 찾기
#     if len(dr) % 2 == 0:
#         center_r = dr[(len(dr) // 2) - 1]  # 더 작은 쪽 (왼쪽)
#         center_c = dc[(len(dc) // 2) - 1]
#     else:
#         center_r = dr[len(dr) // 2]
#         center_c = dc[len(dc) // 2]
#
#     print(f'#{tc} {center_r} {center_c}')








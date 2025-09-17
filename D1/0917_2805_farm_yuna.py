import sys
sys.stdin = open('2805_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 농장의 크기. 항상 홀수
    arr = [list(map(int, input().strip())) for _ in range(N)]
    # print(arr)

    # 수확은 항상 농장의 크기에 맞는 정사각형 마름모 형태
    # 마름모 형태의 값(가치)을 더하기

    # 시나리오: 행별로 인덱스값 뽑아서 더하기
    # 0번째 열일 때는 c 값
    # 1번째 열일 때는 c-1, c, c+1
    # 2번째 열일 때는 c-2, c-1, c, c+1, c+2
    # 거꾸로 돌아가기
    # 슬라이싱!!

    carving = 0 # 수확량

    
    if N == 1:  # 1*1 매트릭스에서는 그 값이 답임
        carving = arr[0][0]
    else:
        c = N // 2   # 열의 기준 농장의 중앙 열
        
        
        # 0 ~ 중앙까지
        for r in range(c + 1):  
            carving += sum(arr[r][c - r: c + r + 1])

        # 아래쪽 마름모
        for r in range(c + 1, N):  # 중앙 다음 줄부터 끝까지
            k = N - 1 - r  # 중앙 열에서 얼마나 떨어져있는지 확인
            carving += sum(arr[r][c - k: c + k + 1]) # 범위만큼 더하기

    print(f'#{tc} {carving}')










# import sys
# sys.stdin = open('algo1_sample_in.txt')
# N 개의 숫자열 arr을 M 개의 윈도우로 나누어 윈도우 내에서 패턴을 찾기
    # 단순 증가 패턴을 가지는 윈도우는 몇 개인지 출력하기

    # N이 M의 배수가 아닌 경우 마지막 윈도우는 남은 원소에 대해서만 증가 패턴을 확인
    # 윈도우 내의 숫자가 1개인 경우 단순 증가 패턴으로 간주

    # N이 M의 배수가 아닌 경우
        # 윈도우 내의 숫자가 1개인 경우
    # N이 M의 배수인 경우 -> 어짜피 남은거 나눠질 테니 조건 걸 필요 없음

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(arr)

    # 윈도우 만들기
    count = 0
    for i in range(0, N, M):
        window = arr[i:i + M]

        # 윈도우 숫자가 1이면
        if len(window) == 1:
            count += 1
        # 윈도우 숫자가 1이 아니면 윈도우를 돌면서 단순 커지는지 확인
        increase = 0
        for k in range(len(window)-1):

            if window[k] < window[k+1]: # 단순 증가 패턴이라면
                k += 1 # 그 다음 k 확인
                increase += 1 # 단순 증가 패턴의 count를 +1

        if increase == (M-1): # 윈도우 안의 숫자가 모두 단순증가라면
            count += 1 # 단순증가 +1 해주고 다음 윈도우 확인
            i += 1
        else: # 윈도우 안의 숫자가 단순증가가 아니라면
            i += 1

    print(f'#{tc} {count}') # 결과 출력




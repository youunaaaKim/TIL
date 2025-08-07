import sys
sys.stdin = open('input.txt')  # input.txt 파일에서 입력을 읽도록 설정

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 배열 크기, M: 연속해서 더할 숫자 개수
    arr = list(map(int, input().split()))

    sums = []  # M개씩 연속된 숫자의 합을 저장할 리스트 초기화
    for i in range(N - M + 1):  # 시작 인덱스 i를 0부터 N-M까지 반복
        current_sum = 0  # 현재 구간의 합을 저장할 변수 초기화
        # i부터 i+M-1까지 인덱스 j를 순회하며 arr[j] 값을 current_sum에 더하기
        for j in range(i, i + M):
            current_sum += arr[j]
        sums.append(current_sum)

    #sums 리스트에서 최솟값, 최댓값 찾기
    min_num = sums[0]
    max_num = sums[0]
    for num in sums:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    answer = max_num - min_num
    print(f'#{tc} {answer}')

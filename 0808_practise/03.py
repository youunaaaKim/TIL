import sys

sys.stdin = open('03_input.txt')

T = int(input())
#print(T)

for tc in range(1, T+1):
    N, M = map(int, input().split())
    #print(N)
    #print(M)
    arr = [list(map(str, input())) for _ in range(N)]
    #print(arr)

    # 1번, 가로 전체로 봤을 때 회문이 있다면
    for r in range(N):
        arr_r = arr[r]
        if arr_r == arr_r[::-1]:
            answer = ''.join(arr_r)
            print(f'#{tc} {answer}')
        else:
            #문장 중간에 회문이 있다면
            for i in range(N - M + 1): # 각 줄에서 길이 M짜리 부분 문자열을 추출해서 회문인지 확인. 슬라이싱의 시작 위치들
                substr_r = arr_r[i:i + M]
                if substr_r == substr_r[::-1]:
                    answer_r = ''.join(substr_r)
                    print(f'#{tc} {answer_r}')


    # 2번, 세로 전체로 봤을 때 회문이 있다면
    # zip(*arr)로 전치해서 열 기준 접근
    for ans in zip(*arr):
        ans_str = ''.join(ans)
        if ans_str == ans_str[::-1]:
            print(f'#{tc} {ans_str}')
        #문장 중간에 회문이 있다면
        else:
            for i in range(N - M + 1):
                substr_c = arr_r[i:i + M]
                if substr_c == substr_c[::-1]:
                    answer_c = ''.join(substr_c)
                    print(f'#{tc} {answer_c}')
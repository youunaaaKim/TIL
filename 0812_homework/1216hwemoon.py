import sys
sys.stdin = open('1216hwemoon_input.txt')

T = 10
for tc in range(1, T + 1):
    Test = int(input())
    N = 100
    arr = [list(map(str, input())) for _ in range(N)]
    # print(arr)


# 가로와 세로의 회문의 길이를 구하는 리스트를 만들고 거기서 비교를 해야 함

    # answer_list = []
    # # 1번, 가로 전체로 봤을 때 회문이 있다면
    # # 회문 찾기
    # for i in range(N):# 각 줄에서 부분 문자열을 추출해서 회문인지 확인
    #     arr_r = arr[i]
    #     substr_r = arr_r[i:i + N]  # 시작 위치부터 회문의 길이만큼
    #     if substr_r == substr_r[::-1]:  # 슬라이싱 방식으로 회문 확인
    #         answer = len(substr_r)
    #         answer_list.append(answer)
    #
    # # 2번, 세로 전체로 봤을 때 회문이 있다면
    # # zip(*arr)로 전치해서 열 기준 접근
    # for ans in zip(*arr):
    #     for i in range(N):
    #         # 각 줄에서 부분 문자열을 추출해서 회문인지 확인
    #         substr_c = arr_c[i:i + N]  # 시작 위치부터 회문의 길이만큼
    #         if substr_c == substr_c[::-1]:  # 슬라이싱 방식으로 회문 확인
    #             answer_c = len(substr_c)
    #             answer_list.append(answer_c)
    # print(answer_list)

    '''
    1. 변수 범위 점검
arr_r는 가로줄 하나(arr[i])만 담고 있어서 세로 탐색에서는 쓰면 안 돼.

세로 탐색에서는 col = [arr[r][c] for r in range(N)]처럼 열 데이터를 따로 뽑아서 그걸로 회문 검사를 해야 해.

2. 슬라이싱 범위 점검
지금은 arr_r[i:i+N]처럼 고정 길이 N만 검사하는데, 이러면 전체 길이 회문만 찾게 돼.

회문 문제는 길이를 줄여가면서(N, N-1, N-2, …, 1) 모든 경우를 확인해야 해.
'''
    answer_list = []

    # 1번, 가로 회문
    for row in arr:
        for length in range(N, 0, -1):  # 긴 길이부터 검사
            for start in range(N - length + 1):
                substr_r = row[start:start + length]
                if substr_r == substr_r[::-1]:
                    answer_list.append(length)
                    break  # 이 줄에서는 더 짧은 건 볼 필요 없음
            else:
                continue
            break

    # 2번, 세로 회문
    for col in zip(*arr):  # 세로 데이터
        col = list(col)  # 슬라이싱 가능하도록 변환
        for length in range(N, 0, -1):
            for start in range(N - length + 1):
                substr_c = col[start:start + length]
                if substr_c == substr_c[::-1]:
                    answer_list.append(length)
                    break
            else:
                continue
            break

    print(f"#{tc} {max(answer_list)}")

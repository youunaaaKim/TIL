import sys

sys.stdin = open('1959_input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    A_arr = list(map(int, input().split()))
    B_arr = list(map(int, input().split()))
    # print(A_arr)
    # print(B_arr)

    # 두 개의 배열의 인덱스 시작 위치를 조정해서
    # 숫자들이 서로 마주보는 위치를 변경할 수 있다.
    # 하지만 더 긴 쪽의 양 끝을 벗어나면 안됨

    # 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값 구하기

    # 곱해서 숫자 더한 최댓값을 리턴하는 함수
    def wow(short_arr, long_arr, start_idx):
        '''
        :param short_arr: 짧은 배열
        :param arr2: 긴 배열
        :param start_idx: 긴 배열에서 짧은 배열이 시작하는 인덱스
        :return: 곱한 값들의 합
        '''
        middle_answer = []  # 곱한 결과를 저장할 리스트
        for i in range(len(short_arr)):  # 짧은 배열의 길이만큼 반복
            # 같은 위치의 숫자끼리 곱함
            little_answer = short_arr[i] * long_arr[start_idx + i]
            middle_answer.append(little_answer)  # 결과 저장
        big_answer = sum(middle_answer)  # 총합 구함
        return big_answer  # 결과 반환


    max_val = -float('inf')  # 최댓값 초기화

    # 두 개의 배열 중에 작은 배열 찾기
    if len(A_arr) <= len(B_arr):  # A가 짧거나 같은 경우
        short_arr = A_arr  # 짧은 배열
        long_arr = B_arr  # 긴 배열
    else:  # B가 더 짧은 경우
        short_arr = B_arr
        long_arr = A_arr

    # 작은 배열의 인덱스 값을 한 칸씩 옮겨보기
    for i in range(len(long_arr) - len(short_arr) + 1):
        # 현재 위치에서 곱해서 합 구하기
        result = wow(short_arr, long_arr, i)
        # 최댓값 갱신
        if result > max_val:
            max_val = result

    # 최종 결과 출력
    print(f'#{tc} {max_val}')










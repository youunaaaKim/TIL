def counting_sort(input_arr, k):
    '''
    카운팅 정렬 함수
    input_arr : 정렬할 입력 배열 (각 원소는 0 이상 k 이하의 정수)
    k : 입력 배열 내 원소의 최대값 (데이터 범위를 의미)
    '''
    # 1. k+1 크기의 카운팅 배열을 0으로 초기화 (인덱스 0부터 k까지 사용)
    counting_arr = [0] * (k + 1)

    # 2. 입력 배열 내 각 원소의 빈도수를 counting_arr에 기록합니다.
    for num in input_arr:
        counting_arr[num] += 1

    # 2.1 빈도수 배열 출력
    # print('빈도수 배열:', counting_arr)

    # 3. 누적 합을 계산하여 각 원소가 정렬된 배열 내에서 차지할 위치를 결정합니다.
    for i in range(1, k + 1):
        counting_arr[i] += counting_arr[i - 1]

    # 3.1 누적 합 배열 출력
    # print('누적 합 배열:', counting_arr)

    # 4. 결과 배열 초기화: 입력 배열과 같은 크기로 생성합니다.
    result_arr = [0] * len(input_arr)

    # 5. 입력 배열을 역순으로 순회하며, 각 원소를 결과 배열의 올바른 위치에 배치합니다.
    #    (역순 순회는 정렬의 안정성을 보장하기 위한 기법입니다.)
    # 5.1 역순 reversed 버전
    for num in reversed(input_arr):
        counting_arr[num] -= 1  # 해당 원소의 위치 인덱스를 하나 감소시킵니다.
        result_arr[counting_arr[num]] = num

    # 5.2 역순 index 버전
    # for i in range(len(input_arr) - 1, -1, -1):
    #     counting_arr[input_arr[i]] -= 1
    #     result_arr[counting_arr[input_arr[i]]] = input_arr[i]

    return result_arr


# 테스트 예시
arr = [0, 4, 1, 3, 1, 2, 4, 1]
print(
    '정렬 결과:', counting_sort(arr, 5)
)  # 출력 예시: [0, 1, 1, 1, 2, 3, 4, 4]

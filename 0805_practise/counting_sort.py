

def counting_sort(input_arr, k):
    counting_arr = [0] * (k + 1)

    for num in input_arr:
        counting_arr[num] +=1

    for i in range(1, k+1):
        counting_arr[i] += counting_arr[i - 1]

    result_arr = [0] * len(input_arr)
    for num in reversed(input_arr):
        counting_arr[num] -= 1  # 해당 원소의 위치 인덱스를 하나 감소시킵니다.
        result_arr[counting_arr[num]] = num

    return result_arr

# 테스트 예시
arr = [0, 4, 1, 3, 1, 2, 4, 1]
print(
    '정렬 결과:', counting_sort(arr, 5)
)  # 출력 예시: [0, 1, 1, 1, 2, 3, 4, 4]


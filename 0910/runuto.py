import sys

sys.stdin = open('input.txt')


def quick_sort_lomuto(arr, start, end):
    """
    퀵 정렬을 재귀적으로 지시하는 '매니저' 함수입니다.
    """
    # 정렬할 범위에 원소가 1개 이상 있을 때만 실행합니다.
    if start < end:
        # 1. 분할: partition 함수를 호출하여 피벗의 최종 위치를 찾습니다.
        pivot_idx = partition_lomuto(arr, start, end)

        # 2. 정복 (재귀 호출)
        # 피벗을 기준으로 나뉜 왼쪽 부분을 재귀적으로 정렬합니다.
        quick_sort_lomuto(arr, start, pivot_idx - 1)
        # 피벗을 기준으로 나뉜 오른쪽 부분을 재귀적으로 정렬합니다.
        quick_sort_lomuto(arr, pivot_idx + 1, end)


def partition_lomuto(arr, start, end):
    """
    로무토 파티션: 가장 오른쪽 원소를 피벗으로 사용합니다.
    피벗보다 작은 값들은 왼쪽으로, 큰 값들은 오른쪽으로 재배치합니다.
    """
    # 피벗을 리스트의 마지막 원소로 선택합니다.
    pivot = arr[end]
    # '피벗보다 작은 그룹'의 경계를 나타내는 인덱스입니다.
    i = start - 1

    # start부터 end-1(피벗 직전)까지 순회합니다.
    for j in range(start, end):
        # 만약 현재 원소(arr[j])가 피벗보다 작다면,
        if arr[j] < pivot:
            # '작은 그룹'의 경계를 한 칸 오른쪽으로 이동시키고,
            i += 1
            # 경계 위치(i)의 값과 현재 값(j)을 교환하여, 작은 원소를 왼쪽으로 보냅니다.
            arr[i], arr[j] = arr[j], arr[i]

    # 모든 순회가 끝나면, i+1 위치가 피벗이 들어갈 최종 자리입니다.
    # 피벗(arr[end])과 경계 다음 위치(arr[i+1])의 값을 교환합니다.
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    # 피벗의 최종 위치 인덱스를 반환합니다.
    return i + 1


T = int(input())
for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    quick_sort_lomuto(numbers, 0, len(numbers) - 1)
    print(f'#{tc}', *numbers)

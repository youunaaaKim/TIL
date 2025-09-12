import sys

sys.stdin = open('input.txt')

'''
퀵 정렬을 계속 호출하면서 계속 피벗을 기준으로 쪼개고 쪼갠거에서 피벗 위치 고르기
쪼갤 수 없을 때까지 피벗 위치 정하는 함수 호출
'''
def quick_sort_lomuto(arr, start, end):
    '''

    쪼갤 수 없을 때 까지 피벗을 호출하는 함수

    :param arr: 배열
    :param start: 시작 위치
    :param end: 끝나는 위치
    :return: 리턴 없음 그냥 종료
    '''
    # 쪼갤 수 없을 때 까지 피벗을 호출
    if start < end: # 쪼갤 수 없을 때 까지
        # 함수를 호출
        # 이 함수는 파티션의 위치를 리턴함
        # 파티션의 위치 : 피벗은 최종적으로 자기보다 큰 값, 자기보다 작은 값 사이로 들어감 그 위치를 리턴
            piv_idx = partition_lomuto(arr, start, end)

        # 리턴받은 파티션의 위치를 기준으로 앞 부분 재귀, 뒷 부분 재귀
        # 재귀 : 파티션 위치 반환하고 그 기준으로 쪼개기
        # 피벗을 기준으로 나뉜 앞쪽 부분을 재귀
            quick_sort_lomuto(arr, start, piv_idx - 1)
            # 피벗을 기준으로 나뉜 뒷 부분을 재귀
            quick_sort_lomuto(arr, piv_idx + 1, end)
    # 리턴 없음 쪼갤 수 없으면 종료

def partition_lomuto(arr, start, end):
    '''

    피벗의 위치를 정해주는 함수

    :param arr: 배열
    :param start: 시작 위치
    :param end: 끝나는 위치
    :return: 파티션의 위치를 반환함
    '''
    i = start -1 # 경계를 나타내는 인덱스
    piv = arr[end] # 초기 피벗의 위치는 맨 마지막 위치

    for j in range(start, end): # j가 배열을 돌면서 인덱스에 해당하는 값을 확인
        if arr[j] < piv: # 맨 마지막 위치의 값과 j 위치의 인덱스 값을 비교할 때 후자가 작다면
            i += 1 # i의 값을 1 올려주고
            arr[i], arr[j] = arr[j], arr[i] # 작은 값을 앞으로 바꾸기

    # 피벗 위치와 경계의 다음 위치를 바꾸기 피벗 위치 => 경계의 다음 위치
    arr[i+1], arr[end] = arr[end], arr[i+1]

    # 피벗의 위치를 반환
    return i + 1

























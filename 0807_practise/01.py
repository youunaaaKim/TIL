import sys
sys.stdin = open('01_input.txt')

def select_smallest(arr, k):
    '''
    주어진 리스트 arr에서 k번째로 작은 원소를 반환하는 함수
    '''
    # k번 반복하면서, 'k번째로 작은 원소'를 정렬
    for i in range(k):
        min_idx = i # 현재 위치를 최소값 위치로 가정
        n = len(arr)
        # i+1부터 끝까지 돌며, arr[min_idx]보다 더 작은 원소 찾으면 갱신
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # 찾은 최소값을 i번째와 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # k번째로 작은 원소 = arr[k-1]
    return arr[k - 1]

def select_largest(arr, k):
    '''
    주어진 리스트 arr에서 k번째로 큰 원소를 반환하는 함수
    '''

    for i in range(k):# 앞에서부터 k번째까지 반복
        max_idx = i # 현재 위치를 최대값 위치로 가정
        n = len(arr)
        # i 이후의 요소 중에서 가장 큰 값의 인덱스를 찾음
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr[k - 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = [] # 결과를 저장할 리스트

    for i in range(N): # N개의 숫자 중에서, 큰 수, 작은 수, 큰 수 순서로 선택
        if i % 2 == 0: # 짝수 인덱스
            val = select_largest(arr[:], i//2 + 1) # i // 2 + 1 번째로 큰 수를 선택 (1번째, 2번째, ...)
        else: # 홀수 인덱스
            val = select_smallest(arr[:], i//2 + 1) # i // 2 + 1 번째로 작은 수를 선택 (1번째, 2번째, ...)
        result.append(val)  # 선택한 값을 결과 리스트에 추가

    # 출력
    print(f"#{tc} {' '.join(map(str, result))}")
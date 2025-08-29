def comb(arr, r):
    """
    Args:
        arr (list): 원본 배열
        r (int): 뽑을 개수

    Returns:
        list: 모든 조합이 담긴 2차원 리스트
    """
    result = []

    # 기저 조건(Base Case): 뽑을 개수가 0이면, 빈 리스트를 담은 리스트를 반환하여 조합 완성
    if r == 0:
        return [[]]

    # 재귀 호출(Recursive Step)
    for i in range(len(arr)):
        # i번째 원소를 첫 번째 요소로 선택
        elem = arr[i]

        # i번째 원소 이후의 나머지 리스트에서
        # 나머지 (r-1)개의 조합을 재귀적으로 구함
        for rest in comb(arr[i + 1 :], r - 1):
            # 선택한 요소(elem)와 나머지 조합(rest)을 합쳐 결과에 추가
            result.append([elem] + rest)

    return result


# --- 실행 코드 ---
all_combs = comb([1, 2, 3, 4], 3)
print(all_combs)

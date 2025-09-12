def find_permutations(nums):
    """
    순열 탐색을 시작하고 최종 결과를 반환하는 메인 함수.
    """
    result = []
    # 각 숫자의 사용 여부를 기록할 리스트 (used[i]가 True이면 i번째 숫자는 사용 중)
    used = [False] * len(nums)

    # 빈 순열([])에서 백트래킹 탐색 시작
    backtrack_permutations_helper(nums, used, [], result)

    return result


def backtrack_permutations_helper(nums, used, current_permutation, result):
    """
    실제 백트래킹 탐색을 수행하는 재귀 함수 (헬퍼 함수).
    """
    # 기저 조건: 현재 순열의 길이가 원본 리스트의 길이와 같으면 해를 찾은 것
    if len(current_permutation) == len(nums):
        result.append(current_permutation[:])  # 완성된 순열을 결과에 추가
        return

    # 재귀 단계: 모든 숫자를 순회하며 다음 자리에 올 숫자를 선택
    for i in range(len(nums)):
        # 유망성 조사: 아직 사용하지 않은 숫자라면
        if not used[i]:
            # 1. 선택 (Choose): 숫자를 사용했다고 표시하고, 현재 순열에 추가
            used[i] = True
            current_permutation.append(nums[i])

            # 2. 탐색 (Explore): 다음 자리를 채우기 위해 재귀 호출
            backtrack_permutations_helper(
                nums, used, current_permutation, result
            )

            # 3. 선택 취소 (Un-choose): 재귀 호출이 끝나고 돌아오면,
            #    선택을 취소하여 다음 반복에서 다른 선택을 할 수 있도록 원상 복구
            current_permutation.pop()
            used[i] = False


# --- 실행 ---
print(find_permutations([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

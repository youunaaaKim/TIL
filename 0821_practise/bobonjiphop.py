from itertools import combinations # iterable에서 원소 개수가 r개인 조합 뽑기

arr = list(range(1, 11)) # input
N = len(arr)
target_sum = 10
valid_subset = [] # 부분집합을 저장할 리스트

for k in range(1, N + 1): # 1개부터 N+1개까지의 부분집합을 설정할 K
    # arr에서 k개의 원소로 만들 수 있는 모든 조합을 생성
    for subset in combinations(arr, k):
        # # 해당 조합(부분집합)의 합이 10이면
        if sum(subset) == target_sum:
            # 결과 리스트에 추가
            valid_subset.append(subset)


# --- 결과 출력 ---
valid_subset.sort()
for subset in valid_subset:
    print(*subset)
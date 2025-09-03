import sys
sys.stdin = open('16811_carrot_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    sizes = list(map(int, input().split()))

    # 크기별 개수 저장 (크기 1~30)
    count = [0] * 31
    for size in sizes:
        count[size] += 1

    max_per_box = N // 2  # 한 상자에 들어갈 수 있는 최대 당근 수
    min_diff = float('inf')  # 최소 개수 차이
    is_valid = False  # 유효한 포장이 존재하는지 여부

    # 소: 1~i, 중: (i+1)~j, 대: (j+1)~30 으로 나누기
    for i in range(1, 29):       # i: 소 상자의 최대 크기
        for j in range(i + 1, 30):  # j: 중 상자의 최대 크기
            small_count = sum(count[1:i + 1])
            medium_count = sum(count[i + 1:j + 1])
            large_count = sum(count[j + 1:31])

            # 조건 3: 비어있는 상자가 있으면 안 됨
            if small_count == 0 or medium_count == 0 or large_count == 0:
                continue

            # 조건 4: 한 상자에 너무 많은 당근이 있으면 안 됨
            if max(small_count, medium_count, large_count) > max_per_box:
                continue

            # 조건 만족 → 개수 차이 계산
            current_diff = max(small_count, medium_count, large_count) - min(small_count, medium_count, large_count)

            if current_diff < min_diff:
                min_diff = current_diff
                is_valid = True

    # 결과 출력
    if is_valid:
        print(f'#{tc} {min_diff}')
    else:
        print(f'#{tc} -1')

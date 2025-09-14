T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))

    # 맥스 값 초기화
    max_num = -1

    # i, j 순회
    for i in range(N):
        for j in range(i+1, N):
            # i, j가 같지 않을 경우
            if i != j:
                # 단조인지 확인
                is_pass = True
                # 확인할 숫자
                check_num = str(A[i] * A[j])
                # 확인할 숫자 순회
                for k in range(len(check_num) - 1):
                    # 현재 위치 숫자가 다음 위치보다 크면
                    if int(check_num[k]) > int(check_num[k + 1]):
                        # 단조 아니라고 표시하고 반복 종료
                        is_pass = False
                        break

                # 단조이면 업데이트
                if is_pass:
                    max_num = max(max_num, A[i] * A[j])

    print(f"#{tc} {max_num}")
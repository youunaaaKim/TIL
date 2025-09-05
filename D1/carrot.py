# 같은 크기의 당근은 같은 상자에 들어있어야 한다.
# 비어 있는 상자가 있으면 안 된다.
# 한 상자에 N/2개(N이 홀수면 소수점 버림)를 초과하는 당근이 있어서도 안 된다.
# 앞의 조건을 만족하면서도, 각 상자에 든 당근의 개수 차이가 최소가 되도록 포장해야 한다.
# 이때의 개수 차이를 서류에 표시 한다.

import sys
sys.stdin = open('p_01.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(arr)

    cou = [0] * (N+1)
    for i in arr:
        cou[i] += 1
    print(cou)

    final = []
    for i in range(len(cou)):
        if cou[i] != 0:
            final.append(cou[i])
    print(final)

    # 최대 최소 차이 구하기
    # 최소로 가질 수 있는 당근의 갯수
    cut = N//2

    # 집단의 갯수가 3인 경우
    if len(final) == 3:
        for f in range(len(final)):
            # 당근의 갯수가
            if final[f] > cut:
                print(f'#{tc} -1')
            else:
                answer = max(final) - min(final)
                print(f'#{tc} {answer}')


    # 집단의 갯수가 3이 아닌 경우
    if len(final) != 3:
        # 최대 포용 가능한 만큼 합치기
        # 하지만 두 집단이 완전히 합쳐지는 거 아니면 안됨


    # for f in range(len(final)):
    #
    #
    #     if final[f] > cut:
    #         print(f'#{tc} -1')











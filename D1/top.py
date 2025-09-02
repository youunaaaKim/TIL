import sys
sys.stdin = open('top_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, W1, W2 = input().split()
    N = int(N)
    W1 = int(W1)
    W2 = int(W2)
    K = list(map(int, input().split()))
    print(K)
    # 각 탑의 높이에 맞춰 화물들을 쌓았을 때 최소 비용이 들도록 계산
    # 층별 비용 1층은 *1, 2층은 *2

    # 시나리오
    # 일단 k를 정렬, w1과 w2에 나눠 담기
    # 최소 비용을 계산

    # 나눠담을 리스트
    first_top = []
    last_top = []
    # k를 정렬
    top_list = sorted(K, reverse=True)
    print(top_list)
    # w1과 w2에 나눠 담기
    for i in range(0, len(top_list)):
        if i % 2 == 0: # 인덱스 숫자가 짝수면 last_top
            last_top.append(top_list[i])
        else: # 인덱스 숫자가 홀수면 first_top
            first_top.append(top_list[i])
    print(first_top)
    print(last_top)

    first_top_sum = 0
    last_top_sum = 0
    # 최소 비용 계산하기
    for f in range(0, len(first_top)):
        first_top_sum += (f+1) * first_top[f] # 층 수(0층 없으니 1 더하기) * 쌓을 화물
    for l in range(0, len(last_top)):
        last_top_sum += (l+1)*last_top[l] # 층 수(0층 없으니 1 더하기) * 쌓을 화물

    answer = first_top_sum + last_top_sum

    print(f'#{tc} {answer}')









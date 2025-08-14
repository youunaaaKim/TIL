import sys
sys.stdin = open('03_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    #print(arr)

    # Ai x Aj값을 넣을 리스트
    multipl = []
    #Ai x Aj값 구하기
    for j in range(N):
        for i in range(j):
            num = arr[i]*arr[j]
            # 붙여넣을 때 str 타입으로 붙여넣기
            # int로 하면 숫자의 앞자리, 뒷자리 비교 못하기 때문
            multipl.append(str(num))
    #print(multipl)

    # multipl에서 단조 증가하는 수 찾기
    # 단조 증가하는 숫자 넣을 리스트
    answer = []
    for num in multipl:
        if all(num[i] <= num[i + 1] for i in range(len(num) - 1)):
            answer.append(int(num))
    print(f'#{tc} {max(answer)}')

    # 내가 틀렸던 부분
    # for i in range(len(num) - 1):
    #     if num[i] <= num[i + 1]:
    #         answer.append(int(num))
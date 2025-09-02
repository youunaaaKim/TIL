import sys
sys.stdin = open('chajum_system_input_txt')

T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    N = int(N)
    M = int(M)
    answer = list(map(int, input().split())) # 답지
    arr = [list(map(int, input().split())) for _ in range(1, N+1)] # 학생들이 입력한 답
    print(answer)
    print(arr)

    # 채점방식
    # 처음으로 문제를 맞으면 1점, 그 다음 연속으로 답을 맞으면 앞 문항이 얻은 점수에 + 1 점을 추가하고,
    # 틀린경우 다시 0점으로 초기화하여 같은 방식으로 계산

    # 열 각각 돌면서 비교하면서 채점 저장하기
    score = [0] * (N+1)
    for i in range(N):
        stack = 0
        for j in range(M):
            if answer[j] == arr[i][j]:
                stack += 1
                score[i] += stack
            else:
                stack = 0


    result = max(score) - min(score)
    print(f'#{tc} {result}')







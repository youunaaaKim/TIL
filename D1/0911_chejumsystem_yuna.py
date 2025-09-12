import sys
sys.stdin = open('chajum_system_input_txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 학생 수, M은 문항 수
    answer = list(map(int, input().split())) # 답지
    arr = [list(map(int, input().split())) for _ in range(N)] # 학생들이 입력한 답
    # print(answer)
    # print(arr)

    # 답지와 학생들이 연속으로 답을 맞췄는지 확인해야 함
    # 연속으로 맞췄다면 계속 +1을 더해가면서 점수 계산
    # 아니라면 0으로 초기화해서 다시 더하기

    # 학생들의 총점을 입력할 빈 배열 만들기
    score = [0] * N

    for i in range(N):
        stack = 0 # 어려웠던 부분 - stack, is_correct를 처음에 N을 도는 포문 바깥에 둬서 고민하는 시간을 많이 가짐
        # 반복문 안에서 초기화해야 각 학생마다 점수가 계산됨
        is_correct = [0] * M # 학생들 각각의 문항별로 채점 점수를 확인할 리스트
        for j in range(M):
            if answer[j] == arr[i][j]:
                stack += 1
                is_correct[j] = stack
            else:
                stack = 0
        score[i] = sum(is_correct)
    ans = max(score) - min(score)
    print(f'#{tc} {ans}')

    # 처음엔 stack만 가지고 했지만, 이를 포문 바깥에 두어서, 계속 답이 안맞는 이슈가 발생
    # -> is_correct 배열을 새로 만들어서 입력이 잘 되고 있는지 확인하면서 문제를 다시 풀었음





import sys
sys.stdin = open('4466_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    #print(arr)

    arr.sort(reverse=True)
    #print(arr)

    final_grade = [] # 최종 점수를 입력할 배열

    for subject in range(K):
        final_grade.append(arr[subject])

    result = sum(final_grade)
    print(f'#{tc} {result}')

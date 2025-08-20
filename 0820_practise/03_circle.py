import sys
sys.stdin = open('03_input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    N = int(N)
    M = int(M)
    arr = list(map(int, input().split()))

    # M번 회전 작업을 반복
    for _ in range(M):
        # 맨 앞의 원소(index 0)를 꺼내서 맨 뒤에 추가
        arr.append(arr.pop(0))

    # M번 회전 후, 맨 앞에 있는 원소를 출력
    print(f'#{tc} {arr[0]}')

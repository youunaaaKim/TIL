import sys
sys.stdin = open('switch_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N번까지의 리스트
    arr = [list(map(int, input().split())) for _ in range(2)]

    # 첫 번째 리스트와 두 번째 리스트가 값이 같아질 때 까지
    # 얼마나 바꿔야하는지 세는 변수
    count = -1
        # 1번부터 N번까지 번호가 붙어있고, i번 스위치를 조작하면 i번부터 N번까지의 전등의 켜짐/꺼짐 상태가 반대가 된다고 한다

    for switch in range(N):
        for i in range(switch, N):
            if arr[0][switch] != arr[1][switch]:
                # i 부터 N까지 0이면 1, 1이면 0
                if arr[0][i] == 0:
                    arr[0][i] = 1
                else:
                    arr[0][i] = 0
            count += 1
            if arr[0] == arr[1]:
                break
        print(f'#{tc} {count}')


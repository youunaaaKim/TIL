import sys
sys.stdin = open('20551_input.txt')

# 세 개의 상자
# [A, B, C] 개의 사탕이 들었음
# 각 상자의 사탕이 0이 아니며, A<B<C가 되도록 하는 최소 먹어야 하는 사탕
# 이를 만족할 수 없다면 -1 출력

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    print(arr)
    eat = 0
    for i in range(2,0,-1): # 배열을 돌면서
        while arr[i - 1] >= arr[i]: # 앞 숫자가 큰 "동안" (애초에 조건에 맞으면 안걸림)
            arr[i - 1] -= 1 # 사탕을 한개씩 먹기
            eat += 1 # 먹은 사탕 수를 증가시키기

            # 사탕을 먹으면서 사탕 바구니의 사탕이 0보다 작아지면 실패
            if arr[i - 1] <= 0:
                eat = -1 # 실패의 의미로 eat = -1
                break # while 문 종료

        if eat == -1: # 그리고 eat 이 -1 이면
            break # for 문 종료

    for i in range(2): # 완성된 배열을 돌면서
        if arr[i] != 0: # 사탕 바구니가 0이 아니고
            if arr[0] < arr[1] < arr[2]: # 차례대로 증가한다면
                print(f'#{tc} {eat}') # 사탕 몇 개 먹었는지 출력
                break
            else:
                print(f'#{tc} -1') # 차례대로 증가 안하면 -1 출력
                break



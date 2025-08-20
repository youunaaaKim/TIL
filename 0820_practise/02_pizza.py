# 피자는 순서대로 들어감
# 첫 회전때 반절로 치즈 줄음
# 두 번째 회전 때 0//2로 치즈 양 줄음음
# 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램을 작성하시오.

import sys
sys.stdin = open('02_input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    N = int(N) # 화덕의 크기
    M = int(M) # 피자의 치즈의 양
    #print(N)
    Ci = list(map(int, input().split()))
    #print(Ci)



    # queue, left 리스트 활용하기
    # 먼저 큐에서 피자의 치즈 녹는거 계산하기
    # 피자 녹으면 새로운 피자 넣기
    # 맨 마지막 남은 피자 확인

    # 빈 리스트를 큐로 사용
    queue = []
    # 남은거 저장할 리스트
    left = []

    for i in range(N):
        queue.append([Ci[i], i+1]) # N의 크기만큼 큐에 피자 넣기. 인덱스 번호 +1 과 같이~
    # print(queue)

    for i in range(N, M): # N부터 M 까지의 크기만큼 큐에 피자 넣기 인덱스 번호 +1 과 같이~
        left.append([Ci[i], i + 1])
    # print(left)

    # 첫 턴은 큐의 숫자들을 1/2 하기
        # 만약 0 이하가 되었다면
            # 남은 피자 넣기
    # 피자가 하나 남을 때 까지
    # 큐의 숫자들을 1//2 하기
        # 만약 0 이하가 되었다면
            # 남은 피자 넣기


    # 첫 번째 턴은 그냥 1/2
    for _ in range(len(queue)):
        cheese, num = queue.pop(0)  # 맨 앞 피자 꺼내기
        cheese = cheese / 2  # 치즈 반으로 줄이기 (정수 나눗셈)
        if cheese == 0: # 치즈가 0이면
            if left:
                queue.append(left.pop(0))  # 새로운 피자 넣기
            # 치즈 0이고 left 없으면 제거
        else: # 치즈가 0이 아니면
            queue.append([cheese, num])  # 다시 뒤에 넣기

    # 두 번째 턴은 피자가 하나만 남을 때 까지 1//2
    while len(queue) > 1:
        cheese, num = queue.pop(0)
        cheese = cheese // 2
        if cheese == 0:
            if left:
                queue.append(left.pop(0))
        else:
            queue.append([cheese, num])
    # print(queue)
    print(f'#{tc} {queue[0][1]}')

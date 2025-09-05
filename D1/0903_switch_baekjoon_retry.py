'''
학생이 받은 수 num
남학생 : 학생별로 받은 num의 배수의 인덱스 위치의 스위치를 조작
여학생 : num의 인덱스 위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서 그 구간에 속한 스위치의 상태를 모두 바꾼다.
이때 구간에 속한 스위치의 개수는 항상 홀수
조건에 어긋나면 그 위치의 스위치만 바꿈
'''

import sys
sys.stdin = open('switch_bj.txt')

for tc in range(1):
    N = int(input()) # 스위치 개수
    switch = list(map(int, input().split())) # 스위치 상태
    M = int(input()) # 학생 수
    stu = [list(map(int, input().split())) for _ in range(M)] # 학생의 성별과 학생이 받은 수
    # print(switch)
    # print(stu)


    # 스위치 배열에 대해서, 남자일 경우 배수 스위치 조작, 여자일 경우 대칭 확인 후 조작
    for j in range(len(stu)): # 학생의 성별과 학생이 받은 수를 탐색하는 포문
        l = stu[j][1] # 학생이 받은 숫자
        # 남성이라면
        if stu[j][0] == 1:
            # l의 배수에 해당하는 스위치 인덱스의 값을 확인
            # 배수 스위치 조작하기 -> 1이면 0, 0이면 1
            for q in range(1, N+1): # 스위치의 길이까지 포문을 돌면서(스위치는 1부터 시작)
                idx = l * q - 1 # 받은 숫자의 배수 위치
                if idx >= N: # 배수가 N을 넘어가면 안됨
                    break
                if switch[idx] == 1: # 1이면 0으로 바꿔주고, 0이면 1로 바꾸기
                    switch[idx] = 0
                else:
                    switch[idx] = 1
        # 여성이라면
        else:
            # 양 옆의 숫자가 동일하다면 그 옆까지 숫자 보기
            # 양 옆의 숫자만 동일하면 양 옆만 바꾸기
            # 모두 다르면 그 위치 스위치만 바꾸기
            pos = stu[j][1] - 1  # 받은 수 => 입력 받은 스위치 번호는 1부터 시작, 내 인덱스는 0부터 시작

            # 범위 넘어가는지 체크하면서 대칭 비교
            # 바로 양 옆에 스위치가 스위치 숫자를 벗어나지 않고, 대칭이라면
            # 대칭인 최대 거리 저장
            max_k = 0  # 대칭 가능한 최대 거리
            for k in range(N//2+1):
                if pos - k < 0 or pos + k >= N:
                    break # 인덱스 범위를 벗어나면 중단
                if switch[pos - k] != switch[pos + k]:
                    break  # 대칭이 깨졌다면 거기까지만
                max_k = k # 여기까지만 확인하고 대칭인 거리 확인하고 포문 나오기
            for idx in range(pos - max_k, pos + max_k + 1): # 대칭인 만큼만 인덱스 위치 확인하기
                if switch[idx] == 0: # 1이면 0으로 바꿔주고, 0이면 1로 바꾸기
                    switch[idx] = 1
                else:
                    switch[idx] = 0

    for i in range(len(switch)):
        print(switch[i], end=' ')
        # 스위치의 길이
        if i % 20 == 19:
            # 20의 배수 -1 이 되면 줄바꿈하기
            print()








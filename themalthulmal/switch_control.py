'''
N개의 전등이 설치되어 있다. 각 전등은 1번부터 N번까지 번호가 붙어있고,
i번 스위치를 조작하면 i번부터 N번까지의 전등의 켜짐/꺼짐 상태가 반대가 된다고 한다.
모든 전등의 현재 상태와 스위치 조작 후 상태가 주어지면 최소 몇 개의 스위치를 조작해야 하는지 알아내는 프로그램을 만드시오.

시나리오
앞에서부터 확인하고 고치고의 과정
계속 확인하고 고치고
확인하고 고치고

같아질 때 까지
확인하고 고치는 함수를 작성해보자!
'''

import sys
sys.stdin = open('switch_input.txt')


def check_and_switch(arr):
    '''
    :param arr: 배열을 받기
    배열의 양쪽을 확인하고 같은 인덱스의 값이 다르다면 두 번째 인덱스를 스위치 하는 함수
    :return: 바뀐 두 번째 인덱스를 포함한 arr
    '''
    #인덱스의 값이 다르다면
    count = 0 # 스위치 키고 끄는 횟수
    while arr[0] != arr[1]: # 첫 번째, 두 번째 리스트의 값이 다를 때 while문 돌기
        for i in range(len(arr[0])): # arr[0]의 리스트 길이만큼 돌 때
            if arr[0][i] != arr[1][i]: # 0번째 리스트의 i 위치의 값과, 1번째 인덱스의 i 위치의 값이 다를 때
            # 스위치
                if arr[1][i] == 1: # 1이면 0
                    arr[1][i] = 0
                else:
                    arr[1][i] = 1 # 0이면 1
        count += 1 # 스위치 한 갯수 세기
    return count # 스위치 한 갯수 리턴


T = int(input()) # 테스트케이스 수
for tc in range(1, T+1):
    N = int(input()) # 스위치 갯수
    arr = [list(map(int, input().split())) for _ in range(2)] # 조작 전 스위치 상태와 조작 후 스위치 상태

    # 첫 번째 리스트와 두 번째 리스트가 값이 같아질 때 까지
    result = check_and_switch(arr) # 함수

    print(f'#{tc} {result}')

    # 1. 자꾸 카운트 갯수가 맞지 않는 문제 발생
    # 왜냐면 위의 코드는 첫 번째, 두 번째 리스트가 동일하지 않으면 i로 돌면서 두 번째 리스트를 다 바꿈,, 근데 왜 무한반복 안될까?
    # 2. 와일문 안써도 됨 앞에서부터 그냥 포문으로 비교해도 됨

import sys
sys.stdin = open('switch_input.txt')


def check_and_switch(arr):
    '''
    :param arr: 배열을 받기
    배열의 양쪽을 확인하고 같은 인덱스의 값이 다르다면 두 번째 인덱스를 스위치 하는 함수
    :return: 바뀐 두 번째 인덱스를 포함한 arr
    '''
    #인덱스의 값이 다르다면
    count = 0 # 스위치 키고 끄는 횟수
    L = len(arr[0])
    for i in range(L): # arr[0]의 리스트 길이만큼 돌 때
        if arr[0][i] != arr[1][i]: # 0번째 리스트의 i 위치의 값과, 1번째 인덱스의 i 위치의 값이 다를 때
            # i 위치 부터 len(arr[0])의 위치의 값까지 스위치
            for j in range(i, L):
                if arr[1][j] == 1: # 1이면 0
                    arr[1][j] = 0

                else:
                    arr[1][j] = 1 # 0이면 1
            count += 1

    return count # 스위치 한 갯수 리턴


T = int(input()) # 테스트케이스 수
for tc in range(1, T+1):
    N = int(input()) # 스위치 갯수
    arr = [list(map(int, input().split())) for _ in range(2)] # 조작 전 스위치 상태와 조작 후 스위치 상태

    # 첫 번째 리스트와 두 번째 리스트가 값이 같아질 때 까지
    result = check_and_switch(arr) # 함수

    print(f'#{tc} {result}')

# check_and_switch에서 arr[1]을 직접 수정하고 있어서,
# 나중에 다른 테스트케이스를 돌릴 때 원본 데이터가 이미 바뀌어 있는 상태로 시작될 수 있습니다.
# arr을 깊은 복사를 사용하면 안전합니다. arr_copy = [row[:] for row in arr]
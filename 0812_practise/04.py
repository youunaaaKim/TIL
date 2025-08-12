import sys
sys.stdin = open('04_input.txt')


def push(item):
    '''스택에 item을 삽입합니다.'''
    s.append(item)

def pop():
    '''스택의 top(마지막 원소)을 제거하고 반환합니다.'''
    if len(s) == 0:  # 공백 스택 검사
        # underflow 상황
        return None
    else:
        return s.pop()  # 마지막 원소 반환 및 제거

def is_empty():
    '''스택이 비어 있으면 True, 그렇지 않으면 False를 반환합니다.'''
    return len(s) == 0

def peek():
    '''스택의 top(마지막 원소)을 반환하되, 제거하지 않습니다.'''
    if not is_empty():
        return s[-1]
    return None

T = int(input())
for tc in range(1, T + 1):
    # 빈 스택 생성
    s = []

    arr = list(input()) # 문제 입력 받기
    for i in range(len(arr)):
		    # 스택이 비어있지 않고, 스택의 마지막 원소와 arr의 현재 문자가 같으면
        if not is_empty() and peek() == arr[i]:
            pop()
        else:
            push(arr[i])

    # 완료된 문자열 출력
    print(f'#{tc} {len(s)}')
import sys

sys.stdin = open('03_input.txt')


def check_brackets(string):
    '''
    여러 종류의 괄호 ((), [], {})와 숫자가 섞인 문자열에서
    괄호 짝이 올바른지 스택을 통해 검사한다.
    '''
    stack = []

    for char in string:
        # 여는 괄호 -> 스택에 push
        if char in '([{':
            stack.append(char)

        # 닫는 괄호 -> 스택에서 pop 후 매칭 확인
        elif char in ')]}':
            # pop하기 전에 스택이 비어있는지 확인 / 비어있다면 짝 불일치
            if len(stack) == 0:
                return -1

            # 스택이 비어있지 않다면 pop 진행
            top_char = stack.pop()

            # 닫는 괄호와 pop해서 나온 여는 괄호를 비교
            # 그런데 비교를 했는데 짝이 맞지 않으면 그대로 종료
            if char == ')' and top_char != '(':
                return -1
            elif char == ']' and top_char != '[':
                return -1
            elif char == '}' and top_char != '{':
                return -1
        # 숫자나 기타 문자들은 무시
        else:
            continue

    # 모든 괄호를 처리 후, 스택이 비어 있어야만 올바른 짝
    if len(stack) == 0:
        return 1
    else:
        return -1


T = int(input().strip())
for tc in range(1, T + 1):
    line = input().strip()
    result = check_brackets(line)
    print(f'#{tc} {result}')

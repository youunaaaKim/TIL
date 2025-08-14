def get_precedence(op):
    """연산자의 우선순위를 숫자로 반환하는 함수"""
    if op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    else:  # 괄호 등 그 외의 경우는 가장 낮은 우선순위 부여
        return 0


def infix_to_postfix(expression):
    stack = []  # 연산자를 임시 저장할 스택
    result = []  # 최종 후위 표기법 결과를 담을 리스트

    # 입력된 중위 표기법 식을 토큰 단위로 순회
    for token in expression:
        # 1. 피연산자인 경우 (숫자나 알파벳)
        if token.isalnum():
            # 바로 결과 리스트에 추가
            result.append(token)

        # 2. 여는 괄호 '('인 경우
        elif token == '(':
            # 무조건 스택에 push
            stack.append(token)

        # 3. 닫는 괄호 ')'인 경우
        elif token == ')':
            # 스택의 top이 여는 괄호가 될 때까지 모든 연산자를 pop하여 결과에 추가
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            # 루프가 끝나면 스택 top은 '(' 이므로, 이를 pop하여 버림
            stack.pop()

        # 4. 연산자인 경우
        else:
            # 스택 top의 연산자 우선순위가 현재 연산자보다 높거나 같으면 계속 pop
            while (
                stack
                and stack[-1] != '('
                and get_precedence(stack[-1]) >= get_precedence(token)
            ):
                result.append(stack.pop())
            # 위 조건을 만족하지 않으면(자기보다 우선순위가 낮은 연산자를 만나면)
            # 현재 연산자를 스택에 push
            stack.append(token)

    # 5. 마지막으로 스택에 남아있는 모든 연산자를 결과에 추가
    while stack:
        result.append(stack.pop())

    # 결과 리스트를 하나의 문자열로 합쳐서 반환
    return ''.join(result)


# 테스트
expr1 = '(A+B)*C'
expr2 = '(A+B)*(C-D)'
print(infix_to_postfix(expr1))  # "AB+C*"
print(infix_to_postfix(expr2))  # "AB+CD-*"

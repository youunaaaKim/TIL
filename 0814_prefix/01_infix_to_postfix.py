def infix_to_postfix(expression):
    # 각 연산자의 우선순위를 딕셔너리로 정의
    precedence = {
        '+' : 1,
        '-' : 2,
        '*' : 2,
        '/' : 2,
    }

    # 연산자를 임시로 저장할 스택
    stack = []
    #최종 후위 표기법 결과를 담을 리스트 정의
    result = []

    # 입력되는 중위 표기법 식을 토큰 단위로 순회 # 중위표기법을 후위표기법으로 변환하는 방법 참고(노션)
    for token in expression:
        # 1. 피연산자(숫자, 문자)일 경우
        if token.isalnum(): # True / False
            # 바로 결과 리스트에 추가
            result.append(token)
        # 2. 여는 괄호 '('인 경우 무조건 스텍에 push
        elif token == '(':
            # 우선순위와 상관없이 무조건 스택에 push
            stack.append(token)
        # 3. 닫는 괄호 ')'인 경우
        # 왼쪽 괄호를 만나기 전까지 스텍에서 pop 하여 출력
        elif token == ')':
            # 스택 top이 여는 괄호가 될 때 까지 모든 연산자를 pop하여 결과에 추가
            # 스택이 비어있지 않고, top이 여는 괄호가 아닌 동안 반복
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            # 반복이 끝나면 스택 top은 '(' 여는 괄호이므로, 이를 pop하여 버림
            stack.pop()
        # 4. 연산자인 경우 - 우선순위 비교
        else:
            # 스텍에 top에 있는 연산자(isp) 우선순위와 현재 연산자 우선순위(icp) 비교
            # isp가 icp보다 높거나 같으면 계속 pop
            # stack이 비어있지 않고, top이 여는 괄호가 아니며, isp가 icp보다 높거나 같으면 pop
            while(
                stack
                and stack[-1] != '('
                and precedence.get(stack[-1]) >= precedence.get(token)
            ):
                result.append(stack.pop())
            # 위 조건을 만족하지 않으면 (자기(token)보다 우선순위가 낮은 연산자를 만나면)
            # 현재 연산자를 (token)를 스택에 push
            stack.append(token)

    # 5. 모든 토큰 처리가 끝난 후 스택에 남아있는 연산자 처리
    # 스택이 빌 때 까지 pop -> while
    while stack:
        result.append(stack.pop())


    # 6. 결과 리스트에 모든 요소를 하나의 문자열로 반환
    return ''.join(result)



# 테스트
expr1 = '(A+B)*C'
expr2 = '(A+B)*(C-D)'
print(infix_to_postfix(expr1))  # "AB+C*"
print(infix_to_postfix(expr2))  # "AB+CD-*"

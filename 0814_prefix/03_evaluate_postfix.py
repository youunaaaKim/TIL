def evaluate_postfix(expression):
    """
    후위 표기법으로 표현된 수식을 계산하여 결과를 반환하는 함수.

    Args:
        expression (str): 후위 표기법으로 작성된 문자열 (예: "53+2*")

    Returns:
        int or float: 수식의 최종 계산 결과
    """
    # 피연산자를 임시로 저장할 스택
    stack = []
    # 후위표기법 수식을 왼쪽 부터 순회
    for token in expression:
        # 1. 토큰이 숫자인 경우
        if token.isdigit():
            # 스택에 push(문자를 정수로 변환)
            stack.append(int(token))
        # 2. 토큰이 연산자인 경우
        # 스택에서 피연산자 2개를 pop
        else:
            # 중요! 먼저 꺼낸 것이 연산의 오른 쪽에  위치함
            right = stack.pop() # 두 번째 피연산자
            left = stack.pop() # 첫 번째 피연산자

            # 토큰에 따라서 적절한 연산 수행
            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                result = left / right
            elif token == '^':
                result = left**right
            else:
                # 정의되지 않은 연산자가 들어올 경우 처리
                raise ValueError('잘못된 연산자입니다.')
            # 연산 결과 result를 다시 스택에 push
            stack.append(result)
    # 모든 연산이 끝나면 스택에 마지막으로 남은 값 하나가 최종 결과
    return stack.pop()

# --- 실행 코드 ---
# (5 + 3) * 2 를 후위 표기법으로 표현
postfix_expr = "53+2*"
result = evaluate_postfix(postfix_expr)
print(f"'{postfix_expr}'의 계산 결과: {result}")  # '53+2*'의 계산 결과: 16

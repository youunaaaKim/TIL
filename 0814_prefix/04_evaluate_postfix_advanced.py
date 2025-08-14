# expression을 공백 기준으로 나눠 토큰 리스트를 생성
def evaluate_postfix_advanced(expression):
    tokens = expression.split()  # "12 3 +" -> ['12', '3', '+']
    stack = []

    # 분리된 토큰 리스트를 순회
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b

            stack.append(result)

    return stack.pop()


# 테스트
postfix_expr = "12 3 +"
result = evaluate_postfix_advanced(postfix_expr)
print(f"'{postfix_expr}'의 계산 결과: {result}")  # 15

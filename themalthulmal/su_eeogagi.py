# import sys
# N = input(sys.stdin.readline())
N = 100
max_length = 0
result_sequence = []
# 두 번째 수는 양의 정수 중에서 하나를 선택한다.

# 세 번째부터 이후에 나오는 모든 수는 앞의 앞의 수에서 앞의 수를 빼서 만든다.
# 예를 들어, 세 번째 수는 첫 번째 수에서 두 번째 수를 뺀 것
# 음의 정수가 만들어지면, 이 음의 정수를 버리고 더 이상 수를 만들지 않는다.
# 입력으로 첫 번째 수가 주어질 때, 이 수에서 시작하여 위의 규칙으로 만들어지는
# 최대 개수의 수들을 구하는 프로그램을 작성하시오. 최대 개수의 수들이 여러 개일 때,
# 그중 하나의 수들만 출력하면 된다.
# [시나리오]
# 두 번째 수는 N-1부터 1까지로 해서 뺀거 리스트에 넣고 길이 세기
# max 비교해서 업데이트

# 두 번째 수가 돌아갈 때
for i in range(N - 1, 0, -1):
    sequence = [N, i]
    # 음수 전까지 리스트 만들기
    while True:
        next_num = sequence[-2] - sequence[-1]
        if next_num < 0:
            break
        sequence.append(next_num)

    if len(sequence) > max_length:
        max_length = len(sequence)
        result_sequence = sequence

# 출력
print(max_length)
for i in result_sequence:
    print(i, end=' ')

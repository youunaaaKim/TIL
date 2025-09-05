def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i*n
    print(answer)


solution('hello', 3)
############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 len 함수를 사용하지 않습니다.
def longest_string(str_list):
    long_length = 0
    word = []

    for i in str_list:
        length = 0
        for j in i:
            length += 1

        if length > long_length:
            long_length = length
            word = i

    return word


    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(longest_string(['apple', 'banana', 'cherry', 'date']))  # 'banana'
print(longest_string(['cat', 'caterpillar', 'dog', 'elephant']))  # 'caterpillar'
print(longest_string(['a', 'ab', 'abc', 'abcd']))  # 'abcd'
#####################################################

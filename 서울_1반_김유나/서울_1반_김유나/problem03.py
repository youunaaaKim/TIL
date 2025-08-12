############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장 함수 sum, len, filter, 리스트 count 메서드 사용 시 감점
def defect_rate(results):
    sum_of_pass = 0
    sum_of_fail = 0
    for i in results:

        if i == 'fail':
            sum_of_fail += 1
        else :
            sum_of_pass += 1
    answer = float(sum_of_fail / (sum_of_pass + sum_of_fail))
    return answer
    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(defect_rate(['pass', 'fail', 'pass', 'fail']))   # 0.5
print(defect_rate(['pass', 'pass']))                   # 0.0
print(defect_rate(['fail', 'fail', 'fail']))           # 1.0
#####################################################
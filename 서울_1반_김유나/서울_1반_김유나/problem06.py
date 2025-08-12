############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def grade_distribution(scores):
    result = {}
    for student, score in scores.items():
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'

        if grade not in result:
            result[grade] = []  # ❗️최초 등장 시에만 초기화
        result[grade].append(student)  # 학생 추가

    return result
        
    # 여기에 코드를 작성하여 함수를 완성합니다.
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
case1 = {'Kim': 92, 'Lee': 75, 'Park': 88, 'Choi': 60}
# {'A': ['Kim'],  'C': ['Lee'], 'B': ['Park'], 'D': ['Choi']}
print(grade_distribution(case1))

print(grade_distribution({'Min': 95, 'Oh': 93}))       
# {'A': ['Min', 'Oh']}

case2 = {
    'Ahn': 90,   
    'Baek': 82,  
    'Choi': 75,  
    'Dong': 60,  
    'Eun': 59    
}
# {'A': ['Ahn'], 'B': ['Baek'], 'C': ['Choi'], 'D': ['Dong'], 'F': ['Eun']}
print(grade_distribution(case2))

case3 = {
    'Kim': 100,  
    'Lee': 89,   
    'Park': 70,  
    'Shin': 69,  
    'Yang': 0    
}
# {'A': ['Kim'], 'B': ['Lee'], 'C': ['Park'], 'D': ['Shin'], 'F': ['Yang']}
print(grade_distribution(case3))
#####################################################
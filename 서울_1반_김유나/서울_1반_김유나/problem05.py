############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# Python 내장 함수 sum, map 사용 시 감점

def calc_total(price_map, orders):
    '''
    주문한 물품의 총 금액을 정수로 반환하는 함수
    '''

    total_price = 0

    # 주문 목록 리스트에 있는 물건 순회
    for goods in orders:
        # 주문한 물품이 있을 경우
        if goods in price_map:
            # 금액을 더함
            total_price += price_map[goods]

    return total_price

    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(calc_total({'apple': 1000, 'pear': 800}, ['pear', 'apple', 'apple']))  # 2800
print(calc_total({'pen': 1200, 'note': 1500}, [])) # 0
print(calc_total({'apple': 1000, 'orange': 900, 'grape': 1200}, ['orange', 'orange'])) # 1800
#####################################################


import json  # JSON 데이터를 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로 처리를 위한 라이브러리


# 1. 파일 경로 설정
# pathlib을 사용하여 파일 경로를 설정

file_path = Path('data/books_20.json')


# 2. 파일 존재 여부 확인
# 파일이 존재하는지 확인하고, 존재하면 파일을 열어 JSON 데이터를 읽음

if file_path.exists(): # 파일 존재 여부 확인
    # 파일 열기
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file) # JSON 파일을 파이썬 딕셔너리로 변환


# 3. 정가 범위 분류
# 도서의 정가를 기준으로 범위를 분류하고, 각 범위에 해당하는 도서 제목을 저장

    price_categories = {
        "1만원 이상 2만원 미만": [],
        "1만원 미만": [],
        "2만원 이상": []
    }  # 정가 범위를 저장할 딕셔너리 생성

    for item in data['item']: # 'item' 리스트의 각 항목을 순회
        title = item['title']
        price = int(item['priceStandard'])

    # 정가를 분류하고 해당 범위에 도서 제목을 추가
    # 정가 범위 분류는 "1만원 이상 2만원 미만", "1만원 미만", "2만원 이상"

        if 10000 < price < 20000:
            price_categories["1만원 이상 2만원 미만"].append(title)
        elif price < 10000:
            price_categories["1만원 미만"].append(title)
        else:
            price_categories["2만원 이상"].append(title)


# 4. 결과 출력
# 분류된 정가 범위와 도서 제목을 출력

    print("정가 범위 분류:")
    for category, books in price_categories.items(): # 범위별 도서 출력
        print(f'{category}: ')
        for i in range(len(books)):
            print(f'  - {books[i]}') # 범위와 도서 제목 출력
        print('\n')


# 5. 파일이 없을 경우
# 파일이 존재하지 않으면 오류 메시지 출력

else:
    print(f"파일이 존재하지 않습니다: {file_path}")
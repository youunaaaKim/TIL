import json  # JSON 데이터를 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로 처리를 위한 라이브러리

# 1. 파일 경로 설정
# pathlib을 사용하여 파일 경로를 설정합니다.
file_path = Path('data/books_20.json')  # JSON 파일 경로 설정

# 2. 파일 존재 여부 확인
# 파일이 존재하는지 확인하고, 존재하면 파일을 열어 JSON 데이터를 읽습니다.
if file_path.exists():  # 파일이 존재할 경우
    # 파일 열기
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file)
        # print(type(data))  # JSON 파일을 파이썬 딕셔너리로 변환하는 코드 (json.load)

    # 3. 도서 가격 리스트 생성
    # 'item' 리스트의 각 항목을 순회하며 도서 가격을 추출하여 리스트에 추가합니다.
    book_prices = []  # 도서 가격을 저장할 빈 리스트
    for item in data['item']:  # 'item' 리스트의 각 항목을 순회
        book_prices.append(item['priceSales']) # 'priceSales' 값을 리스트에 추가하는 코드 (book_prices.append)
        

    # 4. 평균 가격 계산
    # 도서 가격 리스트의 평균을 계산합니다.
    average_price = sum(book_prices) / len(book_prices)  # 평균 가격을 계산하는 코드 (sum(book_prices) / len(book_prices))

    # 5. 결과 출력
    # 계산된 평균 가격을 출력합니다.
    print(f"도서 평균 가격: {average_price:.2f}원")

else:
    # 6. 파일이 없을 경우 처리
    # 파일이 존재하지 않으면 오류 메시지를 출력합니다.
    print(f"파일이 존재하지 않습니다: {file_path}")  # 파일이 존재하지 않을 때의 처리 코드 (print(f"파일이 존재하지 않습니다: {file_path}"))

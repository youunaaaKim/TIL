from datetime import datetime  # 날짜와 시간을 처리하기 위한 라이브러리
import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리

# 1. 파일 경로 설정
# pathlib을 사용하여 파일 경로를 설정합니다.
file_path = Path('data/books_2000.json')  # JSON 파일 경로 설정

# 2. 파일 존재 여부 확인
# 파일이 존재하는지 확인하고, 존재하면 파일을 열어 JSON 데이터를 읽습니다.
if file_path.exists():  # 파일이 존재할 경우
    # 파일 열기
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file)  # JSON 파일을 파이썬 딕셔너리로 변환하는 코드 (json.load)

    # 3. 월별로 도서 분류

        monthly_books = {}  # 월별 도서 가격을 저장할 빈 딕셔
        for item in data: # 'item' 리스트의 각 항목을 순회
            pubDate = item['pubDate']
            priceSales = item['priceSales']
            # 출판일에서 월 추출 (YYYY-MM-DD 형식 가정)

            try:
                month = int(datetime.strptime(pubDate, '%Y-%m-%d').strftime('%m')) # 날짜 형식 변환
            except ValueError:
                continue

            # 월별로 가격 저장

           
            if month not in monthly_books:
                monthly_books[month] = []
            monthly_books[month].append(priceSales)


    # 4. 결과 출력 (월별 도서 수)
        for month, priceSales in sorted(monthly_books.items()):
         # 월별 도서 가격 평균 계산
            average_price = sum(priceSales) / len(priceSales)
            average_price = round(average_price, 2)




            print(f"{month}월: 평균 가격 {average_price}원 (총 {len(priceSales)}권)")

else:
    # 5. 파일이 없을 경우 처리
    # 파일이 존재하지 않으면 오류 메시지를 출력합니다.
    print(f"파일이 존재하지 않습니다: {file_path}")




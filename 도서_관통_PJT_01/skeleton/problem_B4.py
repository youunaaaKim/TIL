from datetime import datetime  # 날짜와 시간 처리를 위한 라이브러리
import json  # JSON 데이터를 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로 처리를 위한 라이브러리

# 1. 파일 경로 설정
# pathlib을 사용하여 파일 경로를 설정합니다.
file_path = Path("data/books_500.json")  # JSON 파일 경로 설정

# 2. 파일 존재 여부 확인
# 파일이 존재하는지 확인하고, 존재하면 파일을 열어 JSON 데이터를 읽습니다.
if file_path.exists():  # 파일이 존재할 경우
    # 파일 열기
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file)# JSON 파일을 파이썬 딕셔너리로 변환하는 코드 (json.load)  
        

     # 3. 출판일을 기준으로 최신 도서 10개 추출 (hint: 출판일 :pubDate.  sorted 함수 key 속성)
        books_with_date = []
        for item in data:
            title = item.get('title')
            pubDate = item.get('pubDate') # 'item' 리스트의 각 항목을 순회

            try:
                pub_date_form_changed = datetime.strptime(pubDate, "%Y-%m-%d") # 날짜 형식 변환
            except ValueError:
                continue
            books_with_date.append((title, pub_date_form_changed))

        books_with_date.sort(key=lambda x:x[1], reverse=True)
        latest_books = books_with_date[:10]

    # 4. 결과 출력
    print("최신 도서 10개:")
    for book in latest_books:
        print(f'{book[0]} - {book[1].strftime("%Y-%m-%d")}')
          # 선택된 도서를 순회하며 출력

else:
    print(f"파일이 존재하지 않습니다: {file_path}")
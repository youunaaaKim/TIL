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


# 3. 책 제목 리스트 생성
# 'item' 항목을 순회하며 각 도서의 'title' 값을 리스트에 추가

    book_titles = [] # 책 제목을 저장할 빈 리스트 생성

    for item in data['item']: # 'item' 리스트에서 각 항목을 순회
        book_titles.append(item['title']) # 책 제목을 리스트에 추가


# 4. 결과 출력
# 리스트에 저장된 책 제목 출력

    print(f"책 제목 리스트:\n{book_titles}")


# 5. 파일이 없을 경우
# 파일이 존재하지 않으면 오류 메시지 출력

else:
    print(f"파일이 존재하지 않습니다: {file_path}")
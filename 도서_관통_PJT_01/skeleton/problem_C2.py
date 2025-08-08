import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리

# 1. 파일 경로 설정
# pathlib을 사용하여 파일 경로 설정
file_path = Path('data/books_500.json')


# 2. 파일 존재 여부 확인
# 파일이 존재하는지 확인하고, 존재하면 파일을 열어 JSON 데이터를 읽음

if file_path.exists(): # 파일 존재 여부 확인
    # 파일 열기
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file) # JSON 파일을 파이썬 딕셔너리로 변환

# 파일이 존재하지 않으면 오류 메시지 출력

else:
    print(f"파일이 존재하지 않습니다: {file_path}")
    data = [] # 파일이 없을 경우 빈 리스트로 초기화하여 오류 방지


# 3. categoryId와 categoryName을 기준으로 정보 분류

categorized_books_data = {} # 각 카테고리별로 필요한 도서 정보를 저장할 딕셔너리 생성

for book in data:
    categoryId = book.get('categoryId')
    categoryName = book.get('categoryName')

    if categoryId is not None and categoryName is not None:

        if categoryId not in categorized_books_data:
            categorized_books_data[categoryId] = {
                "name": categoryName,
                "books": []
            }
        
# 각 도서에서 필요한 정보만 추출

        extracted_info = {
            "title": book.get("title"),
            "author": book.get("author"),
            "publisher": book.get("publisher"),
            "pubDate": book.get("pubDate"),
            "isbn": book.get("isbn"),
            "price": book.get("priceStandard")
        }
        # 추출된 정보를 'books' 리스트에 추가
        categorized_books_data[categoryId]["books"].append(extracted_info)


# 4. 모든 분류된 도서 정보를 하나의 JSON 파일로 저장

output_file_name = 'category_books.json'
output_file_path = Path(f'data/{output_file_name}')


# 5. 최종적으로 준비된 데이터를 JSON 파일로 저장

with output_file_path.open('w', encoding='utf-8') as outfile:
    json.dump(categorized_books_data, outfile, ensure_ascii=False, indent=4)

print(f"JSON 파일이 생성되었습니다: {output_file_name}")
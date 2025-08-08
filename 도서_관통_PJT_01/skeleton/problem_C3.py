from pathlib import Path
import json

# 1. 파일 경로 설정
# pathlib을 사용하여 파일 경로를 설정

file_path = Path('data/books_500.json')

# 파일 존재 여부 확인
if file_path.exists():
    with open(file_path, encoding='utf-8') as f:
        books = json.load(f)

    # 시리즈 정보를 기준으로 책 묶기
    series_dict = {}

    for book in books:
        series = book.get('seriesInfo')
        if series:
            series_id = series.get('seriesId')
            if series_id not in series_dict:
                series_dict[series_id] = {
                    'seriesId': series.get('seriesId'),
                    'seriesName': series.get('seriesName'),
                    'books': []
                }
            series_dict[series_id]['books'].append(book)

    # 결과 저장 (예: data/series_books.json)
    output_path_name = 'series.json'
    output_path = Path(f'data/{output_path_name}')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(series_dict, f, ensure_ascii=False, indent=2)

    print(f"모든 시리즈 데이터가 {output_path_name} 파일로 병합되었습니다.")

else:
    print(f"파일이 존재하지 않습니다: {file_path}")

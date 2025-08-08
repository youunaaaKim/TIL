import json
from pathlib import Path


# JSON 파일로 저장하기
data = {
    'name': '파일 저장하기',
    'value': 20
}

# dumps 사용 (dictionary를 json 문자열로 변환)
json_string = json.dumps(data, ensure_ascii=False, indent=4)

# JSON 파일을 생성
new_json_1 = Path('sample_data/sample1.json')
new_json_1.write_text(json_string, encoding='utf-8')


# dump 사용 (직접 dictionary를 JSON 파일로 저장할 때 사용)
new_json_2 = Path('sample_data/sample2.json')
with new_json_2.open('w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
    

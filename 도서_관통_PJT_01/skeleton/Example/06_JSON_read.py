import json
from pathlib import Path


# JSON 파일 읽어오기
json_file = Path('sample_data/books_20.json')

json_text = json_file.read_text(encoding='utf-8')  # JSON은 문자열
print(type(json_text))  # <class 'str'>

# loads 사용 (JSON 문자열을 변환할 때 사용)
data = json.loads(json_text) #  변환
print(type(data))  # <class 'dict'>

# load 사용 (JSON 파일에서 바로 읽어와서 변환할 때 사용)
json_file = Path('sample_data/books_20.json')
with json_file.open(encoding='utf-8') as json_file:
    data = json.load(json_file)
    print(type(data))   # <class 'dict'>

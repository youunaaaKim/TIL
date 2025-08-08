from pathlib import Path


file_path = Path('new_directory/new.md')

# Text를 바로 가져오는 방법
print(file_path.read_text(encoding='utf-8'))

# open 메서드를 이용한 방법
with file_path.open('r', encoding='utf-8') as file:
    print(file)   # <_io.TextIOWrapper name='new_dir\\new.md' mode='r' encoding='utf-8'> 
    print(file.read())


# 한 줄씩 라인 별로 읽어 오기
with file_path.open('r', encoding='utf-8') as file:
    print(file.readline()) # # 새로 만들기
    print(file.readline()) # * First line


# 텍스트를 리스트로 가져오기
with file_path.open('r', encoding='utf-8') as file:
    print(file.readlines()) # ['# 새로 만들기\n', '* First line\n', '* Second line\n', '* Third line\n']

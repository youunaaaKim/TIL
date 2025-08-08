from pathlib import Path


# 폴더 생성
# exist_ok : True (폴더가 존재할 경우 에러 발생하지 않음)
new_dir = Path('new_directory')
new_dir.mkdir(exist_ok=True)

# 파일 생성
Path('new_file.txt').write_text("Hello, World!")

# 새로만든 폴더 내부에 파일 생성
new_file = new_dir / 'new.md'
new_file.write_text('# 새로 만들기', encoding='utf-8')

# 작성된 파일에 이어서 여러 줄 쓰기
with new_file.open('a', encoding='utf-8') as file:
    file.write('\n')
    file.write('* First line\n')
    file.write('* Second line\n')
    file.write('* Third line\n')
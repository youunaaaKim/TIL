from pathlib import Path
# 현재 위치의 파일 목록 보기
current_path = Path.cwd()

print(current_path.iterdir()) # <generator object Path.iterdir at 0x000001F6010147B0>
# 반복문을 이용해 내용 확인하기
for item in current_path.iterdir():
    print(item)             # 파일/폴더
    print(item.name)        # 파일/폴더 이름만 출력
    print('-----')

# 파일/폴더 여부 확인
for item in current_path.iterdir():
    if item.is_file():
        print(f'파일 : {item.name}')
    elif item.is_dir():
        print(f'폴더 : {item.name}')
    else:
        print(item.name)

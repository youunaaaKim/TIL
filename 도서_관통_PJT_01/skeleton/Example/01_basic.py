
from pathlib import Path


# 경로 다루기 

# 현재 작업 디렉토리
current_path = Path.cwd()
print(f'현재 작업 경로 : {current_path}')

# 홈 디렉토리
home_path = Path.home()
print(f'홈 디렉토리 : {home_path}')

# 특정 경로
specific_path = Path('home/user/documents/file.txt')
print(f'특정 경로 : {specific_path}')

# 경로 결합 하기
new_path = Path('documents') / 'subfolder' / 'file.txt'
print(f'경로 합치기 : {new_path}')


# 파일 다루기

# 파일명만 확인하기
file_name = specific_path.name
print(f'파일명 확인 : {file_name}')

# 파일 확장자를 제외한 이름
stem = specific_path.stem
print(f'파일명 확인 : {stem}')

# 파일 확장자
suffix = specific_path.suffix
print(f'파일 확장자 확인 : {suffix}')


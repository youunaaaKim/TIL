from pathlib import Path

current_path = Path.cwd()

# 특정 패턴의 파일 찾기
for python_file in current_path.glob('*.py'):
    print(python_file.name)


# 재귀적으로 모든 하위 디렉토리 검색
for file in current_path.rglob('*.txt'):
    print(file.name)

# 응용하기
# 언더스코어가 1개를 가지는 파일 리스트 생성하기
result = []
for file in current_path.rglob('*_*'):  # 언더스코어를 가진 모든 파일, 폴더 검색
    if file.is_file() and file.name.count('_') == 1:   # 파일이면서 언더스코어가 1개라면
        result.append(file.name)     # 결과에 담기

print(result)
from pathlib import Path

# Aboslute path
# relative path

p = Path("emails")
exists = p.exists()
print(exists)

if not exists:
    p.mkdir()

exists = p.exists()
print(exists)

if exists:
    p.rmdir()

exists = p.exists()
print(exists)

path = Path()
print(path.glob('*.py'))

for file in path.glob('*.py'):
    print(file)

for file in path.glob('*'): # all files in directory
    print(file)


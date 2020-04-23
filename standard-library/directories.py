from pathlib import Path

path = Path("../modules/ecommerce")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# print(path.exists())
print(path.iterdir())

for p in path.iterdir():
    print(p)

# path = [p for p in path.iterdir()]

path = [p for p in path.iterdir() if p.is_dir()]
# py_file = [p for p in path.glob("*.py")]
# py_file = [p for p in path.rglob("*.py")]
print(path)
# print(py_file)

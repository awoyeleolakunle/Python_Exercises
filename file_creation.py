import pathlib
from pathlib import Path


file_path = pathlib.Path("c:/my_folder/my_file.txt")
file_path = Path.cwd() / "My_folder"
file_path.mkdir(exist_ok=True)
new_file_path = file_path/"my_file.txt"
new_file_path.touch(exist_ok=True)
print(file_path.exists())
print(file_path.name)
print(new_file_path.name)
print(new_file_path.parent.name)
print(file_path.parent.name)
#file_path = "babygirl"
#print(f"{file_path.replace('b', 'M')}")

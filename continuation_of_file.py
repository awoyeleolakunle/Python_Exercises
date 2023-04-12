import pathlib
from pathlib import Path

path1 = pathlib.Path.cwd()
folder_a = path1 / "folder_a"
folder_a.mkdir(exist_ok=True)

file_paths = [
    folder_a / "private.img",
    folder_a / "lyrics-txt",
    folder_a / "alone.vid",

]

for path in file_paths:
    path.touch()
# print(folder_a)
# print(file_paths)
# for file in folder_a.iterdir():
# print(file.name)

for file in path1.iterdir():
    print(file.name)
# for files in path1.glob("*.py"):
# print(files.name)


# source = path1 / "my_practice_folder" / "file_for_practice"
# destination = path1 / "folder_a" / "file_for_practice"
# source.replace(destination)
# print(source)
source = path1/"prof"/"folder_a"/"file_for_practice"
print(source.name)
destination = path1/"my_practice_folder"/"file_for_practice"
source.replace(destination)

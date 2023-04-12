import pathlib
from pathlib import Path

practice_file_creation = pathlib.Path("c:/my_practice_folder/file_for_practice")
practice_file_creation = Path.cwd() / "my_practice_folder"
practice_file_creation.mkdir(exist_ok=True)
print(practice_file_creation.exists())
new_file = practice_file_creation/"file_for_practice"
new_file.touch(exist_ok=True)
print(new_file.exists())
print(new_file.name)
print(practice_file_creation.name)





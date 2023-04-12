import pathlib
from pathlib import Path


def file_maker():
    empty_list = []

    precious_file = pathlib.Path.cwd()
    new_precious_file_folder = precious_file / "new_precious_file"
    new_precious_file_folder.mkdir(exist_ok=True)

    new_file_precious = new_precious_file_folder / "new_file_precious"
    new_file_precious.touch()

    new_file_precious.write_text("The Lord is my shepherd")

    my_text = new_file_precious.read_text()

    b = my_text.split(" ")
    print(b)

    for word in my_text:
        empty_list.append(word)

    return empty_list


print(file_maker())


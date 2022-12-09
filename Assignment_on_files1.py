import pathlib
from pathlib import Path

assignment_for_file = pathlib.Path.home()
my_folder = assignment_for_file/"my_folder"
my_folder.mkdir(exist_ok=True)
print(my_folder.exists())



inner_files = [
    my_folder / "file1.txt",
    my_folder / "file2.txt",
    my_folder / "image1.png"

                    ]
for path in inner_files:
    path.touch()
    print(inner_files)
for files in my_folder.iterdir():
    print(files.name)

images_folder = my_folder/"images_folder"
images_folder.mkdir(exist_ok=True)
print(images_folder.exists())

source =Path(r'C:/Users/ADMIN/my_folder/image1.png')
print(source.exists())
destination =Path(r'C:/Users/ADMIN/my_folder/images_folder/image1.png')
print(destination.exists())
source.replace(destination)
delete_file = my_folder/"file1.txt"
delete_file.unlink()
delete_images_folder = my_folder/images_folder/"image1.png"
delete_images_folder.unlink()
delete_file2 = my_folder/"file2.txt"
delete_file2.unlink()
delete_images_folder_now = my_folder/"images_folder"
delete_images_folder_now.rmdir()
delete_my_folder = path.home()/"my_folder"
print(my_folder.parent)
delete_my_folder.rmdir()




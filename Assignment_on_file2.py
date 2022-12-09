import pathlib
from pathlib import Path

assignment_folder = pathlib.Path.home()
practice_files_folder = assignment_folder/"practice_files_folder"
practice_files_folder.mkdir(exist_ok=True)
print(practice_files_folder.exists())

document = practice_files_folder/"document"
document.mkdir(exist_ok=True)
print(document.parent.name)

sub_folder = practice_files_folder/"sub_folder"
sub_folder.mkdir(exist_ok=True)
print(sub_folder.parent.name)

images = practice_files_folder/"images"
images.mkdir(exist_ok=True)
print(images.parent.name)

new_images_file =[
    images/"image1.png",
    images/"image2.gif",
    images/"image3.png",
    images/"image4.jpg"

]

for path in new_images_file:
    path.touch()
    print(new_images_file)

for files in images.iterdir():
    print(files)





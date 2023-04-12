import pathlib
from pathlib import Path


#fake_path = Path.home()
#print(fake_path)

#fake_path = Path.cwd()
#print(fake_path)


#path = pathlib.Path("c:/chohort14/hisGrace")
#print(path.is_absolute())

#fake_path = pathlib.Path("c:\kelloyes\hello.txt")
#print(fake_path)

fake_path = pathlib.Path("c:/cohort14/private.img")
cwd_path = Path.cwd()
fake_path = Path.cwd()/"prof"
fake_path.mkdir()
new_file= fake_path.touch()
#print(cwd_path)
#print("parent -", cwd_path.parent)
#print(fake_path.parents)
#print("Anchor -", fake_path.anchor)

#print("name - ", fake_path.name)
#print("Suffix -", fake_path.suffix)
#print("Stem -", fake_path.stem)

#cwd_path.mkdir(exist_ok=  True)
#print("Exists? -", fake_path.exists())
#print(cwd_path.exists())





# create a path object

from pathlib import Path

file = Path("test.txt")

# check if file exists

from pathlib import Path

file = Path("test.txt")

print(file.exists())

# create a folder

from pathlib import Path

folder = Path("MyFolder")

folder.mkdir()

# create and write a file

from pathlib import Path

file = Path("test.txt")

file.write_text("Hello Python")

# read a file

from pathlib import Path

file = Path("test.txt")

data = file.read_text()

print(data)

# get a file name

from pathlib import Path

file = Path("documents/report.pdf")

print(file.name)

# get file extension

print(file.suffix)

# get file name without extension

print(file.stem)
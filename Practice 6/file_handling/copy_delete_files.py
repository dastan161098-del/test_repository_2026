#1
import shutil
import os

shutil.copy("sample.txt", "sample_copy.txt")

if os.path.exists("sample_copy.txt"):
    print("File copied successfully")

os.remove("sample_copy.txt")
print("Copy deleted")

#2
import shutil
import os

# Copy file
shutil.copy("sample.txt", "sample_copy.txt")
print("File copied")

# Backup file
shutil.copy("sample.txt", "sample_backup.txt")

# Delete file safely
file = "sample_copy.txt"

if os.path.exists(file):
    os.remove(file)
    print("File deleted")
else:
    print("File not found")
#1
import shutil

shutil.move("sample.txt", "test_folder/sample.txt")

print("File moved")

#2
import shutil

# Move file
shutil.move("sample.txt", "test_folder/sample.txt")

# Copy file to another directory
shutil.copy("fruits.txt", "test_folder/fruits_copy.txt")

print("Files moved/copied")
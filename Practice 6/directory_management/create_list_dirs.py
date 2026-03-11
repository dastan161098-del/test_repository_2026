#1
import os

os.makedirs("test_folder/subfolder", exist_ok=True)

files = os.listdir(".")
for f in files:
    print(f)

#2
import os

# Create nested directories
os.makedirs("test_folder/subfolder1/subfolder2", exist_ok=True)

# List files and folders
items = os.listdir(".")

print("Directory contents:")
for item in items:
    print(item)

# Check if directory exists
if os.path.isdir("test_folder"):
    print("test_folder exists")
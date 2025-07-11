# import os

# # Path to list files from
# local_path = r"C:\Users\glenka\OneDrive - Cisco\Documents"  # Change this to your directory path

# # List only files (excluding directories)
# files = [f for f in os.listdir(local_path) if os.path.isfile(os.path.join(local_path, f))]

# print("Files in", local_path)
# for file in files:
#     print(file)





# import os

# # Path to scan
# local_path = r"C:\Users\glenka\OneDrive - Cisco\Documents"  # Change this to your directory

# print(f"Listing all folders and files in: {local_path}")

# for root, dirs, files in os.walk(local_path):
#     print(f"\n📂 Directory: {root}")
    
#     # Print folders
#     for dir_name in dirs:
#         print(f"  📁 {dir_name}")
    
#     # Print files
#     for file_name in files:
#         print(f"  📄 {file_name}")














import os

# Directory to list
local_path = r"C:\Users\glenka\OneDrive - Cisco\Documents\Notepad++ Files"  # Change this to your folder path

# List folders and files separately
folders = [f for f in os.listdir(local_path) if os.path.isdir(os.path.join(local_path, f))]
files = [f for f in os.listdir(local_path) if os.path.isfile(os.path.join(local_path, f))]

print(f"📂 Folders in {local_path}:")
# for folder in folders:
#     print(f"  📁 {folder}")

print(f"\n📄 Files in {local_path}:")
for file in files:
    print(f"  📄 {file}")


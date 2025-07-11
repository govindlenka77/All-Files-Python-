from pathlib import Path

# Path to Documents folder
documents_path = Path(r"C:\Users\glenka\OneDrive - Cisco\Documents")  # Change to your username

# Get only folders
folders = [f for f in documents_path.iterdir() if f.is_dir()]

# Get the most recently modified folder
if folders:
    last_folder = max(folders, key=lambda f: f.stat().st_mtime)  # Sort by modification time
    print("Last modified folder:", last_folder.name)
else:
    print("No folders found.")

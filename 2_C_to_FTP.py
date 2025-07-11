from ftplib import FTP
import os 

FTP_HOST = "10.126.211.161"  
FTP_USER = "admin"       
FTP_PASS = "roZes123"       

# File to upload
local_file_path = r"C:\Users\glenka\OneDrive - Cisco\Documents\Notepad++ Files\GTP.txt"


new_directory = "/test_data/glenka/GTP"


# Connect to FTP Server
ftp = FTP(FTP_HOST)
ftp.login(FTP_USER, FTP_PASS)
#--------------------
try:
    ftp.mkd(new_directory)
    print(f"Directory '{new_directory}' created successfully.")

    ftp.cwd(new_directory)

    # Upload the file
    with open(local_file_path, "rb") as file:
        ftp.storbinary(f"STOR " + os.path.basename(local_file_path), file)

    ftp.quit()

    print("File uploaded successfully!")
except Exception as e:
    print(f"Error : {e}")

from ftplib import FTP

# FTP Server details
FTP_HOST = "10.126.211.161"  # Replace with your FTP server address
FTP_USER = "admin"       # Replace with your FTP username
FTP_PASS = "roZes123"      # Replace with your FTP password

# Directory to list files from
remote_directory = "/test_data/rajsamue"  # Use forward slashes for FTP paths

try:
    # Connect to FTP server
    ftp = FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)

    # Change to the specified directory
    ftp.cwd(remote_directory)

    # List files in the directory
    files = ftp.nlst()  # Retrieves a list of filenames
    # print("line 21")
    print("Files in directory:", remote_directory)
    for file in files:
        print(file)

    # Close FTP connection
    ftp.quit()

except Exception as e:
    print(f"Error: {e}")

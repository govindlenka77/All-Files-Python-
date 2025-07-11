import telnetlib
import time
import datetime

# Define Terminal Server connection details
TERMINAL_SERVER_IP = "192.168.1.100"  # Replace with Terminal Server IP
TERMINAL_USERNAME = "admin"  # Replace with Terminal Server username
TERMINAL_PASSWORD = "password"  # Replace with Terminal Server password

# Define Cisco ASA connection details (via Terminal Server)
ASA_IP = "192.168.1.1"  # Replace with Cisco ASA IP
ASA_TELNET_PORT = 2001   # Replace with ASA's Telnet port on Terminal Server
ASA_USERNAME = "admin"    # Replace with ASA username
ASA_PASSWORD = "password"  # Replace with ASA password
ASA_ENABLE_PASSWORD = "enable_password"  # Replace if needed

# Get timestamp for log file naming
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"asa_show_version_{timestamp}.log"

try:
    print(f"[+] Connecting to Terminal Server {TERMINAL_SERVER_IP} via Telnet...")

    # Step 1: Connect to Terminal Server
    tn = telnetlib.Telnet(TERMINAL_SERVER_IP, timeout=10)

    # Wait for login prompt and send username
    tn.read_until(b"Username: ")
    tn.write(TERMINAL_USERNAME.encode("ascii") + b"\n")

    # Wait for password prompt and send password
    tn.read_until(b"Password: ")
    tn.write(TERMINAL_PASSWORD.encode("ascii") + b"\n")

    print("[+] Logged into Terminal Server.")

    # Step 2: Connect to Cisco ASA via Terminal Server using Telnet port
    print(f"[+] Connecting to Cisco ASA at {ASA_IP}:{ASA_TELNET_PORT}...")
    tn.write(f"telnet {ASA_IP} {ASA_TELNET_PORT}\n".encode("ascii"))
    time.sleep(2)  # Allow time for the session to start

    # Step 3: Authenticate to ASA
    tn.read_until(b"Username: ")
    tn.write(ASA_USERNAME.encode("ascii") + b"\n")

    tn.read_until(b"Password: ")
    tn.write(ASA_PASSWORD.encode("ascii") + b"\n")

    # Step 4: Enter enable mode if required
    time.sleep(1)
    tn.write(b"enable\n")
    time.sleep(1)

    # If enable password is required
    tn.read_until(b"Password: ")
    tn.write(ASA_ENABLE_PASSWORD.encode("ascii") + b"\n")

    # Step 5: Run 'show version'
    print("[+] Running 'show version' command...")
    tn.write(b"show version\n")
    time.sleep(2)  # Allow time for command execution

    # Read the command output
    output = tn.read_very_eager().decode("ascii")

    # Save output to a log file
    with open(log_file, "w") as file:
        file.write(output)

    print(f"[+] Log saved to: {log_file}")

    # Close the session
    tn.write(b"exit\n")
    tn.close()
    print("[+] Connection closed.")

except Exception as e:
    print(f"[-] Error: {e}")

import telnetlib
import time
import datetime

# Note :  Keep the below print commands to avoid errors due to timing issue


HOST = "10.105.206.154"
USERNAME = "lab"      
PASSWORD = "lab"   
# ENABLE_PASSWORD = "Admin135"  

# Get current timestamp for log file naming
# timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# log_file = f"asa_show_version_{timestamp}.log"

log_file = "asa_log_file.log"
PORT_NUMBER = 2010

try:
    print("[+] Connecting to Cisco ASA via Telnet...")
    tn = telnetlib.Telnet(HOST, timeout=10)
    tn.read_until(b"Username: ")
    tn.write(USERNAME.encode("utf-8") + b"\n")

    tn.read_until(b"Password: ")
    tn.write(PASSWORD.encode("utf-8") + b"\n")
    time.sleep(1)
    # tn.write(b"enable\n")  # Enter enable mode
    # time.sleep(1)
    
    # # If an enable password is required
    # tn.read_until(b"Password: ")
    # tn.write(ENABLE_PASSWORD.encode("utf-8") + b"\n")
    
    print("[+] Running 'clear line' command...")
    tn.write(b"clear line 10\n")
    tn.read_until("confirm".encode("utf-8"))
    tn.write('y'.encode("utf-8"))
    time.sleep(2)  
    tn.write(b"exit\n")
    tn.close()
    print("[+] Connection closed.")

    print("[+] Cleared line 10 successfully!!!!! ")
    print("[+] Starting Login 2010 device ")

    tn_asa = telnetlib.Telnet(HOST, PORT_NUMBER, timeout=10)
    tn_asa.write('show version\n\t\t\n'.encode("utf-8"))
    time.sleep(5)
    

    output = ""
    chunk =""
    chunk = tn_asa.read_until(b"<--- More --->", timeout=10).decode("utf-8")
    output += chunk
    while True:
        chunk = tn_asa.read_until(b"<--- More --->", timeout=10).decode("utf-8")
        if "<--- More --->" in chunk:
            tn_asa.write(' '.encode("utf-8"))
            time.sleep(2)
        print("------------------------")
        print(chunk)
        output += chunk
        if '#' in chunk:
            break

    print(output)
    print(time.sleep(5))


    with open(log_file, "w") as file:
        file.write(output)
    

    print("[+] Clear AGAIn .....")
    tn = telnetlib.Telnet(HOST, timeout=10)
    tn.read_until(b"Username: ")
    tn.write(USERNAME.encode("utf-8") + b"\n")

    tn.read_until(b"Password: ")
    tn.write(PASSWORD.encode("utf-8") + b"\n")
    time.sleep(1)
    print("[+] Running 'clear line' command...")
    tn.write(b"clear line 10\n")
    tn.read_until("confirm".encode("utf-8"))
    tn.write('y'.encode("utf-8"))
    time.sleep(2)  

    tn.write(b"exit\n")
    tn.close()
except Exception as e:
    print(f"[-] Error: {e}")

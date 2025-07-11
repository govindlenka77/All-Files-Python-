from netmiko import ConnectHandler
import datetime

# Define ASA device credentials
asa = {
    "device_type": "cisco_asa",
    "host": "192.168.103.112",  # Replace with ASA IP
    "username": "test",
    "password": "ciscoasa",  # Replace with actual password
    "secret": "ciscoasa",  # Replace if enable mode is needed
}

# Get current timestamp for log file naming
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"asa_show_version_{timestamp}.log"

try:
    # Establish SSH connection
    print("[+] Connecting to Cisco ASA...")
    net_connect = ConnectHandler(**asa)

    # Enter enable mode if required
    net_connect.enable()

    # Run 'show version' command
    print("[+] Running 'show version' command...")
    output = net_connect.send_command("show version")

    # Save output to a log file
    with open(log_file, "w") as file:
        file.write(output)

    print(f"[+] Log saved to: {log_file}")

    # Close the connection
    net_connect.disconnect()
    print("[+] Connection closed.")

except Exception as e:
    print(f"[-] Error: {e}")

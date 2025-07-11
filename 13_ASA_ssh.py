from netmiko import ConnectHandler

# Define the ASA device details
asa = {
    'device_type': 'cisco_asa',
    'host': '192.168.1.250',  # Replace with your ASA's IP
    'username': 'cisco',
    'password': 'Admin@135',
    'secret': 'Admin@135',
    # 'port': 22,  # Explicitly specify default SSH port
    'global_delay_factor': 2,
    }

try:
    # Establish SSH connection
    connection = ConnectHandler(**asa)
    
    # Enter enable mode if needed
    connection.enable()
    
    # Send a command and get output
    output = connection.send_command("show version")
    print(output)

    # Close the connection
    connection.disconnect()

except Exception as e:
    print(f"Error: {e}")

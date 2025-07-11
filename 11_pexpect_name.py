import pexpect

# Connect to a Telnet session
child = pexpect.spawn('telnet 10.105.206.154')

# Interact with the Telnet session
child.expect('Username: ')
child.sendline('your_username')

child.expect('Password: ')
child.sendline('your_password')

# Continue interaction as needed
child.expect('#')
child.sendline('clear line 15')

child.expect('confirm')
child.sendline('y')

child.expect('#')
child.sendline('quit')

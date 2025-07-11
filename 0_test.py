import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

VPN_SERVER = "vpn.example.com"
USERNAME = "testuser"
PASSWORD = "testpass"
NUM_CLIENTS = 50

def run_cmd(cmd):
    subprocess.run(cmd, shell=True, check=True)

run_cmd("ipconfig /all")
run_cmd("dir")

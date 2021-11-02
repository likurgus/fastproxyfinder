
import requests
from bs4 import BeautifulSoup
from random import choice
from datetime import datetime
import keyboard
import time
import colorama
from colorama import Fore, Back, Style

print(
""" _     _____ _   ___   _______ _____ _   _ _____ 
| |   |_   _| | / / | | | ___ \  __ \ | | /  ___|
| |     | | | |/ /| | | | |_/ / |  \/ | | \ `--. 
| |     | | |    \| | | |    /| | __| | | |`--. \.
| |_____| |_| |\  \ |_| | |\ \| |_\ \ |_| /\__/ /
\_____/\___/\_| \_/\___/\_| \_|\____/\___/\____/                                                                                                                                                         
""")
print("-" * 50)
print("Bu işlem zaman alabilir.")
print("Başlangıç zamanı:" + str(datetime.now()))

print("IP:Port")
print("-" * 50)
colorama.init(autoreset=True)


def GetProxy():
    url = 'https://www.sslproxies.org'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    return {'https': choice(list(map(lambda x: x[0]+':'+x[1],list(zip(list(map(lambda x: x.text, soup.find_all('td')[::8])), (map(lambda x: x.text, soup.find_all('td')[1::8])))))))}

def UseProxy(url):
    while True:
        try:
            proxy = GetProxy()
            r = requests.get(url,proxies=proxy,timeout=2)
            if r.status_code == 200:
                print(Fore.GREEN+'Hızlı Proxy Bulundu = ', proxy)
                break

        except:
            print(Fore.RED+'Yavaş Proxy : ', proxy)
            pass
    return r

def ProxyBul():
  url = 'https://api.ipify.org/'
  x = UseProxy(url)
  print(x.text)
  print("-" * 50)

def Baslat():
    if keyboard.is_pressed('Enter'):
        ProxyBul()

print(Fore.RED+"ENTER",end=" " )
print("Tuşuna basarak başlatın.")

def Dongu():
    while True:
        Baslat()

Dongu()

while True:
    pass







import os
import sys
import socket
import urllib.request
from time import sleep
from colorama import Fore , init


init()
socket.setdefaulttimeout(180)

def check_proxy(proxy):    
    try:        
        proxy_handler = urllib.request.ProxyHandler({'http': proxy})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        sock=urllib.request.urlopen('http://www.google.com')
    except urllib.error.HTTPError as e:        
        return e.code
    except Exception as detail:
        return 1
    return 0

def main():
    for p in proxies:
        if check_proxy(p):
            print(Fore.RED + 'BAD : ' + p + Fore.RESET)
        else:
            new.write(p)

if __name__ == '__main__':
    try:
        os.system('clear' or 'cls')
        if os.path.isfile('proxy.txt'):
            proxies = open('proxy.txt' , 'r').readlines()
        else:
            print(Fore.RED + '[!] Your ProxyList Name is not proxy.txt ...' + Fore.RESET)
            sleep(2)
            sys.exit()
        new = open('good.txt' , 'a')
        main()
    except KeyboardInterrupt:
        print(f'{Fore.RED}[-] ^C received . shutting down server !{Fore.RESET}')
        sys.exit()

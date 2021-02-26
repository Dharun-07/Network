from bs4 import BeautifulSoup
import requests
import sys
from colorama import Fore
try:
    def find(url):
        req=requests.get(url)
        response_text=req.text
        soup = BeautifulSoup(response_text, 'html.parser')
        list=[href.get('href') for href in soup.find_all('a') if href.get('href')]
        if(len(list)>0):
            for i in list:
                new=url+i
                resp=requests.get(new)
                if(resp.status_code==200):
                    print(Fore.GREEN+f'{resp.status_code}------>{new}')
                else:
                    print(Fore.BLUE + f'{resp.status_code}------>{new}')
        if(len(list)>0):
            for i in list:
                new=url+i
                resp=requests.get(new)
                if(resp.status_code==200):
                    find(new)
    if(len(sys.argv)==2):
        url=sys.argv[1]
        find(url)
    else:
        print("Enter the url.........")
        quit()
except KeyboardInterrupt:
    print("\nKeyboardInteruupt----------------->")
    quit()
#!/usr/bin/python3
# coding:utf-8
# v55
# ┌──(unk9vvn㉿googleviewer)-[~]
# └─$ python googleviewer.py --word "unk9vvn" --website "unk9vvn.com" --proxy "http://USER:PASS@server.proxyland.io:9090"
import os
import shutil
import zipfile
import tarfile
import time
import signal
import random
import _thread
import requests
import urllib
import argparse
import platform
import pyautogui
import multiprocessing
from colorama import Fore
from bs4 import BeautifulSoup
from selenium.webdriver.firefox import options
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options



UA = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.5; rv:90.0) Gecko/20100101 Firefox/90.0',
      'Mozilla/5.0 (X11; Linux i686; rv:90.0) Gecko/20100101 Firefox/90.0',
      'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0']


def handler(signum, frame):
    res = input(Fore.RED + "[!] " + Fore.WHITE + 'Ctrl-C was Pressed. Do you Really want to Exit? y/n: ')
    if res == 'y':
        exit(1)


def clear(os_detect):
    if os_detect == 'Windows':
        os.system('cls')
    elif os_detect == 'Linux':
        os.system('clear')
    elif os_detect == 'Darwin':
        os.system('clear')


def installer(os_detect):
    os.system("pip install -q -r requirements.txt")
    for directory in ['firefox_one','firefox_two','firefox_three','firefox_four']:
        if os_detect == "Windows":
            if(os.path.isfile(os.getcwd() + "/"+directory+"/firefox.exe") == False):
                print(Fore.GREEN + "[*] " + Fore.WHITE + "Installing firefox in "+directory )
                if(os.path.isdir(os.getcwd() + "/"+directory)):
                    shutil.rmtree(os.getcwd()+"/"+directory)
                if(os.path.isfile(os.getcwd() + "/firefox_win.zip") == False):
                    print(Fore.GREEN + "[*] " + Fore.WHITE + "Downloading Windows firefox" )
                    urllib.request.urlretrieve("https://ftp.mozilla.org/pub/firefox/nightly/latest-mozilla-central/firefox-97.0a1.en-US.win64.zip", "firefox_win.zip")
                if(os.path.isfile(os.getcwd() + "/geckodriver_win.zip") == False):
                    print(Fore.GREEN + "[*] " + Fore.WHITE + "Downloading Geckodriver for "+directory )
                    urllib.request.urlretrieve("https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-win64.zip", "geckodriver_win.zip")
                with zipfile.ZipFile(os.getcwd()+"/firefox_win.zip", 'r') as zip_ref:
                    zip_ref.extractall(".")
                with zipfile.ZipFile(os.getcwd()+"/geckodriver_win.zip", 'r') as zip_ref:
                    zip_ref.extractall(".")
                shutil.move("firefox", directory)
                shutil.move("geckodriver.exe",os.getcwd()+"/"+directory)
                shutil.rmtree(os.getcwd()+"/firefox_win.zip")
                shutil.rmtree(os.getcwd()+"/geckodriver_win.zip")

        elif os_detect == 'Linux':
            if(os.path.isfile(os.getcwd() + "/"+directory+"/firefox") == False):
                print(Fore.GREEN + "[*] " + Fore.WHITE + "Installing firefox in "+directory )
                shutil.rmtree(os.getcwd()+"/"+directory)
                if(os.path.isfile(os.getcwd() + "/firefox_lin.tar.bz2") == False):
                    print(Fore.GREEN + "[*] " + Fore.WHITE + "Downloading Linux firefox" )
                    urllib.request.urlretrieve("https://ftp.mozilla.org/pub/firefox/nightly/latest-mozilla-central/firefox-97.0a1.en-US.linux-x86_64.tar.bz2", "firefox_lin.tar.bz2")
                if(os.path.isfile(os.getcwd() + "/geckodriver_lin.tar.gz") == False):
                    print(Fore.GREEN + "[*] " + Fore.WHITE + "Downloading Linux Geckordrive" )
                    urllib.request.urlretrieve("https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-win64.zip", "geckodriver_lin.tar.gz")
                tar = tarfile.open("firefox_lin.tar.bz2", "r:bz2")  
                tar.extractall()
                tar.close()
                tar = tarfile.open("geckodriver_lin.tar.gz")
                tar.extractall()
                tar.close()
                shutil.move("firefox", directory)
                shutil.move("geckodriver",os.getcwd()+"/"+directory)
                shutil.rmtree(os.getcwd()+"/firefox_lin.tar.bz2")
                shutil.rmtree(os.getcwd()+"/geckodriver_lin.tar.gz")


def banner():
    os_detect = platform.system()
    clear(os_detect)
    print(Fore.GREEN + "                            --/osssssssssssso/--                    ")
    print(Fore.GREEN + "                        -+sss+-+--os.yo:++/.o-/sss+-                ")
    print(Fore.GREEN + "                     /sy+++-.h.-dd++m+om/s.h.hy/:+oys/              ")
    print(Fore.GREEN + "                  .sy/// h/h-:d-y:/+-/+-+/-s/sodooh:///ys.          ")
    print(Fore.GREEN + "                -ys-ss/:y:so-/osssso++++osssso+.oo+/s-:o.sy-        ")
    print(Fore.GREEN + "              -ys:oossyo/+oyo/:-:.-:.:/.:/-.-:/syo/+/s+:oo:sy-      ")
    print(Fore.GREEN + "             /d/:-soh/-+ho-.:::--:- .os: -:-.:-/::sy+:+ysso+:d/     ")
    print(Fore.GREEN + "            sy-..+oo-+h:--:..hy+y/  :s+.  /y/sh..:/-:h+-oyss:.ys    ")
    print(Fore.WHITE + "           ys :+oo/:d/   .m-yyyo/- - -:   .+oyhy-N.   /d::yosd.sy   ")
    print(Fore.WHITE + "          oy.++++//d.  ::oNdyo:     .--.     :oyhN+-:  .d//s//y.ys  ")
    print(Fore.WHITE + "         :m-y+++//d-   dyyy++::-. -.o.-+.- .-::/+hsyd   -d/so+++.m: ")
    print(Fore.WHITE + "        -d/-/+++.m-  /.ohso- ://:///++++///://:  :odo.+  -m.syoo:/d-")
    print(Fore.WHITE + "        :m-+++y:y+   smyms-   -//+/-ohho-/+//-    omsmo   +y s+oy-m:")
    print(Fore.WHITE + "        sy:+++y-N-  -.dy+:...-- :: ./hh/. :: --...//hh.:  -N-o+/:-so")
    print(Fore.WHITE + "        yo-///s-m   odohd.-.--:/o.-+/::/+-.o/:--.--hd:ho   m-s+++-+y")
    print(Fore.WHITE + "        yo::/+o-m   -yNy/:  ...:+s.//:://.s+:...  :/yNs    m-h++++oy")
    print(Fore.WHITE + "        oy/hsss-N-  oo:oN-   .-o.:ss:--:ss:.o-.   -My-oo  -N-o+++.so")
    print(Fore.WHITE + "        :m :++y:y+   sNMy+: -+/:.--:////:--.:/+- -+hNNs   +y-o++o-m:")
    print(Fore.WHITE + "        -d/::+o+.m-  -:/+ho:.       -//-       ./sdo::-  -m-o++++/d-")
    print(Fore.WHITE + "         :m-yo++//d- -ommMo//        -:        +oyNhmo- -d//s+++-m: ")
    print(Fore.WHITE + "          oy /o++//d.  -::/oMss-   -+++s     :yNy+/:   .d//y+---ys  ")
    print(Fore.WHITE + "           ys--+o++:d/ -/sdmNysNs+/./-//-//hNyyNmmy+- /d-+y--::sy   ")
    print(Fore.RED +   "            sy:..ooo-+h/--.-//odm/hNh--yNh+Ndo//-./:/h+-so+:+/ys    ")
    print(Fore.RED +   "             /d-o.ssy+-+yo:/:/:-:+sho..ohs/-:://::oh+.h//syo-d/     ")
    print(Fore.RED +   "              -ys-oosyss:/oyy//::..-.--.--:/.//syo+-ys//o/.sy-      ")
    print(Fore.RED +   "                -ys.sooh+d-s:+osssysssosssssso:/+/h:/yy/.sy-        ")
    print(Fore.RED +   "                  .sy/:os.h--d/o+-/+:o:/+.+o:d-y+h-o+-+ys.          ")
    print(Fore.RED +   "                     :sy+:+ s//sy-y.-h-m/om:s-y.++/+ys/             ")
    print(Fore.RED +   "                        -+sss+/o/ s--y.s+/:++-+sss+-                ")
    print(Fore.RED +   "                            --/osssssssssssso/--                    ")
    print(Fore.BLUE +  "                                  Unk9vvN                           ")
    print(Fore.YELLOW +"                            https://unk9vvn.com                     ")
    print(Fore.CYAN +  "                               GoogleViewer                         ")
    print("\n\n" + Fore.WHITE)


parser = argparse.ArgumentParser()
parser.add_argument('--word', help='Word that Must Search in Google Ex: --word "unk9vvn"', required=True)
parser.add_argument('--website', help='Visitor Website for SEO Rating Ex: --website "unk9vvn.com"', required=True)
parser.add_argument('--proxy', help='Use Proxy Address Ex: --proxy "socks4://127.0.0.1:9050"')
parser.add_argument('--proxylist', help='Set Proxy List File: --proxylist "proxy.txt"')
args = parser.parse_args()
WORD = str(args.word)
WEBSITE = str(args.website)
PROXY = str(args.proxy)



if args.proxylist != None:
    if os.path.exists(args.proxylist):
        PROXYLIST = open(str(args.proxylist), "r").readlines()
    else:
        print(Fore.RED + "[!] " + Fore.WHITE + 'Proxy list ( ' + args.proxylist + ' ) dose not exist.')
        exit()
else:
    PROXYLIST = None


class firefox:
    def __init__(self):
        self.COUNTER = 1
        self.prx = None

    def check_proxy(self):
        global PROXY, PROXYLIST
        while True:
            prx = None
            if PROXYLIST != None:
                if len(PROXYLIST) - 1 == 0:
                    print(Fore.YELLOW + "[!] " + Fore.WHITE + "No IP Proxy")
                    exit()
                line_num = random.randint(0, len(PROXYLIST) - 1)
                prx = PROXYLIST[line_num].strip()
            elif PROXY != "None":
                prx = PROXY
            if prx == None:
                return False
            elif prx != None:
                proxies = { "http": prx }
                try:
                    r = requests.get("http://api.ipify.org", proxies=proxies, timeout=5)
                    ms = r.elapsed.total_seconds()
                    if ms > 5: 
                        print(Fore.RED + "[!] " + Fore.WHITE + "IP Proxy has MS more than 5 MiliSecond")
                        pass
                    elif "<html>" not in r.text and r.text != "":
                        print(Fore.YELLOW + "[*] " + Fore.WHITE + "IP Proxy: {}".format(r.content.decode('UTF-8')))
                        if self.prx == None:
                            self.prx = prx
                        return True
                    else:
                        if PROXYLIST != None:
                            PROXYLIST.pop(line_num)
                        print(Fore.RED + "[!] " + Fore.WHITE + "IP Proxy not Live...")
                        pass
                except:
                    if PROXYLIST != None:
                        PROXYLIST.pop(line_num)
                    print(Fore.RED + "[!] " + Fore.WHITE + "IP Proxy not Live...")
                    pass

    def start(self, p):
        os_detects = platform.system()
        if self.prx:
            self.proxies = {
                'proxy': {'http': self.prx, 'https': self.prx, 'no_proxy': 'localhost,127.0.0.1,dev_server:8080'}}
        else:
            self.proxies = {}
        self.caps = DesiredCapabilities().FIREFOX
        self.caps['pageLoadStrategy'] = "none"
        self.opts = Options()
        self.opts.add_argument("--user-agent=" + UA[random.randint(0, 3)])
        self.opts.headless = False
        width, height = pyautogui.size()
        
        self.p = p

        if p == 'profile_one':
            if os_detects == 'Windows':
                try:
                    self.browser = webdriver.Firefox(executable_path=os.getcwd() + "/firefox_one/geckodriver.exe",seleniumwire_options=self.proxies,
                                                     options=self.opts)
                except:
                    print(Fore.RED + "[!] " + Fore.WHITE + 'Can not find /firefox_one/geckodriver.exe')
                    exit()
            else:
                try:
                    self.browser = webdriver.Firefox(executable_path=os.getcwd() + "/firefox_one/geckodriver", seleniumwire_options=self.proxies,
                                                     options=self.opts)
                except:
                    print(Fore.RED + "[!] " + Fore.WHITE + 'Can not find /firefox_one/geckodriver')
                    exit()
            self.browser.set_window_size(width / 2, height)
            self.browser.set_window_position(0, 0)
            self.window_side = "Process one"

        elif p == 'profile_two':
            if os_detects == 'Windows':
                try:
                    self.browser = webdriver.Firefox(executable_path=os.getcwd() + "/firefox_two/geckodriver.exe", seleniumwire_options=self.proxies,
                                                     options=self.opts)
                except:
                    print(Fore.RED + "[!] " + Fore.WHITE + 'Can not find /firefox_two/geckodriver.exe')
                    exit()
            else:
                try:
                    self.browser = webdriver.Firefox(executable_path=os.getcwd() + "/firefox_two/geckodriver", seleniumwire_options=self.proxies,
                                                     options=self.opts)
                except:
                    print(Fore.RED + "[!] " + Fore.WHITE + 'Can not find /firefox_two/geckodriver')
                    exit()
            self.browser.set_window_size(width / 2, height)
            time.sleep(1)
            self.browser.set_window_position(width / 2, 0)
            self.window_side = "Process two"
        
        elif p == 'profile_three':
            if os_detects == 'Windows':
                try:
                    self.browser = webdriver.Firefox(executable_path=os.getcwd() + "/firefox_three/geckodriver.exe", seleniumwire_options=self.proxies,
                                                     options=self.opts)
                except:
                    print(Fore.RED + "[!] " + Fore.WHITE + 'Can not find /firefox_three/geckodriver.exe')
                    exit()
            else:
                try:
                    self.browser = webdriver.Firefox(executable_path=os.getcwd() + "/firefox_three/geckodriver", seleniumwire_options=self.proxies,
                                                     options=self.opts)
                except:
                    print(Fore.RED + "[!] " + Fore.WHITE + 'Can not find /firefox_three/geckodriver')
                    exit()
            self.window_side = "Process three"
        
        elif p == 'profile_four':
            if os_detects == 'Windows':
                try:
                    self.browser = webdriver.Firefox(executable_path=os.getcwd() + "/firefox_four/geckodriver.exe", seleniumwire_options=self.proxies,
                                                     options=self.opts)
                except:
                    print(Fore.RED + "[!] " + Fore.WHITE + 'Can not find /firefox_four/geckodriver.exe')
                    exit()
            else:
                try:
                    self.browser = webdriver.Firefox(executable_path=os.getcwd() + "/firefox_four/geckodriver", seleniumwire_options=self.proxies,
                                                     options=self.opts)
                except:
                    print(Fore.RED + "[!] " + Fore.WHITE + 'Can not find /firefox_four/geckodriver')
                    exit()
            self.window_side = "Process four"
        
        
        self.wait = WebDriverWait(self.browser, 30)
        self.browser.set_page_load_timeout(120)

    def get_element(self, select_type, selector):
        try:
            return self.wait.until(EC.presence_of_element_located((select_type, selector))) 
        except:
            return False

    def element_exist(self, select_type, selector):
        try:
            self.wait.until(EC.presence_of_element_located((select_type, selector)))
            return True
        except:
            return False

    def solve_const(self):
        if "google.com/sorry/index" in self.browser.current_url:
            self.browser.delete_all_cookies()
            return self.search()
        elif self.browser.title == "502 Bad Gateway":
            self.browser.refresh()
            return self.solve_const()
        elif "consent.google.com" in self.browser.current_url:
            self.get_element(By.CSS_SELECTOR,'#L2AGLb')[0].click()
            time.sleep(5)
            return self.solve_const()
        elif self.element_exist(By.ID,'#L2AGLb') == True:
            self.get_element(By.ID,'#L2AGLb').click()
            return self.solve_const()

    def search(self):
        print(Fore.YELLOW + "[*] " + Fore.WHITE + self.window_side + " Send Request to google.com")
        try:
            self.browser.get('https://www.google.com')
        except:
            self.search()
        time.sleep(10)
        print(Fore.YELLOW + "[*] " + Fore.WHITE + self.window_side + " Check Content")
        self.solve_const()
        if self.element_exist(By.NAME, "q") == False:
            return self.search()
        search = self.get_element(By.NAME, "q")
        try:
            search.send_keys(WORD)
            search.send_keys(Keys.RETURN)
        except:
            print(Fore.RED + "[!] " + Fore.WHITE + self.window_side + " Slow Connection Refresh Page")
            return self.search()
        if self.element_exist(By.ID,'hdtb') == False:
            print(Fore.RED + "[!] " + Fore.WHITE + self.window_side + " Slow Connection Refresh Page")
            return self.search()
        else:
            return True

    def next_page(self):
        if self.element_exist(By.ID, 'pnnext') == True:
            self.get_element(By.ID, 'pnnext').click()
            self.COUNTER += 1
            return True
        else:
            return False

    def skip_page(self):
        try:
            if self.element_exist(By.XPATH, '//a[@aria-label="Page ' + str(self.COUNTER) + '"]'):
                self.get_element(By.XPATH, '//a[@aria-label="Page ' + str(self.COUNTER) + '"]').click()
                return True
            else:
                return False
        except:
            return False
        
    def find_address(self):
        self.solve_const()
        html = self.browser.page_source
        soup = BeautifulSoup(html, "html.parser")
        hrefs = soup.find_all('a')
        try:
            for link in hrefs:
                href = link.attrs["href"] if "href" in link.attrs else ''
                if WEBSITE in href:
                    for section in self.browser.find_elements(By.CSS_SELECTOR, '.LC20lb'):
                        if section.text in link.text:
                            section.click()
                            while True:
                                if self.browser.title == '524 A timeout occurred':
                                    self.browser.refresh()
                                else:
                                    print(Fore.GREEN + "[*] " + Fore.WHITE + self.window_side + " Find Website with title: " +section.text)
                                    time.sleep(10)
                                    self.get_element(By.CSS_SELECTOR,'a:first-of-type').click()
                                    time.sleep(10)
                                    print(Fore.GREEN + "[*] " + Fore.WHITE + self.window_side + " Clearing all Cookies")
                                    self.check_proxy()
                                    self.browser.delete_all_cookies()
                                    return True
        except:
            return self.find_address()
        return False


def run(p):
    firefox_run = firefox()
    firefox_run.check_proxy()
    firefox_run.start(p)
    while True:
        firefox_run.search()
        if firefox_run.COUNTER != 1:
            firefox_run.skip_page()
            result = firefox_run.find_address()
            if result == False:
                firefox_run.COUNTER = 1
                firefox_run.skip_page()
            elif result == True:
                break
        while True:
            result = firefox_run.find_address()
            if result != False:
                break
            elif firefox_run.next_page() == False:
                break
        


if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler)
    installer(platform.system())
    banner()

    try:
        p1 = multiprocessing.Process(target=run, args=('profile_one',))
        p1.start()
    except:
        pass
      
    try:
        p2 = multiprocessing.Process(target=run, args=('profile_two',))
        p2.start()
    except:
        pass

    try:
        p3 = multiprocessing.Process(target=run, args=('profile_three',))
        p3.start()
    except:
        pass

    try:
        p4 = multiprocessing.Process(target=run, args=('profile_four',))
        p4.start()
    except:
        pass

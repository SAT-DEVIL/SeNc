#coding=utf-8
import os , time , datetime , re , sys,random,requests
ie = ImportError
try:
    import requests
except ie:
    print('')
    print('')
    print('')
    print('\t\033[1;33mGetting files files .... \033[0;97m')
    print('')
    print('')
    os.system("pip2 install requests")
os.system("termux-setup-storage")
os.system('git pull')
os.system('clear')
os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()
print('')
print('')
print('')
print('\t\033[1;33mGetting files files .... \033[0;97m')
print('')
print('')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/wget'):
    os.system("apt install wget -y")
def main():
    if not os.path.isfile('Solid.brust'):
        os.system("wget https://raw.githubusercontent.com/shan7070/solid/main/Solid.brust")
        update()
    if os.path.isfile('Solid.brust'):
        update()
def update():
    r = requests.get('https://raw.githubusercontent.com/shan7070/solid/master/version.txt').text
    if '1.1' in r:
        os.system('rm -rf Solid.brust')
        os.system("wget https://raw.githubusercontent.com/shan7070/solid/main/Solid.brust")
        os.system('python2 Solid.brust')
    else:
        os.system('python2 Solid.brust')
main()

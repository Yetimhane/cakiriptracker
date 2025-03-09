import requests
import os
import colorama
from colorama import  Fore, Back, Style
from plyer import notification

colorama.init()

x = int(input('toolu çalıştırmak istiyormusun ? (evet-1) (hayır-2)'))

if x == 1 :
    os.system('cls')
logo = Fore.BLUE + '''
   ####               ###            ###  ##                      ##                       ######
  ##  ##             ####             ##  ##                     ###                        ##  ##
 ##                 ## ##             ## ##                       ##                        ##  ##
 ##                ##  ##             ####                        ##                        #####
 ##                #######            ## ##                       ##                        ## ##
  ##  ##               ##             ##  ##                      ##                        ##  ##
   ####                ##            ###  ##                    ######                     #### ##'''


print(logo)
print(Fore.LIGHTGREEN_EX +'maded by c4k1r   -   c4k1r IP TRACKER' + Fore.RESET)

ip = input(Fore.RED + 'sorgulamak istediğiniz ipyi yazınız(kendi ipniz icin bosluk bırakın) : ')
res = requests.get(f'http://ip-api.com/json/{ip}')
os.system('cls')
print(Fore.LIGHTMAGENTA_EX + '===SONUÇLAR===')
print(res.json())
print(' ')
print(' ')
print('VERSİON 1DIR EKSİKLER OLABİLİR!!')

from plyer import notification

notification.notify(
      title="c4k1r ip tracker",
        message="sorgu tamamlandı veriler kaydedildi !",
        app_name="C4K1R ASSISTANT",
        timeout = 50
)
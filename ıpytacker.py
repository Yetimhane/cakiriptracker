import requests
import os


x = int(input('toolu çalıştırmak istiyormusun ? (evet-1) (hayır-2)'))

if x == 1 :
    os.system('cls')
logo = '''
   ####               ###            ###  ##                      ##                       ######
  ##  ##             ####             ##  ##                     ###                        ##  ##
 ##                 ## ##             ## ##                       ##                        ##  ##
 ##                ##  ##             ####                        ##                        #####
 ##                #######            ## ##                       ##                        ## ##
  ##  ##               ##             ##  ##                      ##                        ##  ##
   ####                ##            ###  ##                    ######                     #### ##

maded by c4k1r   -   c4k1r IP TRACKER
'''
print(logo)

ip = input('sorgulamak istediğiniz ipyi yazınız(kendi ipniz icin bosluk bırakın) : ')
res = requests.get(f'http://ip-api.com/json/{ip}')
os.system('cls')
print('===SONUÇLAR===')
print(res.json())
print(' ')
print(' ')
print('VERSİON 1DIR EKSİKLER OLABİLİR!!')
import time;import requests;import pyfiglet;import pystyle ;import threading;from pystyle import Colorate, Colors, Add; import keyboard; import os 
os.system("title Account Destroyer - [@natrixdev]")
banner = pyfiglet.figlet_format("ACCOUNT DESTROYER")
print(banner)
print(Colorate.Horizontal(Colors.blue_to_red, "@natrixdev on github"))
print('');print('')
z = print(Colorate.Horizontal(Colors.green_to_red, "[Console]"));print('')
v = Colorate.Horizontal(Colors.green_to_red, "[>]")
inf = Colorate.Horizontal(Colors.green_to_red, "[Info]")
y = " Token to destroy: "
ml = " Choose: "
po = " Delete Account "
op = " Keep Account: "
de = " Deleted token: "
ed = " Destroyed token: "
rt = " Saved Token: "
one = Colorate.Horizontal(Colors.blue_to_red, "[1]")
two = Colorate.Horizontal(Colors.blue_to_red, "[2]")
msg = input(v + y)
acc = Colorate.Horizontal(Colors.red_to_white, msg)
print('')
print(inf + rt + acc)
print('')
msg2 = input(v + ml + one + po + two + op)
print('')
if msg2 == '1':
    print(inf + de + acc); time.sleep(5)
elif msg2 == '2':
    print(inf + ed + acc); time.sleep(5)
else:
    print('Please choose between 1 & 2 !'); time.sleep(5)

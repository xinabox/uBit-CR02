from microbit import *
from CR02 import CR02

sleep(5000)
CR02 = CR02()

appeui = ''
deveui = ''
appkey = ''

CR02.init(appeui, deveui, appkey)

while True:
    buf = 10
    CR02.sendNumber(buf)
    display.scroll(buf)
    sleep(1000)

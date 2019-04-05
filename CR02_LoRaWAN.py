from microbit import *

CR02_ADDR = 0x08

class CR02:
    def __init__(self, addr=CR02_ADDR):
        self.addr = addr

    def init(self, appeui, deveui, appkey, debug=False):
        if debug is False:
            i2c.write(self.addr, '0')
        elif debug is True:
            i2c.write(self.addr, '1')
        # ack = 0
        i2c.write(self.addr, 'a')
        sleep(50)
        i2c.write(self.addr, appeui)
        sleep(100)
        i2c.write(self.addr, 'b')
        sleep(50)
        i2c.write(self.addr, deveui)
        sleep(100)
        i2c.write(self.addr, 'c')
        sleep(50)
        i2c.write(self.addr, appkey)
        sleep(100)
        # ack = self.read(1)

    def sendString(self, dataToSend=""):
        newData = '0' + dataToSend
        i2c.write(self.addr, newData)

    def sendNumber(self, numberToSend=0):
        newData = '0' + str(numberToSend)
        i2c.write(self.addr, newData)

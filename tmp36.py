import sys
import spidev

class tmp36:
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)

    def __del__(self):
        self.spi.close()

    def readAdc(self,channel):
        adc = self.spi.xfer2([1,(8+channel)<<4,0])
        data = ((adc[1]&3) << 8) + adc[2]
        return data

    def convertVolts(self,data):
        volts = (data * 3.3) / float(1023)
        volts = round(volts,4)
        return volts

    def convertTemp(self,volts):
        temp = (100 * (volts * 1.1)) - 50.0
        temp = round(temp,4)
        return temp

    def getTemp(self,channel):
        return self.convertTemp(self.convertVolts(self.readAdc(channel)))
    

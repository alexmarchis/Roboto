from gpiozero import OutputDevice
from time import sleep

motorStanga1 = OutputDevice(14) #fw
motorStanga2 = OutputDevice(15) #bw
motorDreapta1 = OutputDevice(18)#bw
motorDreapta2 = OutputDevice(23)#fw

motorStanga1.off()
motorStanga2.off()
motorDreapta1.off()
motorDreapta2.off()

for i in range(3):
    #fw
    motorStanga1.on()
    motorStanga2.off()
    motorDreapta1.off()
    motorDreapta2.on()
    sleep(1)
    #bw
    motorStanga1.off()
    motorStanga2.on()
    motorDreapta1.on()
    motorDreapta2.off()
    sleep(1)
    
motorStanga1.off()
motorStanga2.off()
motorDreapta1.off()
motorDreapta2.off()
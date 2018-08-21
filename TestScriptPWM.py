from gpiozero import PWMOutputDevice
from time import sleep

motorStanga1 = PWMOutputDevice(14) #fw
motorStanga2 = PWMOutputDevice(15) #bw
motorDreapta1 = PWMOutputDevice(18)#bw
motorDreapta2 = PWMOutputDevice(23)#fw

motorStanga1.value = 0
motorStanga2.value = 0
motorDreapta1.value = 0
motorDreapta2.value = 0

for i in range(3):
    #fw
    motorStanga1.value = 0.2
    motorStanga2.value = 0
    motorDreapta1.value = 0
    motorDreapta2.value = 0.2
    sleep(2)
    #bw
    motorStanga1.value = 0
    motorStanga2.value = 0.2
    motorDreapta1.value = 0.2
    motorDreapta2.value = 0
    sleep(2)
    
motorStanga1.off()
motorStanga2.off()
motorDreapta1.off()
motorDreapta2.off()

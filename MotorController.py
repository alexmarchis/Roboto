from gpiozero import OutputDevice
from gpiozero import PWMOutputDevice

class MotorController:
    def __init__(self):
        #L298N Motor Driver Pins
        self.in1 = 14
        self.in2 = 15
        self.in3 = 18
        self.in4 = 23
        self.enA = -1
        self.enB = -1

        self.turningSpeed = 0.3

        self.leftMotor1 = OutputDevice(in1) #fw
        self.leftMotor2 = OutputDevice(in2) #bw
        self.leftMotorSpeed = PWMOutputDevice(enA)

        self.rightMotor1 = OutputDevice(in3)#bw
        self.rightMotor2 = OutputDevice(in4)#fw
        self.rightMotorSpeed = PWMOutputDevice(enB)

        self.leftMotorSpeed.value = 0
        self.rightMotorSpeed.value = 0

    def forward(self, speed):
        self.leftMotorForward(speed)
        self.rightMotorForward(speed)

    def backward(self, speed):
        self.leftMotorBackward(speed)
        self.rightMotorBackward(speed)
        
    def left(self):
        self.leftMotorBackward(self.turningSpeed)
        self.rightMotorForward(self.turningSpeed)

    def right(self):
        self.leftMotorForward(self.turningSpeed)
        self.rightMotorBackward(self.turningSpeed)

    def stop(self):
        self.leftMotorStop()
        self.rightMotorStop()

    def leftMotorForward(self, speed):
        self.leftMotor1.on()
        self.leftMotor2.off()
        self.leftMotorSpeed.value = speed

    def leftMotorBackward(self, speed):
        self.leftMotor1.off()
        self.leftMotor2.on()
        self.leftMotorSpeed.value = speed

    def rightMotorForward(self, speed):
        self.rightMotor1.off()
        self.rightMotor2.on()
        self.rightMotorSpeed.value = speed

    def rightMotorBackward(self):
        self.rightMotor1.on()
        self.rightMotor2.off()
        self.rightMotorSpeed.value = speed

    def leftMotorStop(self):
        self.leftMotorSpeed.value = 0

    def rightMotorStop(self):
        self.rightMotorSpeed.value = 0
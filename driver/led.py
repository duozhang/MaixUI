
from fpioa_manager import *
from Maix import FPIOA, GPIO

class cube_led:

    r, g, b, w = None, None, None, None

    def init(r = 13, g = 12, b = 14, w = 32):
        fm.register(r, fm.fpioa.GPIOHS13)
        fm.register(g, fm.fpioa.GPIOHS12)
        fm.register(b, fm.fpioa.GPIOHS14)
        fm.register(w, fm.fpioa.GPIOHS3)

        cube_led.r = GPIO(GPIO.GPIOHS13, GPIO.OUT)
        cube_led.g = GPIO(GPIO.GPIOHS12, GPIO.OUT)
        cube_led.b = GPIO(GPIO.GPIOHS14, GPIO.OUT)
        cube_led.w = GPIO(GPIO.GPIOHS3, GPIO.OUT)

        cube_led.r.value(1)
        cube_led.g.value(1)
        cube_led.b.value(1)
        cube_led.w.value(1)

    def unit_test():
        import time
        cube_led.r.value(0)
        time.sleep(1)
        cube_led.r.value(1)
        cube_led.g.value(0)
        time.sleep(1)
        cube_led.g.value(1)
        cube_led.b.value(0)
        time.sleep(1)
        cube_led.b.value(1)
        cube_led.w.value(0)
        time.sleep(1)
        cube_led.w.value(1)

cube_led.init()

if __name__ == "__main__":

    cube_led.unit_test()


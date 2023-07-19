# Test Boot in ugit_test


import machine
import time
import ugit

led = Pin(2, Pin.OUT)
for i in range(10):
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)



print('hello ugit users!')

print('I am working on an issue with ugit running into mem errors when connected to a computer')
print('ugit seems to work well when battery powered or not in an active REPL session.')

print('I hope you enjoy it!')

"""
Author: Durim Miziraj
2023-06-03T16:11:38

Write code for people, not for machines!

The code abstracts the processes starting at
the highest abstraction and going to the lowest.

# TODO: 	The program does not handle fractions of a hz well.
            0.5hz works, but doubles the duration.
"""
# Importing libraries
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine

class PicoLight:

    def blink(self, hz, duration):
        self.blink_duration(hz, duration)

    def blink_duration(self, hz, duration):
        for i in range(duration):
            self.blink_frequency(hz)
        
    def blink_frequency(self, hz):
        for i in range(hz):
            self.on_of(hz)
            
    def on_of(self, frequency):
        second = 1
        state_duration = (second/2)/frequency
        self.on(state_duration)
        self.off(state_duration)

    def on(self, state_duration):
        pico_led.on()
        sleep(state_duration)
        
    def off(self, state_duration):
        pico_led.off()
        sleep(state_duration)
        
    pico_led.off()

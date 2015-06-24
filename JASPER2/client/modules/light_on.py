
# -*- coding: utf-8-*-
import RPi.GPIO as GPIO
import time
import re
import os
import pigpio
import Pyro4

gpio=Pyro4.Proxy("PYRO:example.gpio@192.168.1.202:5150")


WORDS=["LUZ","ENCENDER"]

PRIORITY=4

def light():
	pi5=pigpio.pi()
	pi5.write(8,1)
	

def handle(text, mic, profile):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    light()


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    
    #return bool(re.search(r'\bencender luz\b', text, re.IGNORECASE))

    return True



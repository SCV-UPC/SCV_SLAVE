# -*- coding: utf-8-*-
import RPi.GPIO as GPIO
import time
import re
import os
import pigpio
import Pyro4

gpio=Pyro4.Proxy("PYRO:example.gpio@192.168.1.202:5150")

WORDS=["ROJO","APAGAR"]

def light():
	pi1=pigpio.pi()
	pi1.write(18,0)
	

def handle(text, mic, profile):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    #gpio.apagar_rojo()
    light()


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bapagar rojob', text, re.IGNORECASE))




# -*- coding: utf-8-*-
import RPi.GPIO as GPIO
import time
import re
import os
import pigpio
import Pyro4



WORDS=["PONER","M\xdaSICA"]

def light():
	pi1=pigpio.pi()
	pi1.write(8,1)
	

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
        Returns True if the input is related to Hacker News.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(True)


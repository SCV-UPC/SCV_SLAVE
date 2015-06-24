# -*- coding: utf-8-*-
import random
import re

WORDS = ["JULIA"]


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    mic.say("La julia es una persona muy gorda, que trabaja poco y que tambien es fea")


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bjulia\b', text, re.IGNORECASE))
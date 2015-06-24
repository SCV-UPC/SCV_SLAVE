import os
import sys
import shutil
import logging
import Pyro4
import time
import cercaIP

import yaml
import argparse

from client import tts, stt, jasperpath, diagnose
from client.conversation import Conversation

from client.mic import Mic

    
stt_engine_class = stt.get_engine_by_slug('sphinx')
tts_engine_class = tts.get_engine_by_slug('espeak-tts')

stt_engine_class0 = stt.get_engine_by_slug('witaiE')
stt_engine_class1 = stt.get_engine_by_slug('witaiC')
stt_engine_class2 = stt.get_engine_by_slug('googleE')
stt_engine_class3 = stt.get_engine_by_slug('googleC')
stt_engine_class4 = stt.get_engine_by_slug('attE')
stt_engine_class5 = stt.get_engine_by_slug('attC')

mic0 = Mic(tts_engine_class.get_instance(),stt_engine_class.get_passive_instance(),stt_engine_class0.get_active_instance())
mic1 = Mic(tts_engine_class.get_instance(),stt_engine_class.get_passive_instance(),stt_engine_class1.get_active_instance())
mic2 = Mic(tts_engine_class.get_instance(),stt_engine_class.get_passive_instance(),stt_engine_class2.get_active_instance())
mic3 = Mic(tts_engine_class.get_instance(),stt_engine_class.get_passive_instance(),stt_engine_class3.get_active_instance())
mic4 = Mic(tts_engine_class.get_instance(),stt_engine_class.get_passive_instance(),stt_engine_class4.get_active_instance())
mic5 = Mic(tts_engine_class.get_instance(),stt_engine_class.get_passive_instance(),stt_engine_class5.get_active_instance())

class mic_remot():
	
	def escolta_0(self):
		return mic0.activeListenToAllOptions()

	def parla_0(self,text):
		mic0.say(text)

	def escolta_1(self):
		return mic1.activeListenToAllOptions()

	def parla_1(self,text):
		mic1.say(text)

	def escolta_2(self):
		return mic2.activeListenToAllOptions()

	def parla_2(self,text):
		mic2.say(text)

	def escolta_3(self):
		return mic3.activeListenToAllOptions()

	def parla_3(self,text):
		mic3.say(text)

	def escolta_4(self):
		return mic4.activeListenToAllOptions()

	def parla_4(self,text):
		mic4.say(text)

	def escolta_5(self):
		return mic5.activeListenToAllOptions()

	def parla_5(self,text):
		mic5.say(text)


mic_remot=mic_remot()
Pyro4.Daemon.serveSimple({mic_remot:"jasper.mic_remot"},port=5211,host=cercaIP.cerca(),ns=False)



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

conversation = Conversation("JASPER", mic0,mic1,mic2,mic3,mic4,mic5)
conversation.handleForever()


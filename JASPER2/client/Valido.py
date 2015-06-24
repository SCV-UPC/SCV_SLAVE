# -*- coding: utf-8-*-
import re

def isValid(words,text):
	for el in words:
		if bool(re.search(r'\b%s\b'%(el), text, re.IGNORECASE)):
			pass
		else:
			return False
	return True
         

   
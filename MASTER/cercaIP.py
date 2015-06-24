from subprocess import check_output

def cerca():
	"""
	Retorna el valor de la ip local de la Raspberry.
	"""

	IP=check_output(['hostname', '-I'])
	return IP.strip()


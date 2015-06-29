from subprocess import check_output

def cerca():
	
	IP=check_output(['hostname', '-I'])
	return IP.strip()


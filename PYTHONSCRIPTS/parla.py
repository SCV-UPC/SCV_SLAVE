import Pyro4

def parla(IP,n,text):


	mic=Pyro4.Proxy("PYRO:jasper.mic_remot@%s:5211"%(IP))

	if n=='0':

		mic.parla_0(text)
	
	if n=='1':

		mic.parla_1(text)
	
	if n=='2':

		mic.parla_2(text)

	if n=='3':

		mic.parla_3(text)

	if n=='4':

		mic.parla_4(text)

	if n=='5':

		mic.parla_5(text)

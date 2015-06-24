import Pyro4

def escolta(IP,n):


	mic=Pyro4.Proxy("PYRO:jasper.mic_remot@%s:5211"%(IP))

	if n=='0':

		text=mic.escolta_0()
		return text

	elif n=='1':

		text=mic.escolta_1()
		return text

	elif n=='2':

		text=mic.escolta_2()
		return text

	elif n=='3':

		text=mic.escolta_3()
		return text

	elif n=='4':

		text=mic.escolta_4()
		return text

	elif n=='5':

		text=mic.escolta_5()
		return text

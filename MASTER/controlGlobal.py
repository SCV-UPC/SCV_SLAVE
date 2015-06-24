import Pyro4
import time
import cercaIP

def temporitzador():

	try:

		IP=cercaIP.cerca()

		trobat=False
		cercaRaspberrys=Pyro4.Proxy("PYRO:jasper.cercaRaspberrys@%s:5168"%(IP))
		comandesGlobals=Pyro4.Proxy("PYRO:jasper.comandesGlobals@%s:5164"%(IP))
		direccions=cercaRaspberrys.direccions()

		for direccio in direccions:

			diferentsMicrofons=Pyro4.Proxy("PYRO:jasper.diferentsMicrofons@%s:5161"%(direccio))
			pregunta=diferentsMicrofons.valor_actual_pregunta()
			ocupat=comandesGlobals.valor_ocupat()
	
			if pregunta==1 and trobat==False and ocupat==0:

				diferentsMicrofons.modifica(1)
				comandesGlobals.modifica_ocupat(1)
				trobat=True
				
			diferentsMicrofons.modifica_pregunta(0)

	except:

		print "error al temporitzador de control global"
		

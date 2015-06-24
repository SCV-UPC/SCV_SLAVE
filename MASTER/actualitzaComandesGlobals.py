import Pyro4
import cercaIP

def cerca():

	cercaRaspberrys=Pyro4.Proxy("PYRO:jasper.cercaRaspberrys@%s:5168"%(cercaIP.cerca()))
	direccions=cercaRaspberrys.direccions()

	diccionari_complert={}
	for direccio in direccions:

		comandes=Pyro4.Proxy("PYRO:jasper.comandesLocals@%s:5162"%(direccio))
		diccionari=comandes.valor_actual()
		for el in diccionari.keys():
			diccionari_complert[el]=diccionari[el]

	return diccionari_complert

def actualitza():

	cercaRaspberrys=Pyro4.Proxy("PYRO:jasper.comandesGlobals@%s:5164"%(cercaIP.cerca()))
	cercaRaspberrys.modifica_valor(cerca())

if __name__=="__main__":

	actualitza()

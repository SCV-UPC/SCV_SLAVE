import Pyro4
import cercaIP

IP=cercaIP.cerca()

def cerca():
	
	diccionariComandesLocals={}
	f=open("/home/pi/SCV/CONFIGURATION/comandes.txt",'r')
	lines=f.readlines()
	for linia in lines:
		veu,comanda=linia.split('*')
		diccionariComandesLocals[veu]=[comanda,IP]
	return diccionariComandesLocals

def actualitza():

	comandes=Pyro4.Proxy("PYRO:jasper.comandesLocals@%s:5162"%(cercaIP.cerca()))
	comandes.modifica_valor(cerca())

if __name__=="__main__":

	actualitza()

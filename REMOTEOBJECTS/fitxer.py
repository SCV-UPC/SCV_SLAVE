import Pyro4
import cercaIP

IP=cercaIP.cerca()

class fitxer():

	def veure_fitxer(self,path):
		f=open(path,'r')
		text=f.read()
		f.close()
		return text


	def escriure_fitxer(self,path,text):
		f=open(path,'w')
		f.write(text)
		f.close()

a=fitxer()

class fitxer_remot():

	def veure_fitxer(self,path):
		return a.veure_fitxer(path)

	def escriure_fitxer(self,path,text):
		a.escriure_fitxer(path,text)

b=fitxer_remot()
Pyro4.Daemon.serveSimple({b:"jasper.fitxer"},port=5187,host=IP,ns=False)


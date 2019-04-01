class ensta:
	def __init__(self, age):
		self.age=age

	def getAge(self):
		print(self.age)

	
class prof(ensta):
	def __init__(self,matiere,name):
		self.matiere=matiere
		self.name=name

	def getName(self):
		print(self.name)

	def getMatiere(self):
		print(self.matiere)

class eleve(ensta):
	def __init__(self,annee, name):
		self.annee=annee
		self.name=name

	def getName(self):
		print(self.name)

	def getAnnee(self):
		print(self.annee)

		

#ajouter stephen.cneff@gmail.com


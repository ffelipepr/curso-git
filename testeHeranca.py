class Pessoa(object):

	def __init__(self,nome='',sexo='',idade=0):
		self.nome = ''
		self.sexo = ''
		self.idade = 0

	def fazerAniv(self):
		self.idade += 1
		print('Parabéns, %s' % (self.nome))

class Aluno(Pessoa):

	def __init__(self,nome='',sexo='',idade=0,matr=0,curso=''):
		super().__init__(nome,sexo,idade)
		self.matr = matr
		self.curso = curso

	def cancelMatr(self):
		print('Matrícula Cancelada')


class Professor(Pessoa):

	def __init__(self,nome='',sexo='',idade=0,especialidade='',salario=0.0):
		super().__init__(nome,sexo,idade)
		self.especialidade = especialidade
		self.salario = salario

	def receberAumento(self,valor):
		self.salario += valor


class Funcionario(Pessoa):

	def __init__(self,nome='',sexo='',idade=0,setor='',trabalhando=False):
		super().__init__(nome,sexo,idade)
		self.setor = setor
		self.trabalhando = trabalhando

	def mudarTrabalho(self):
		self.trabalhando = not self.trabalhando


p1 = Pessoa()
p5 = Aluno()
p2 = Aluno('Maria','feminino',27)
p3 = Professor('Cláudio','masculino',35)
p4 = Funcionario('Fabiana','feminino',30)

p2.curso = 'Informática'
print(p2.idade)
p2.fazerAniv()
print(p2.idade)
print(p2.curso)
#Adicionando esse comentário o arquivo será modificado e eu poderei inserir essa mudança no git

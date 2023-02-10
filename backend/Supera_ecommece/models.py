from django.db import models


#Classe base para as tabelas Cliente e Funcionarios
class Pessoa(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=100, null=False)
    sobrenome = models.CharField(max_length=100, null=False)
    data_nasc = models.DateField(null=False)
    sexo = models.CharField(max_length=9, null=False)
    cpf = models.IntegerField(unique=True, null=False)
    cep = models.IntegerField()
    user = models.CharField(max_length=30)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=20, null=False)

    class Meta:
        abstract = True


#Classe/tabela realacional com Funcionarios
class Profissoes(models.Model):
    nome = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.nome}'


#Classe/tabela dos jogos
class Jogos(models.Model):
    nome = models.CharField(max_length=150, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    score = models.IntegerField()
    image = models.ImageField()


class Clientes(Pessoa):
    n_telefone = models.IntegerField()


class Funcionarios(Pessoa):
    cargo = models.ForeignKey(Profissoes, on_delete=models.CASCADE, default=None)
    n_Inscricao = models.IntegerField(null=False)

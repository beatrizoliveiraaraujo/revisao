from turtle import mode
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class HelloWorld(models.Model):
    nome = models.CharField(max_length=225, null=True)

class Categoria(models.Model):
    categoria = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.categoria

class Produto(models.Model):
    titulo = models.CharField(max_length=255)
    descritivo = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    qtd_estoque = models.IntegerField(validators=[MinValueValidator(0, "Estoque deve ser igual ou maior que 0."), MaxValueValidator(100, "Estoque deve ser maior que 100.")])
    
    def __str__(self) -> str:
        return self.titulo

class Cliente(models.Model):

    basico = 'B'
    premium = 'P'
    god = 'G'

    tipos_planos = [(basico, 'Básico'), (premium, 'Premium'), (god, 'God')]

    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    celular = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    dataCadastro = models.DateField(auto_now_add=True)
    tipo = models.CharField(max_length=1, choices=tipos_planos, default='B')

    def __str__(self) -> str:
        return self.nome
    class Meta:
        ordering = ['-nome']

class Endereco(models.Model):
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=15)

class Pedido(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    status_analise = 'A'
    status_efetuado = 'E'
    status_recusado = 'R'

    status_preparando = 'P'
    status_caminho = 'C'
    status_efetuado = 'E'

    pagamento_dinheiro = 'D'
    pagamento_cartao = 'C'
    pagamento_pix = 'P'

    status_pagamento = [(status_analise, 'Análise'), (status_efetuado, 'Efetuado'), (status_recusado, 'Recusado')]
    pagamento = models.CharField(max_length=1, choices=status_pagamento, default='A')

    status_pedido = [(status_preparando, 'Preparando'), (status_caminho, 'A caminho'), (status_efetuado, 'Entregue')]
    pedido = models.CharField(max_length=1, choices=status_pedido, default='P')

    preco = models.DecimalField(max_digits=10, decimal_places=2)

    formas_pagamento = [(pagamento_dinheiro, 'Dinheiro'), (pagamento_cartao, 'Cartão'), (pagamento_pix, 'Pix')]
    pagamento = models.CharField(max_length=1, choices=formas_pagamento)


class PedidoItem(models.Model):
    quantidade = models.PositiveIntegerField()
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
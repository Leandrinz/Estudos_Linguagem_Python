from utilidadesCEV.moeda import moedaa
from utilidadesCEV.dado.validacao import leia_dinheiro

n = leia_dinheiro("Digite o preço: R$")
moedaa.resumo(n, 25, 20)
from math import ceil

#1° ARREDONDAR NUMEROS

#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo 
#regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
#e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens
#adequadas.

print("peso")
peso=float(input())
result = peso - 50
oi = round(result)* 4
print (result, oi)


#2° PORCENTAGEM

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#quanto pagou ao IR.
#o salário líquido.
print("qual seu salario bruto?")
salB=float(input())
porc = salB/100
ir = porc*11
inss = porc*8
sind = porc*5
liq = salB - (ir+inss+sind)
print("salario bruto", salB)
print("INSS",inss)
print("Sindicato",sind)
print("Imposto de Renda",ir)
print(" salario liquido",liq)

#3° Resto de divisão

#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
print("Qual o tamanho da area a ser pintada em metros quadrados?")
area=int(input())
lit = area/3
lata = lit//18
rest = lit%18
if(rest >0):
 lata=lata+1
print("você precisará de", lata, "lata/s e o total á pagar é de:R$",lata*80)

#4° Resto de divisão com arredondamento e posibilidades

#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, 
# que custam R$ 25,00.Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor.
print("Qual o tamanho da area a ser pintada em metros quadrados?")
area=int(input())
lit = area/6
folga = (lit/100)*10
lit = lit+folga
lata18 = lit//18
rest18 = lit%18
lata3 = lit//3.6
rest3 = lit%3.6
preco18 = lata18 * 80
if(rest18 >0):
 lata18=lata18+1

if(rest3 >0):
 lata3=lata3+1

latam18 = (lata3//5)
restom18 = lata3 - latam18*5 
def Arredonda(n):
    return int(n + (0 if n % 1 ==  0 else 1)) 

preco3 = lata3 * 25
precoMist = preco18 + (Arredonda(restom18)*25)
print("você precisará de", lata18, "lata/s de 18L e o total á pagar é de:R$",lata18*80)
print("você precisará de", lata3, "lata/s de 3.6L e o total á pagar é de:R$",lata3*25)
print ("vc precisara de",latam18,"latas de 18L e ",Arredonda(restom18),"latas de 3.6 L totalizando R$ ",precoMist)


from math import ceil

#1° ARREDONDAR NUMEROS
print("peso")
peso=float(input())
result = peso - 50
oi = round(result)* 4
print (result, oi)


#2° PORCENTAGEM
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
print("Qual o tamanho da area a ser pintada em metros quadrados?")
area=int(input())
lit = area/3
lata = lit//18
rest = lit%18
if(rest >0):
 lata=lata+1
print("você precisará de", lata, "lata/s e o total á pagar é de:R$",lata*80)

#4° Resto de divisão com arredondamento e posibilidades 
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



#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.


def vogal(z):
    vogais = ['a', 'e', 'i', 'o', 'u']

    if z.lower() in vogais:
       return True

    return False
x = input("escreva sua letra: ")
y= len(x) 
k = vogal(x)
while y>1:
    x = input("escreva apenas uma letra: ")
    y= len(x) 
if k == True:
   print(x," é uma vogal")
else:
    print(x,"é uma consoante")


#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
x =input("escreva a primeira nota do aluno: ")
y = input("escreva a segunda nota do aluno: ")
x=float(x)
y=float(y)
x=(x+y)/2
if(7<=x<10):
   print("Aluno aprovado com média:", x)
elif(x==10):
    print("Aprovado com Distinção, média", x)
else:
    print("aluno reprovado, média:",x)

#Faça um Programa que leia três números e mostre o maior deles.

x =input("escreva o primeiro numero: ")
y = input("escreva o segundo numero: ")
z = input("escreva o terceiro numero: ")


if ((x<y)and(z<y)):
    print(y," é maior que",x,"e",z)

elif((z<x)and(y<x)):
     print(x," é maior que",y,"e",z)

elif((x<z)and(y<z)):
 print(z," é maior que",y,"e",x)
else:
    print("todos os numeros são iguais")

#Faça um Programa que leia três números e mostre o maior e o menor deles.

x =input("escreva o primeiro numero: ")
y = input("escreva o segundo numero: ")
z = input("escreva o terceiro numero: ")


if ((x<y)and(z<y)):
   
    if(x<z):
        print(y," é maior o numero e",x,"o menor")
    else:
        print(y," é maior o numero e",z,"o menor")

elif((z<x)and(y<x)):
    if(y<z):
        print(x," é maior o numero e",y,"o menor")
    else:
        print(x," é maior o numero e",z,"o menor")

elif((x<z)and(y<z)):
    if(x<y):
        print(z," é maior o numero e",x,"o menor")
    else:
        print(z," é maior o numero e",y,"o menor")
else:
    print("todos os numeros são iguais")

#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.


x =float(input("escreva o valor do seu salário: "))
y = 0
if(x<=280):
    y=20
    almento = (x/100)*y
    salAlm = x+almento
    print("seu salario teve um almento de " ,y, "% que resulta em um acrecimo de R$",almento,", então seu salario sairá de", x,"para",salAlm)

    



elif(280<x<=700):
    y=15
    almento = (x/100)*y
    salAlm = x+almento
    print("seu salario teve um almento de " ,y, "% que resulta em um acrecimo de R$",almento,", então seu salario sairá de", x,"para",salAlm)

elif(700<x<=1500):
    y=10
    almento = (x/100)*y
    salAlm = x+almento
    print("seu salario teve um almento de " ,y, "% que resulta em um acrecimo de R$",almento,", então seu salario sairá de", x,"para",salAlm)

else:
    y=5
    almento = (x/100)*y
    salAlm = x+almento
    print("seu salario teve um almento de " ,y, "% que resulta em um acrecimo de R$",almento,", então seu salario sairá de", x,"para",almento)




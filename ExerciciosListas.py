'''
#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
lista = range(5)
for num in lista:
    print(num)

#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
lista = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,0.0]
x=0
for num in lista:
    x=x+1
    print(lista[-x])

#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
x =int(input("escreva a primeira nota do aluno: "))
y = int(input("escreva a segunda nota do aluno: "))
z = int(input("escreva a terceira nota do aluno: "))
v = int(input("escreva a quarta nota do aluno: "))
soma = 0
nota = [x,y,z,v]
for num in nota:
    soma=soma+num
    media = soma/len(nota)
print("a média do aluno é: ",media)

#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
def vogal(z):
    vogais = ['a', 'e', 'i', 'o', 'u']

    if z.lower() in vogais:
       return False
    return True
x = ["a","b","c","e","u","g","p","k","l","a"]
i = 0
y=[]
for letra in x:
    k = vogal(letra)
    if k == True:
        i=i+1
        y.append(letra) 

print("as consoantes na lista são",*y,"totalizando",i,"consoantes")     
 
#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
listaNum= []
impar = []
par=[]
i=0
while i <20:
    z = 20 - i
    print("escreva mais",z,"numeros, um de cada vez")
    x= int(input())
    listaNum.append(x)
    i=i+1
    if(x%2>0):
        impar.append(x)
    else:
        par.append(x)
print("os numeros foram ",*listaNum,"\n osnumeros impares são", *impar,"\n os numeros pares são", *par )
'''
i=0
alunos=[]
alunosshow=[]
while i==0:
    x=int(input("você deseja fazer qual ação\nDigite 1 para adicionar um aluno\nDigite 2 para aplicar nota para um aluno ja existente\n"))   
    if(x==1):
        nome = input("digite o nome do aluno:\n")
        alunos.append(nome)
        alunosshow.append(nome)
        alunos.append([])
    else:
        b=0
        print("escreva o nome para qual aluno você deseja dar nota?")
        for aluno in alunosshow:
            print(aluno)
        escolha = int(input())
        i=i+1
        
    





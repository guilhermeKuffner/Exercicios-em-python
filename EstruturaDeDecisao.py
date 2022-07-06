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
# lado = int(input("Digite o valor do lado do quadrado:"))
#
# perimetro = lado*4
# area = lado**2
#
# print("perímetro:",perimetro, "-área:",area)

# nome = input("Digite o nome do cliente:")
# dia = input("Digite o dia de venciemnto da fatura:")
# mes = input("Digite o mês de vencimento da fatura:")
# valor = input("Digite o valor da fatura:")
#
# print("Olá,",nome)
# print("A sua fatura com vencimento em",dia,"de",mes,"no valor de R$",valor,"está fechada.")

# numero = input("Digite o numero a ser analizado")
#
# try:
#     numero = int(numero)
#     aux = 5
#     aux = numero % 2
#
#     if aux == 0:
#         print("par")
#     else:
#         print("ímpar")
#
#
# except:
#     print("Numero invalido")
#
# import math
#
# x1 = float(input("Digite o x1:"))
# y1 = float(input("Digite o y1:"))
# x2 = float(input("Digite o x2:"))
# y2 = float(input("Digite o y2:"))
#
# dist = (x1*x1 - 2*x1*x2 +x2*x2) + (y1*y1 - 2*y1*y2 + y2*y2)
# dist = math.sqrt(dist)
#
#

#  Semana 4

# if dist>=10:
#     print("longe")
# elif dist<10:
#     print("perto")

# n = int(input("Digite um numero natural:"))
# aux=1
#
# while n!=0:
#     aux = aux*n
#     n-1
#
# print(aux)


# número primo

# n = int(input("Digite um número inteiro:"))
#
# if n==2 or n==5 or n==7:
#     print("primo")
# elif n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0 and n%9!=0:
#     print("primo")
# else:
#     print("não primo")

# Semana 5

# def maximo(n1,n2):
#     if n1> n2:
#         return n1
#
#     elif n2>n1:
#         return n2
#     else:
#         return n1

# def fizzbuzz(i):
#     if i%3==0 and i%5!= 0:
#         return "Fizz"
#     elif  i%5==0 and i%3!= 0:
#         return "Buzz"
#     elif i%3==0 and i%5== 0:
#         return "FizzBuzz"
#     else:
#         return i


# x = 1
# while x < 3:
#     y = 1
#     while y < 3:
#         print(x*y, end = "\t")
#         y = y + 1
#     x = x + 1

#Semana 7
# Fatorial

# n = int(input("Digite um número a ser fatorado:"))
# result =1
# aux=n
#
# while aux!=0:
#     result = aux * result
#     aux-=1
#
# print(result)

# Largura 1 e dps altura
#
# largura = int(input("digite a largura:"))
# altura = int(input("digite a altura:"))
# aux = largura
#
# while altura>0:
#     largura = aux
#     while largura>0:
#         print("#",end="")
#         largura-=1
#     altura-=1
#     print("")


# Semana 8



def remove_repetidos(listav1):

    lista_aux = []
    for i in listav1:
        if i not in lista_aux:
            lista_aux.append(i)
        else:
            lista_aux = lista_aux

    lista_aux = sorted(lista_aux)
    return lista_aux
    # listav1.drop_duplicates()




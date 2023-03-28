# # num0 = int(input("Digite um número para ser analizado:"))
# #
# # verifica = num0 %3
# #
# # if verifica==0:
# #     print("Fizz")
# # else:
# #     print(num0)
#
#
#
#
# a = float(input("Digite o valor A:"))
# b = float(input("Digite o valor B:"))
# c = float(input("Digite o valor C:"))
#
# import math
# delta = (b**2) - (4*a*c)
# try:
#         delta = math.sqrt(delta)
# except:
#         print("tente denovo")
#
#
#
#
# x1 = (-b + delta)/(2*a)
# x2 = (-b - delta)/(2*a)
#
# if delta <0 :
#     print("esta equação não possui raízes reais")
# elif delta ==0:
#     print("a raiz desta equação é",x1)
# else:
#     if x1>x2:
#         print("as raizes da equação são",x1,"e",x2)
#     else:
#         print("as raizes da equação são",x2,"e",x1)
#
# a = 12
# b = 23
#
# while a!=b:
#     if a>b:
#         a -=b
#     elif b>a:
#         b -= a
# print(a, b)

# Semana 4

# n = int(input("Digite um numero natural:"))
# aux=1
# if n==0:
#     print("1")
#
# while n!=0:
#     aux = aux*n
#     n= n-1
#
# print(aux)


# num = int(input("Digite um número inteiro:"))
#
# aux=1
# aux2 =1
# dez =10
# teste =1
# verificateste =1
# guarda =0
# cont =1
#
#
# while teste!=0:
#
#     aux = num%dez
#     aux = aux//(dez//10)
#     dez = dez *10
#     guarda = aux
#
#     cont+=1
#     dez2 = 10**cont
#     teste2 =1
#     while teste2 !=0:
#         aux2 = num%dez2
#         aux2 = aux2//(dez2//10)
#         dez2 = dez2 *10
#
#         if guarda ==aux2:
#             print("sim")
#             teste =0
#             teste2 =0
#
#         if aux2==0:
#             teste2 =0
#
#
#     verificateste = num%(dez//10)
#     if verificateste == num:
#         teste = 0
#         print("não")


#Semana 5

# def maior_primo(n):
#     print
#     n = primo(n)
#     return n
#
#
#
# def primo(k):
#     i =0
#     if k==2 or k==5 or k==7:
#         return k
#     elif k%2!=0 and k%3!=0 and k%5!=0 and k%7!=0 and k%9!=0:
#         return k
#     else:
#         last_primo =1
#         while i<=k:
#             if i == 2 or i == 5 or i == 7:
#                 last_primo = i
#             elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 9 != 0:
#                 last_primo = i
#
#             i+=1
#
#         return last_primo

# def maximo(n1,n2,n3):
#
#     if n1> n2 and n1>n3:
#         return n1
#     elif n2>n1 and n2>n3:
#         return n2
#     elif n3 > n2 and n3 > n1:
#         return n3
#     else:
#         return n1

#
# largura = int(input("digite a largura:"))
# altura = int(input("digite a altura:"))
# count = 1
# alt = altura
#
# while altura>0:
#     count2 =1
#     aux = largura
#     aux2 = largura
#     if count ==1 or count==altura:
#         while aux>0:
#             print("#",end="")
#             aux-=1
#         print("")
#     count += 1
#     if altura == alt or altura!=2 :
#         while aux2>0:
#             if count2==1 or count2== largura:
#                 print("1", end="")
#             else:
#                 print(" ", end="")
#             aux2-=1
#             count2 +=1
#         print("")
#     altura-=1

def soma_elementos(lista1):
    soma =0
    for i in lista1:
        soma += i

    return soma



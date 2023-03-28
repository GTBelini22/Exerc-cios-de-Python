# num0 = int(input("Digite um número para ser analizado:"))
#
# verifica3 = num0 %3
# verifica5 = num0 %5
#
# if verifica3==0 and verifica5==0:
#     print("FizzBuzz")
# else:
#     print(num0)
#
#
# ok = 81**0.5
# print(ok)

# num0 = int(input("Digite um número inteiro:"))
#
# deze = num0%100
# deze //=10
#
# print("O dígito das dezenas é:",deze)
#
# b =a

#       Semana 4

# num = int(input("Digite um número inteiro:"))
#
# aux=1
# dez =10
# soma = 0
# teste =1
# verificateste =1
#
# while teste!=0:
#
#     aux = num%dez
#     aux = aux//(dez//10)
#     dez = dez *10
#     soma += aux
#     verificateste = num%(dez//10)
#     if verificateste == num:
#         teste = 0
#
# print(soma)

# def proc3(x , y):
#     if y<0:
#         return -1
#     if y==0:
#         return 1
#     else:
#         return proc3(x,y-1)*x
#
# print(proc3(4,3))


# def funci(n):
#     if n==0:
#         return 1
#     else:
#         print(n)
#         return funci(n-1)+funci(n-1)
#
# print(funci(3))

# def funcio(a):
#     if a<=0:
#         return 0
#     else:
#         return a+funcio(a-1)
#
# print(funcio(5))
for cont in range(10, -20):

     print(cont)
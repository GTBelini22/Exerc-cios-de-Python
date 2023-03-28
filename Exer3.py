# num0 = int(input("Digite um número inteiro:"))
#
# deze = num0%100
# deze //=10
#
# print("O dígito das dezenas é:",deze)
#
# b =a


# num0 = int(input("Digite um número para ser analizado:"))
#
# verifica = num0 %5
#
# if verifica==0:
#     print("Fizz")
# else:
#     print(num0)

# Semana 4

# n = int(input("Digite o valor de n:"))
# aux =1
# while n!=0:
#     print(aux)
#     aux = aux +2
#     n = n-1

#Semana 5

# def vogal(v):
#     resp = True
#
#     if v =="a" or v=="e" or v=="i" or v=="o" or v=="u":
#         return resp
#     else:
#         resp = False
#         return resp

# s = "e"
# print (vogal(s))

def desenhaQuadrado(altura, largura, simbolo = '#', preenchimento = ' '):
    print(simbolo * largura)
    for _ in range(altura-2):
        print('{}{}{}'.format(simbolo, preenchimento * (largura - 2), simbolo))
    print(simbolo * largura)


largura1 = int(input("digite a largura:"))
altura1 = int(input("digite a altura:"))

desenhaQuadrado(altura1, largura1)
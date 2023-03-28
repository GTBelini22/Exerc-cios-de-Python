print("Programa de loja\n")
print("Produtos com código\n 0 a 25 com 10% \n 26 a 50 com 12,5% \n 51 a 100 15%")


aux = 0.0

rep = True
while rep:
        cod = int(input("Digite o código do produto: "))
        valor = float(input("Digite o valor do produto: "))

        if cod >=0 and cod<=10:
            aux = valor * 0.1
            valor -= aux
            print("O valor com desconto do produto será: %.2f \n Obrigado e volte sempre!"%(valor))
            rep = False
        elif cod >=26 and cod <= 50:
            aux = valor * 0.125
            valor -= aux
            print("O valor com desconto do produto será: %.2f \n Obrigado e volte sempre!" % (valor))
            rep = False
        elif cod >= 51 and cod <=100:
            aux = valor * 0.15
            valor -=aux
            rep = False
            print("O valor com desconto do produto será: %.2f \n Obrigado e volte sempre!" % (valor))
        else:
            print("Número invalido!")


# nota1 = float(input("Digite sua primeira nota:"))
# nota2 = float(input("Digite sua segunda nota:"))
# nota3 = float(input("Digite sua terceira nota:"))
# nota4 = float(input("Digite sua quarta nota:"))
#
# media = (nota1 +nota2 + nota3 + nota4)/4
#
# print("A média aritimética é",media)

seg = int(input("Por favor,entre com o número de segundos que deseja converter:"))

dia = seg //86400
horas = (seg - 86400*dia)//3600
restseg = seg % 3600
minutos = restseg // 60
finalseg = restseg %60

print(dia,"dias,",horas,"horas,",minutos,"minutos e",finalseg,"segundos.")
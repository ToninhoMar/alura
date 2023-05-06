dia = 0
while dia < 1 or dia > 31:
   dia = int(input("Digite um dia entre 1 e 32: "))
   if dia < 1 or dia > 31: 
        print("Esse dia esta incorreto tente novamente")
        continue
mes = 0
while mes < 1 or mes > 12:
    mes = int(input("Digite o mes que estamos: "))
    if mes < 1 or mes > 12: 
        print("Esse mes não existe, tente novamente")
        continue
ano = 0
while ano < 1 or ano > 2023:
    ano = int(input("Qual ano estamos: "))
    if ano < 1 or ano > 2023: 
        print("Esse ano não existe, tente novamente")
        continue
print("Pelo visto estamos no dia {:02d}, no mes {:02d} e no ano {:04}".format(dia,mes,ano))


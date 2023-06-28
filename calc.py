while(True):
    print ("1. Somar", "2.subtrair", "3.multiplicar", "4. dividir", "5. sair", sep="\n")
    op = int(input("escolha uma opção: "))
    if op<1 or op>5:
        print("opção inválida")
        continue 
    elif op == 5:
        break
    n = int(input("digite o primeiro número: "))
    m = int(input("digite o segundo número: "))

    if op == 1:
        print(f"{n}+{m} = {n+m}")
    elif op == 2:
        print(f"{n}-{m} = {n-m}")
    elif op == 3:
        print(f"{n}*{m} = {n*m}") 
    else:
        pass
print("até logo")

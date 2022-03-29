x = int(input("Digite o número 1: "))
y = int(input("Digite o número 2: "))
aux = int(input("Escolha qual operação quer fazer: \n(1)Soma \n(2)Subtação \n(3)Divisão \n(4)Multiplicação\n"))


if aux == 1:
    result = x + y
    print(result)
elif aux == 2:
    result = x - y
    print(result)
elif aux == 3:
    result = x / y
    print(result)
elif aux == 4:
    result = x * y
    print(result)
else:
    print("O formato digitado está incorreto (escolha de 1 a 4).")
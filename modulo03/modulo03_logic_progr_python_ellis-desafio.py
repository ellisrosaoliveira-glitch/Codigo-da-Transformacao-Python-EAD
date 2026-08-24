print("===== CALCULADORA EM PYTHON =====")

while True:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    print("\nEscolha uma operação:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("5 - Potência (**)")
    print("6 - Resto da divisão (%)")

    opcao = input("Digite o número da operação: ")

    if opcao == "1":
        print("Resultado:", numero1 + numero2)

    elif opcao == "2":
        print("Resultado:", numero1 - numero2)

    elif opcao == "3":
        print("Resultado:", numero1 * numero2)

    elif opcao == "4":
        if numero2 != 0:
            print("Resultado:", numero1 / numero2)
        else:
            print("Erro: não é possível dividir por zero!")

    elif opcao == "5":
        print("Resultado:", numero1 ** numero2)

    elif opcao == "6":
        if numero2 != 0:
            print("Resultado:", numero1 % numero2)
        else:
            print("Erro: não é possível calcular o resto da divisão por zero!")

    else:
        print("Opção inválida!")

    continuar = input("\nDeseja fazer outra conta? (s/n): ").lower()

    if continuar != "s":
        print("Obrigado por usar a calculadora!")
        break
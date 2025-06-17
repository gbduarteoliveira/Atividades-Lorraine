def decimal_p_binario():
   num = int(input("Digite um número: "))  

   if num == 1:
      return 1
   elif num == 0:
      return 0
   else:
      binario = []  
      while num > 0:
         resto = num % 2
         if resto == 0:
            binario.append("0")
         else:
            binario.append("1")
         calc= num // 2 
         num= calc
      resultado= binario[::-1] 
      return "".join(resultado)

def binario_p_decimal():
    binario = input("Digite um número binário: ")
    tamanho = len(binario)
    soma = 0
    for i in range(tamanho):
        d = int(binario[::-1][i])
        c = d * (2 ** i)
        soma = soma + c
    # decimal = int(binario, 2)
    print(f"O número decimal é: {soma}")


def menu():
    while True:
        print("Escolha uma opção:")
        print("1 - Dec para Bin")
        print("2 - Bin para Dec")
        print("3 Sair")
        
        opcao = input(" Digite uma opção: ")

        if opcao == "1":
           r= decimal_p_binario()
           print(r)
        elif opcao == "2":
            binario_p_decimal()
        elif opcao == "3":
            print("fechando")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()





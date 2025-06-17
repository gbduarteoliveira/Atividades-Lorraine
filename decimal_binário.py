# def decimal_p_binario():
#     num = int(input("Digite um número: "))  

#     if num == 1:
#         print("O binário é: 1")
#     elif num == 0:
#         print("O binário é: 0")
#     else:
#         binario = []  
#         while num > 0:
#             resto = num % 2
#             if resto == 0:
#                 binario.append("0")
#             else:
#                 binario.append("1")
#             calc= num // 2 
#             num= calc
#             binario.reverse()
#     print("".join(binario))

def binario_p_decimal():
   binario=int(input("digite um binario"))
   num=str(binario)
   for i in range(len (num)):
      novo=int(num[i])
      num.reverse()
      print(num)
def binario_p_decimal():


# decimal_p_binario():




#     #menu
# print("escolha uma opção")
# print("1 decimal para binário")
# print("2 binário para decimal")
# opcao=input("escola uma opção(1 ou 2)")
# if opcao == 1:
#     print("o binário é {}")
# else:
#     print ("o decimal é {}")
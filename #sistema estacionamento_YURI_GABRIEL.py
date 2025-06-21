# SISTEMA DE ESTACIONAMENTO

# lISTAS PARA ARMAZENAR DADOS
Vagas = [] 
Status = []  

#LAÇO QUE IRÁ PREENCHER AS LISTAS 
for i in range(1, 21): 
    Vagas.append(f"V{i}")
    Status.append("Livre")

# LISTAS PARA REGISTRO DE DADOS PARA CADASTRO 

Nome = []  
Placa = []  
Modelo = []  
Vaga_escolhida = []  
Valor = [] 

# MENU DO SISTEMA
def sistema():

# LOOP PARA MANTER O SISTEMA FUNCIONANDO
    while True: 
        print("SISTEMA DE VAGAS DE ESTACIONAMENTO")
        print("1 - VAGAS ")
        print("2 - REGISTRO DO VEÍCULO")
        print("3 - ENCERRAR SISTEMA")
    
        opcao = input("Escolha uma opção: ")

 # EXIBE AS VAGAS COM SEU STATUS ATUAL 
        if opcao == "1":

            for i in range(len(Vagas)):
                print(Vagas[i], " - ", Status[i])
            print("1 - Voltar ao menu inicial")
            Voltar = input("Digite uma opção: ")
            if Voltar == "1":
                continue  

 #  CADASTRO DE VEÍCULO      
        elif opcao == "2":
            print("CADASTRO")
            nome = input("Nome do proprietário: ")
            placa = input("Placa do veículo: ")
            modelo = input("Modelo: ")

   # EXIBE AS VAGAS PARA ESCOLHER          
            print("Escolha a vaga desejada:")
            for i in range(len(Vagas)):
                print(Vagas[i], " - ", Status[i])
            
            vaga_escolha = input("Vaga: ").strip().upper()

   # VERIFICA SE A VAGA EXISTE E ESTÁ LIVRE         
            if vaga_escolha in Vagas:
                posicao = Vagas.index(vaga_escolha)
                if Status[posicao] == "Livre":
                    Status[posicao] = "Ocupado"
                    Tempo = input("Tempo em horas de utilização do estacionamento: ")
                    Preco_por_hora = float(Tempo) * 5
                    Nome.append(nome)
                    Placa.append(placa)
                    Modelo.append(modelo)
                    Vaga_escolhida.append(vaga_escolha)
                    Valor.append(Preco_por_hora)
                    print("Registro realizado com sucesso!")

                    print(f"Valor a ser pago pelo uso do estabelecimento: R$ {Preco_por_hora:.2f}")
                else:
                    print("Vaga ocupada")
            else:
                print("Vaga não existe")
            
            print("1 - Voltar")
            opcao = input()
            if opcao == "1":
                continue 
        
        elif opcao == "3":
            print("Encerrando sistema...")
            break
        
        else:
            print("opcao inválida")

# EXECUTA O SISTEMA
sistema()


#GABRIEL OLIVEIRA DUARTE
#YURI OLIVEIRA DUARTE
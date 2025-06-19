import random
palavras = ["python", "computador", "programação", "teclado", "chatgpt", "internet"]


def mostrar_boneco(erros):
    cabeca = "O" if erros >= 1 else " "
    tronco = "|" if erros >= 2 else " "
    braco_esq = "/" if erros >= 3 else " "
    braco_dir = "\\" if erros >= 4 else " "
    perna_esq = "/" if erros >= 5 else " "
    perna_dir = "\\" if erros >= 6 else " "
    print(" -----")
    print(" |   |")
    print(f" |   {cabeca}")
    print(f" |  {braco_esq}{tronco}{braco_dir}")
    print(f" |  {perna_esq} {perna_dir}")
    print(" -----")
    
    
def jogo_forca():
    palavras_aleatoria = random.choice(palavras)
    palavras_descobertas = ["_" for _ in palavras_aleatoria]
    numero_max_de_erros = 6
    erros = 0
    letras_chutadas = []
    palpites = 0

    while erros < numero_max_de_erros and "_" in palavras_descobertas:
        print("palavra:", "".join(palavras_descobertas))
        print("letras já usadas:", ",".join(letras_chutadas))
        print(f"erros restantes: {numero_max_de_erros - erros}")
        mostrar_boneco(erros)

        palpite = input("Digite uma letra: ").lower()
        palpites += 1

        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if palpite in letras_chutadas:
            print("Você já chutou essa letra, tente outra.")
            continue

        letras_chutadas.append(palpite)

        if palpite in palavras_aleatoria:
            for i, letra in enumerate(palavras_aleatoria):
                if letra == palpite:
                    palavras_descobertas[i] = palpite 
                    print("boa palavra correta")
        else:
            erros += 1

    if "_" not in palavras_descobertas:
        print(f"parabéns você ganhou A palavra era: {palavras_aleatoria}")
    else:
        mostrar_boneco(erros)
        print(f"Infelizmente Você perdeu A palavra era: {palavras_aleatoria}")

        if palpites==True:
            print("Boa, letra correta")

while True:
    jogo_forca()
    resposta = input("Deseja jogar novamente? (sim / não): ")
    if resposta != "sim":
        print("Obrigado por jogar!")
        break






import random

def gerar_operacao():
    operadores = ['+', '-', '*', '/']
    numero1 = random.randint(0, 10)
    numero2 = random.randint(1, 10)  
    operador_aleatorio = random.choice(operadores)
    return numero1, numero2, operador_aleatorio

def gerar_resultado(n1, n2, operador):
    if operador == '+':
        return n1 + n2
    elif operador == '-':
        return n1 - n2
    elif operador == '*':
        return n1 * n2
    elif operador == '/':
        return (n1 / n2)

pontos = 0
acertos = 0
rodadas = 0
total_de_rodadas = 20

while rodadas < total_de_rodadas:
    rodadas += 1

    numero1, numero2, operador_aleatorio = gerar_operacao()
    resultado = gerar_resultado(numero1, numero2, operador_aleatorio)
    print(f" {numero1} ?? {numero2} = {resultado}")

    palpite = input("Digite o operador (+, -, *, /): ")

    if palpite == operador_aleatorio:
        pontos += 99
        acertos += 1
        print(f"Correto! Você ganhou{pontos}  pontos e {acertos} acerto!")
    else:
        print(f"Errado. O operador correto era: {operador_aleatorio}")

print(f"Fim do jogo! Total de pontos: {pontos}")
print(f"Total de acertos: {acertos} em {total_de_rodadas} rodadas.")


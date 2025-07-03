import random
from colorama import init, Fore, Style

init(autoreset=True)  # Ativa o colorama

def obter_escolha():
    try:
        escolha = int(input(Fore.YELLOW + "Escolha um número entre 1 e 10: "))
        if (escolha < 1) or (escolha > 10):
            print(Fore.RED + "Escolha inválida! Digite um número entre 1 e 10.")
            return obter_escolha()
        return escolha
    except ValueError:
        print(Fore.RED + "Entrada inválida! Digite apenas números.")
        return obter_escolha()

def determina_resultado(jogador, computador):
    if jogador == computador:
        return Fore.GREEN + "Parabéns, você acertou!"
    else:
        return Fore.RED + "Não foi dessa vez."

def jogar_game():
    print(Style.BRIGHT + Fore.CYAN + "Bem-vindo ao jogo")
    while True:
        jogador = obter_escolha()
        escolhas = list(range(1, 11))  # de 1 a 10
        computador = random.choice(escolhas)
        print(Fore.YELLOW + f"Você escolheu: {jogador}")
        print(Fore.YELLOW + f"O computador escolheu: {computador}")
        resultado = determina_resultado(jogador, computador)
        print(resultado)
        print(Fore.CYAN + "=====================")
        resposta = input(Fore.CYAN + "Deseja jogar novamente? (s/n): ").lower()
        if resposta != "s":
            print(Fore.MAGENTA + "Obrigado por jogar!")
            break

jogar_game()

# Programa para controle de nível de água em um reservatório
# Autor: Fernando José Santiago


#gera numeros aleatórios
import random

#gera cores no terminal
from colorama import Fore, Style

#Verifica o sistema e limpa a tela
import os
os.system('cls' if os.name == 'nt' else 'clear')   


# Programa para controle de nível de água em um reservatório

def verificar_nivel_agua(nivel_agua): # Função para verificar o nível de água e exibir a mensagem correspondente
    criticidade = ["Muito baixo(crítico)", "Baixo", "Médio", "Alto", "Muito Alto(alerta)"] # 
    if criticidade[nivel_agua - 1] == "Muito baixo(crítico)": # checa o nível de água e exibe a mensagem correspondente com a cor apropriada
        print(Fore.RED + "Nível de água muito baixo! Ação imediata necessária!") # Exibe mensagem em vermelho
    elif criticidade[nivel_agua - 1] == "Baixo":# checa o nível de água e exibe a mensagem correspondente com a cor apropriada
        print(Fore.YELLOW + "Nível de água baixo! Atenção!") # Exibe mensagem em amarelo
    elif criticidade[nivel_agua - 1] == "Médio": # checa o nível de água e exibe a mensagem correspondente com a cor apropriada
        print(Fore.GREEN + "Nível de água médio. Situação estável.") # Exibe mensagem em verde
    elif criticidade[nivel_agua - 1] == "Alto": # checa o nível de água e exibe a mensagem correspondente com a cor apropriada
        print(Fore.CYAN + "Nível de água alto. Monitoramento necessário.") # Exibe mensagem em ciano
    elif criticidade[nivel_agua - 1] == "Muito Alto(alerta)": # checa o nível de água e exibe a mensagem correspondente com a cor apropriada
        print(Fore.BLUE + "Nível de água muito alto! Ação imediata necessária!") # Exibe mensagem em azul

print("***Sistema de Controle de Nível de Água***") # Programa para controle de nível de água em um reservatório
nivel_agua = random.randint(1, 5) # Gera um número aleatório entre 1 e 5 para representar o nível de água
verificar_nivel_agua(nivel_agua) # Chama a função para verificar o nível de água e exibir a mensagem correspondente
print(Style.RESET_ALL)  # Resetar a cor para o padrão




# engine.py 

# nada de história, capitulo ou preludio

# lembrete mental: EU SÓ PRECISO DESSAS BIBLIOTECAS!

# checklist: typewriter/mostrar_texto, escolher, só.
# falta: class jogador.py, passar o limpar_tela() pra cá, save_data pra cá, load_data pra cá.

import json
import sys
import os
import time
from rich.console import Console
from rich.live import Live
from rich.text import Text

console = Console()

# ENGINE: TYPEWRITER

def mostrar_texto(texto, atraso=0.07, rapido=False):
    if rapido: # se rapido= print ao invés de typewriter
        console.print(texto)
        return

    texto_render = Text.from_markup(texto)
    atual = Text()

    with Live(atual, refresh_per_second=30, console=console) as live:
        for i in range(len(texto_render)):
            atual = texto_render[:i+1]
            live.update(atual)
            time.sleep(atraso)
        # exemplo: mostrar_texto("esse texto vai ser em typewriter com atraso mais alto!", atraso=0.08, rapido=False)
    

# ENGINE: ESCOLHER

def escolher(opcoes):
    while True:
        for i, opcao in enumerate(opcoes, 1):
            print(f"[{i}] {opcao}")

        try:
            escolha = int(input("Escolha: "))
            return escolha

            if 1 <= escolha <= len(opcoes):
                return escolha
            else:
                print("Erro. Digite somente as opções do menu!")
        except ValueError:
                print("Escolha inválida. Digite um número.") # exemplo: opcao = escolher(["Ler o bilhete", "Não ler"])
            

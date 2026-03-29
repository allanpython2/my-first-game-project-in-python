# bibliotecas pra carregar
import time
import sys
import os
import random
import json
from rich import print

jogador_status = None

def criar_novo_jogo(nome):
    return {
        "nome": nome,
        "vida": 35,
        "vida_max": 35,
        "ataque": 10,
        "inventario": [],
        "capitulo": 1,
        "tutorial_concluido": False
    }
# frases pra se o jogador escolher sair do menu
frases = ["Dando o fora...", "Saindo...", "Não vou perder meu tempo nesse jogo..."]
# game over
def game_over():
    global jogador_status
    morte = input("Aperte ENTER para voltar à batalha ou X para aceitar seu destino e voltar ao menu.").upper()
    if morte == "":
        typewriter("De novo não...", atraso=0.2)
        jogador_status['vida'] = jogador_status['vida_max']
        Preludio()
    elif morte == "X":
        limpar_tela()
        menu_inicial()

# efeito typewriter
def typewriter(texto, atraso=0.08):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(atraso)
    print()
# mensagem secreta rara (um em mil!)
fun = random.randint(1, 1000)
if fun == 1:
    typewriter("odadiuC moC eleuqA euQ alaF moC sa soãM.", atraso=1.0)
    input("...")
    sys.exit()

# limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
# carregar jogo no menu em json (eu ODEIO MUITO json)
def carregar_jogo():
    while True:
        global jogador_status
        try:
            with open("save.json", "r") as arquivo:
                jogador_status = json.load(arquivo)
            print("[bold green][=] Ainda há esperança! Save carregado com sucesso.[/]")
            time.sleep(0.9)
            return True
            time.sleep(0.5)
        except FileNotFoundError:
            print("[italic red][!] Mas ninguém veio. Nenhum save encontrado.[/]")
            return False
# save data em json (eu ODEIO json)
def salvar_jogo():
    with open("save.json", "w") as arquivo:
        json.dump(jogador_status, arquivo, indent=4)
    print("[bold yellow][+] Jogo salvo automaticamente.[/]")
    time.sleep(0.5)
# primeira parte da história:
def Preludio():
    limpar_tela()
    typewriter("Jardim de Cinzas.\nCapítulo 1: Tutorial.")
    typewriter(f"[???] {jogador_status['nome']}, acorda!! você vai se atrasar pra escola!!!")
    typewriter("...")
    time.sleep(1)
    typewriter("Quem será que é agora?")
    time.sleep(1)
    typewriter("devagarzinho, você levanta as pálpebras e vê quem é...")
    print("É A SUA MÃE!!!")
    time.sleep(0.4)
    typewriter("[MÃE MUITO IRRITADA] TÁ ESPERANDO O QUÊ? LEVANTA DA CAMA E VAI SE ARRUMAR!")
    time.sleep(0.4)
    typewriter("Você olha o calendário escolar.")
    typewriter("Hoje é domingo.")
    time.sleep(0.4)
    typewriter("Antes que você pudesse dizer algo ou fechar a porta, alguém chega no corredor e interrompe sua mãe...")
    time.sleep(1)
    print("É sua irmã, Isa!")
    time.sleep(1)
    typewriter(f"[Isa] Mãe, hoje não tem aula, é DOMINGO, SETE HORAS DA MANHÃ!! Deixa o {jogador_status['nome']} dormir e depois desce pra tomar café.")
    time.sleep(1)
    typewriter("[Isa] Na verdade, EU estou atrasada, pro curso musical que VOCÊ tinha que me levar, lembra?")
    time.sleep(2)
    print("Bate um silêncio ensurdecedor no quarto. Sua mãe procura as palavras, mas nada saiu da boca dela.")
    time.sleep(2)
    typewriter(f"[Mãe] Na verdade, por que não deixamos o {jogador_status['nome']} decidir se ele quer dormir ou te levar, hein?")
# interação do jogador

    print("\nO que você quer?")
    acao_jogador = input("\n[1] Dormir\n[2] Ir com a Isa")
    if acao_jogador == "1":
        typewriter(f"\n[Isa] Poxa, {jogador_status['nome']}, vamos logo!")
        time.sleep(1)
        typewriter(f"{jogador_status['nome']}...Tá.")
        typewriter("Sem opções, você se arruma e sai de casa com ela.")
        return Tutorial()
    elif acao_jogador == "2":
        typewriter("[Isa] Obaa, Vamos logo!")
        return Tutorial()
    else:
        print("\n[!] Erro! Digite apenas um dos números listados!")
        return "erro"
# preparando o tutorial
def Tutorial():
    limpar_tela()
    salvar_jogo()
    typewriter(f"[Isa] {jogador_status['nome']}, antes de eu ir pro curso, preciso te ensinar a se defender pra quando você voltar pra casa.")
    time.sleep(0.4)
    typewriter("[Isa] Tá vendo aqueles bem-te-vi? Se você passar por eles, eles vão LUTAR com você. Eu sei, é meio estranho lutar com PÁSSAROS, mas é melhor prevenir do que remediar, né?")
    typewriter("[Isa] Vamos lá, lutar com eles! Não se preocupe, se eu ver que você vai CAIR, eu paro a luta e nós voltamos depois!")
    time.sleep(1)
    print("Entrando na luta...")
    time.sleep(1)
    typewriter("[!] Rápido! Um bem-te-vi feroz se aproxima! O que você faz?")
    typewriter(f"[Isa] {jogador_status['nome']}, sempre que você entrar em uma batalha, tente ANALISAR o inimigo, assim, você pode ver quanto de VIDA ele tem! Ah, e antes que eu me esqueça, você tem {jogador_status['vida']} de VIDA!")
    print("Você analisou o inimigo.")
    # status inimigo
    time.sleep(2)
    inimigo_tutorial_vida = 10
    inimigo_tutorial_ataque = 10
    # voltando pra luta
    typewriter(f"[!] Bem-te-vi furioso! {inimigo_tutorial_vida} de VIDA. Apesar do tamanho pequeno, dá {inimigo_tutorial_ataque} de DANO!")
    jogador_status['vida'] -= inimigo_tutorial_ataque
    typewriter(f"[!] Bem-te-vi atacou {jogador_status['nome']}! Agora, {jogador_status['nome']} tem {jogador_status['vida']} de VIDA!")
    if jogador_status['vida'] <= 0:
        return "derrota"
    typewriter(f"[Isa] Eita, eu esqueci de te avisar, mas ANALISAR um inimigo PULA seu TURNO, e vai pro TURNO DO INIMIGO. É bom saber quando usar! Tente atacar ele de volta!\nAh, e seu ataque padrão dá {jogador_status['ataque']} de dano, mas você pode pegar armas e aumentar seu dano também!")
    inimigo_tutorial_vida -= jogador_status['ataque']
    typewriter(f"[!] Você acertou o bem-te-vi em cheio! A vida do bem-te-vi é: {inimigo_tutorial_vida}")
    # condicao de vitoria
    if inimigo_tutorial_vida <= 0:
        print(f"[Isa] Obaaa! {jogador_status['nome']}, você matou o bem-te-vi!")
        print("[!] Indo para o próximo capítulo...")
        time.sleep(2)
        jogador_status["tutorial_concluido"] = True
        jogador_status["capitulo"] = 2
        salvar_jogo()
        return capitulo2()
        return "vitoria"
    else:
        return "derrota"
    
# escrevendo o capitulo 2 aqui!!
def capitulo2():
    global jogador_status
    nome = jogador_status['nome']
    limpar_tela()
    typewriter(f"[Isa] Tchau {jogador_status['nome']}! Fica bem tá? Olha, como presente, vou te dar essa Faca, tá bom?")
    print("\n[+] Faca foi adicionado ao Inventário, dentro do status do jogador. Você pode abrir o Inventário em Lutas ou no menu principal.") 
    time.sleep(0.4)
    jogador_status['inventario'].append("Faca de Carne")
    print("[!] A Faca não serve apenas para cortar! ao invés de você lutar de mãos vazias, a faca causa 13 de dano!")
    time.sleep(0.4)
    input("Pressione qualquer coisa para mostrar o inventário...")
    print(f"\ninventário: {','.join(jogador_status['inventario'])}\n")
    input("pressione qualquer coisa para sair do inventário...")
    limpar_tela()
    typewriter("[!] Jardim de Cinzas.")
    time.sleep(0.7)
    typewriter("Prólogo: O Pesadelo do Menino.")
    time.sleep(0.7)
    typewriter("Você acorda na sua cama, sem memórias de ter voltado pra casa.")
    ler= input("No espelho ao lado, há um papel colado. Ler? [S/N]")
    if ler.strip().upper() == "S":
        limpar_tela()
        typewriter("No papel, está escrito 'Ser humano', apenas.\nVocê encara o espelho. É você. Apesar de tudo, ainda é >>você<<.")
        time.sleep(2)
    typewriter("A casa está quieta, quase dando pra escutar sua respiração.")
    typewriter("A porta do quarto range quase gritando um aviso de que você saiu. Todas as luzes estão apagadas.")
    typewriter(f"[Isa?] OOOOOOOH {jogador_status['nome']}, abre aqui pra mim por favorzinho? Deixei meu chaveiro cair no esgoto, nojeira!")
    typewriter("Você desce a escada com cuidado, segurando no corrimão. Manchas marrons e um cheiro metálico gruda na sua mão.")
    typewriter("[Isa?] Finalmente! Abre logo aí, tô cansada!")
    typewriter("Tudo está escuro. Você não consegue achar a chave. Droga...")
    typewriter("Se apoiando em cantos vazios pra não cair, você vai até o olho de vidro pra pedir paciência.")
    typewriter("De repente, uma sombra espreita de cima da escada, estranhamente familiar:")
    typewriter(f"{jogador_status['nome']}, teve outro pesadelo de novo? Não abre a porta pra estranhos, você tá doente!")
    typewriter("É a Isa. Realmente, é a Isa.", atraso=0.7)
    typewriter(f"[???] {jogador_status['nome']}, não escuta ela! Abre a porta!")
    typewriter(f"[Isa] Por tudo que é mais sagrado, NÃO ABRE, {jogador_status['nome']}!!!!")
    typewriter("A coisa do outro lado da porta se acalmou.")
    typewriter(f"[O que tá acontecendo?] {jogador_status['nome']}, abre pra sua irmãzinha, vai!!")
    typewriter("[Isa] NÃO!")
    typewriter("Você decide espiar pelo olho de vidro.")
    limpar_tela()
    typewriter("Você vê um vulto incessante se espalhando pelo quintal, como uma sombra.")
    typewriter("Aquilo não é a Isa. Nunca foi.", atraso=0.6)
    time.sleep(2)
    typewriter("A voz levemente chiada, como uma gravação antiga.\nO horário atrasado.\nEla sabia que eu desconfiaria...")
    typewriter("O que quer que seja, sabe como eu penso.")
    typewriter("Há quanto tempo esse pesadelo está comigo? Por que COMIGO? Só eu vejo isto? O que vão achar de mim????!!!!")
    time.sleep(0.7)
    limpar_tela()
    typewriter(f"... {jogador_status['nome']} caiu no chão, apavorado.")
    time.sleep(0.5)
    typewriter(f"[Isa] {jogador_status['nome']}, por favor! Não vai agora... Fala comigo! Eiii!!")
    typewriter("Você acorda no quarto, completamente consciente do que aconteceu. Não foi só um sonho ruim.")
    typewriter("[Isa] Ah, céus! Quer me fazer morta também? Você caiu tremendo em frente a porta, dizendo nada com nada! Já passou, já passou, você tá bem, tá? Está melhor que antes, pelo menos...")
    typewriter("[Isa] eu vou pegar uma água com açúcar pra ver se você se acalma, tá?")
    typewriter("[!] Enquanto o jogador estiver APAVORADO, ele NÃO causará DANO.")
    capitulo3()

# escrevendo o capitulo 3 aqui

def capitulo3():
    global jogador_status
    jogador_status['capitulo'] = "3"
    salvar_jogo()
    typewriter("Jardim de Cinzas. Capítulo 1: Negação")
    print("[bold]em breve!![/bold]")
    menu_inicial()
# iniciar novo jogo

def iniciar_novo_jogo():
    global jogador_status
    nome = input("Digite o nome da criança:")
    
    while nome.strip() == "":
        nome = input("Digite um nome válido:")
        
    jogador_status = criar_novo_jogo(nome)
    salvar_jogo()
        
    Preludio()
# Menu Inicial
def menu_inicial():
    while True:
        typewriter("Jardim de Cinzas.\n")
        time.sleep(1)
        print("-=--==-=--==-=--==-")
        print("MENU PRINCIPAL")
        print("-=--==-=--==-=--==-\n1 - Iniciar Jogo\n2 - Continuar Jogo\n3 - Créditos\n4 - Sair")
        time.sleep(1)
        menu = input("Digite um dos números acima:\nApoie meu github -->>https://github.com/allanpython2/my-first-game-project-in-python").strip()
        if menu == '1':
            iniciar_novo_jogo()
        elif menu == '2':
            if carregar_jogo():
                if jogador_status['capitulo'] == 1:
                    Preludio()
                elif jogador_status['capitulo'] == 2:
                    capitulo2()
                elif jogador_status['capitulo'] == 3:
                    capitulo3()
                else:
                    input("pressione qualquer coisa para voltar ao menu...")
                    limpar_tela()
        elif menu == '3':
            limpar_tela()
            typewriter("Jardim de Cinzas feito por NENSS (Não, Eu Não Sou um Studio)\nCréditos:\nRoteirista: Allan Duarte\nProgramador: Allan Duarte\nCOLABORADORES: ehh, ninguém mas acho legal colocar isso aqui por enquanto...\nEu, criador do jogo, dedico toda a parte de 'Agradecimentos Especiais' à minha família, que me apoiou desde a criação desse jogo. Sou eternamente grato à minha mãe, meu pai, e meu irmão mais novo.")
            input("pressione qualquer coisa para voltar pro menu principal...")
            limpar_tela()
        elif menu == '4':
            frasess = random.choice(frases)
            print(frasess)
            time.sleep(2)
            sys.exit()
        else:
            print("Erro: digite apenas os números listados!")
# aqui é onde toda a magia vai acontecer:
menu_inicial()

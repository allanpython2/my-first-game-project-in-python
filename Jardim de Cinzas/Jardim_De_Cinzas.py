# bibliotecas pra carregar
import time
import sys
import os
import random
import json
from rich import print
from engine import mostrar_texto, escolher

jogador_status = None

def criar_novo_jogo(nome):
    return {
        "nome": nome,
        "vida": 35,
        "vida_max": 35,
        "ataque": 10,
        "inventario": [],
        "capitulo": 1,
        "tutorial_concluido": False,
        "sanidade": 0
    }

# DIRETÓRIO JOGO
DIRETORIO_JOGO = os.path.dirname(os.path.abspath(__file__))

CAMINHO_SAVE = os.path.join(DIRETORIO_JOGO, "save.json")
# frases pra se o jogador escolher sair do menu
frases = ["Dando o fora...", "Saindo...", "Não vou perder meu tempo nesse jogo..."]

# mensagem secreta rara (um em mil!)
fun = random.randint(1, 1000)
if fun == 1:
    mostrar_texto("odadiuC moC eleuqA euQ alaF moC sa soãM.", atraso=1.0)
    input("...")
    sys.exit()

# limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# carregar jogo no menu em json (eu ODEIO MUITO json)
def carregar_jogo():
    DEBUG = False
    global jogador_status
    try:
        with open(CAMINHO_SAVE, "r") as arquivo:
            jogador_status = json.load(arquivo)
            if DEBUG:
                print(f"DEBUG: Save atual:\n Nome: {jogador_status['nome']} | Capítulo: {jogador_status['capitulo']}")
            print("[bold green][=] Save carregado com sucesso.[/]")
            return True
    except FileNotFoundError:
        mostrar_texto("[italic red][!] Mas ninguém veio. Nenhum save encontrado.[/]")
        return False
# save data em json (eu ODEIO json)
def salvar_jogo():
    with open(CAMINHO_SAVE, "w") as arquivo:
        json.dump(jogador_status, arquivo, indent=4)
    print("[bold yellow][+] Jogo salvo automaticamente.[/]")
    time.sleep(0.5)
# primeira parte da história:
def Preludio():
    limpar_tela()
    mostrar_texto("Jardim de Cinzas.\nCapítulo 1: Tutorial.")
    mostrar_texto(f"[???] {jogador_status['nome']}, acorda!! você vai se atrasar pra escola!!!")
    mostrar_texto("...")
    time.sleep(1)
    mostrar_texto("Quem será que é agora?")
    time.sleep(1)
    mostrar_texto("devagarzinho, você levanta as pálpebras e vê quem é...")
    mostrar_texto("É A SUA MÃE!!!", rapido=True)
    time.sleep(0.4)
    mostrar_texto("[MÃE MUITO IRRITADA] TÁ ESPERANDO O QUÊ? LEVANTA DA CAMA E VAI SE ARRUMAR!")
    time.sleep(0.4)
    mostrar_texto("Você olha o calendário escolar.")
    mostrar_texto("Hoje é domingo.")
    time.sleep(0.4)
    mostrar_texto("Antes que você pudesse dizer algo ou fechar a porta, alguém chega no corredor e interrompe sua mãe...")
    time.sleep(1)
    print("É sua irmã, Isa!")
    time.sleep(1)
    mostrar_texto(f"[Isa] Mãe, hoje não tem aula, é DOMINGO, SETE HORAS DA MANHÃ!! Deixa o {jogador_status['nome']} dormir e depois desce pra tomar café.")
    time.sleep(1)
    mostrar_texto("[Isa] Na verdade, EU estou atrasada, pro curso musical que VOCÊ tinha que me levar, lembra?")
    time.sleep(2)
    print("Bate um silêncio ensurdecedor no quarto. Sua mãe procura as palavras, mas nada saiu da boca dela.")
    time.sleep(2)
    mostrar_texto(f"[Mãe] Na verdade, por que não deixamos o {jogador_status['nome']} decidir se ele quer dormir ou te levar, hein?")
# interaçãa o do jogador

    print("\nO que você quer?")
    opcao = escolher(["Dormir", "Ir com a Isa"])
    match opcao:
        case 1:
            mostrar_texto(f"\n Contra sua vontade, Isa te puxa!")
            time.sleep(1)
            mostrar_texto(f"{jogador_status['nome']}...Tá.")
            mostrar_texto("Sem opções, você se arruma e sai de casa com ela.")
            return Tutorial()
        case 2:
            mostrar_texto("[Isa] Obaa, Vamos logo!")
            time.sleep(0.05)
            return Tutorial()
        case _:
            print("\n[!] Erro! Digite apenas um dos números listados!")
            return "erro"
# preparando o tutorial
def Tutorial():
    limpar_tela()
    salvar_jogo()
    mostrar_texto(f"[Isa] {jogador_status['nome']}, antes de eu ir pro curso, preciso te ensinar a se defender pra quando você voltar pra casa.")
    time.sleep(0.4)
    mostrar_texto("[Isa] Tá vendo aqueles bem-te-vi? Se você passar por eles, eles vão LUTAR com você. Eu sei, é meio estranho lutar com PÁSSAROS, mas é melhor prevenir do que remediar, né?")
    mostrar_texto("[Isa] Vamos lá, lutar com eles! Não se preocupe, se eu ver que você vai CAIR, eu paro a luta e nós voltamos depois!")
    time.sleep(1)
    print("Entrando na luta...")
    time.sleep(1)
    mostrar_texto("[!] Rápido! Um bem-te-vi feroz se aproxima! O que você faz?")
    mostrar_texto(f"[Isa] {jogador_status['nome']}, sempre que você entrar em uma batalha, tente ANALISAR o inimigo, assim, você pode ver quanto de VIDA ele tem! Ah, e antes que eu me esqueça, você tem {jogador_status['vida']} de VIDA!")
    print("Você analisou o inimigo.")
    # status inimigo
    time.sleep(2)
    inimigo_tutorial_vida = 10
    inimigo_tutorial_ataque = 10
    # voltando pra luta
    mostrar_texto(f"[!] Bem-te-vi furioso! {inimigo_tutorial_vida} de VIDA. Apesar do tamanho pequeno, dá {inimigo_tutorial_ataque} de DANO!")
    jogador_status['vida'] -= inimigo_tutorial_ataque
    mostrar_texto(f"[!] Bem-te-vi atacou {jogador_status['nome']}! Agora, {jogador_status['nome']} tem {jogador_status['vida']} de VIDA!")
    mostrar_texto(f"[Isa] Eita, eu esqueci de te avisar, mas ANALISAR um inimigo PULA seu TURNO, e vai pro TURNO DO INIMIGO. É bom saber quando usar! Tente atacar ele de volta!\nAh, e seu ataque padrão dá {jogador_status['ataque']} de dano, mas você pode pegar armas e aumentar seu dano também!")
    inimigo_tutorial_vida -= jogador_status['ataque']
    mostrar_texto(f"[!] Você acertou o bem-te-vi em cheio! A vida do bem-te-vi é: {inimigo_tutorial_vida}")
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
    mostrar_texto(f"[Isa] Tchau {jogador_status['nome']}! Fica bem tá? Olha, como presente, vou te dar essa Faca, tá bom?")
    print("\n[+] Faca foi adicionado ao Inventário, dentro do status do jogador. Você pode abrir o Inventário em Lutas ou no menu principal.") 
    time.sleep(0.4)
    jogador_status['inventario'].append("Faca de Carne")
    print("[!] A Faca não serve apenas para cortar! ao invés de você lutar de mãos vazias, a faca causa 13 de dano!")
    time.sleep(0.4)
    input("Pressione qualquer coisa para mostrar o inventário...")
    print(f"[italic bold]\ninventário: {','.join(jogador_status['inventario'])}\n[/]")
    input("pressione qualquer coisa para sair do inventário...")
    limpar_tela()
    mostrar_texto("[!] Jardim de Cinzas.")
    time.sleep(0.7)
    mostrar_texto("Prólogo: O Pesadelo do Menino.")
    time.sleep(0.7)
    mostrar_texto("Você acorda na sua cama, sem memórias de ter voltado pra casa.")
    mostrar_texto("No espelho ao lado, há um papel colado.")
    opcao = escolher(["Ler o bilhete", "Não ler"])
    if opcao == 1:
        limpar_tela()
        mostrar_texto("No papel, está escrito 'Ser humano', apenas. Você encara o espelho.")
        print("[bold yellow]É você. No fundo, saber que, apesar de tudo, ainda é você...[/]")
        time.sleep(1)
        print("[italic blue]te enche de esperança.[/]")
        time.sleep(2)
    else:
        print("Você ignora.")
    mostrar_texto("A casa está quieta, quase dando pra escutar sua respiração.")
    mostrar_texto("A porta do quarto range quase gritando um aviso de que você saiu. Todas as luzes estão apagadas.")
    mostrar_texto(f"[Isa?] OOOOOOOH {jogador_status['nome']}, abre aqui pra mim por favorzinho? Deixei meu chaveiro cair no esgoto, nojeira!")
    mostrar_texto("Você desce a escada com cuidado, segurando no corrimão. Manchas marrons e um cheiro metálico gruda na sua mão.")
    mostrar_texto("[Isa?] Finalmente! Abre logo aí, tô cansada!")
    mostrar_texto("Tudo está escuro. Você não consegue achar a chave. Droga...")
    mostrar_texto("Se apoiando em cantos vazios pra não cair, você vai até o olho de vidro pra pedir paciência.")
    mostrar_texto("De repente, uma sombra espreita de cima da escada, estranhamente familiar:")
    mostrar_texto(f"{jogador_status['nome']}, teve outro pesadelo de novo? Não abre a porta pra estranhos, você tá doente!")
    print("[bold yellow]É a Isa. Realmente, é a Isa.[/]")
    time.sleep(2)
    mostrar_texto(f"[???] {jogador_status['nome']}, não escuta ela! Abre a porta!")
    mostrar_texto(f"[Isa] Por tudo que é mais sagrado, NÃO ABRE, {jogador_status['nome']}!!!!")
    mostrar_texto("A coisa do outro lado da porta se acalmou.")
    mostrar_texto(f"[O que tá acontecendo?] {jogador_status['nome']}, abre pra sua irmãzinha, vai!!")
    mostrar_texto("[Isa] NÃO!")
    mostrar_texto("Você decide espiar pelo olho de vidro.")
    time.sleep(2)
    limpar_tela()
    mostrar_texto("...", atraso=0.5)
    mostrar_texto("Você vê um vulto incessante se espalhando pelo quintal, como uma sombra.")
    print("[red]Aquilo não é a Isa. Nunca foi.[/red]")
    time.sleep(2)
    mostrar_texto("A voz levemente chiada, como uma gravação antiga.\nO horário atrasado.\nEla sabia que eu desconfiaria...")
    mostrar_texto("O que quer que seja, sabe como eu penso.")
    mostrar_texto("Há quanto tempo esse pesadelo está comigo? Por que COMIGO? Só eu vejo isto? O que vão achar de mim????!!!!")
    time.sleep(0.7)
    limpar_tela()
    mostrar_texto(f"... {jogador_status['nome']} caiu no chão, apavorado.")
    time.sleep(0.5)
    mostrar_texto(f"[Isa] {jogador_status['nome']}, por favor! Não vai agora... Fala comigo! Eiii!!")
    mostrar_texto("Você acorda no quarto, completamente consciente do que aconteceu. Não foi só um sonho ruim.")
    mostrar_texto("[Isa] Ah, céus! Quer me fazer morta também? Você caiu tremendo em frente a porta, dizendo nada com nada!\n[Isa]Já passou, já passou, você tá bem, tá? Está melhor que antes, pelo menos...")
    mostrar_texto("[Isa] eu vou pegar uma água com açúcar pra ver se você se acalma, tá?")
    mostrar_texto("[!] Enquanto o jogador estiver APAVORADO, ele NÃO causará DANO.")
    capitulo3()

# escrevendo o capitulo 3 aqui

def capitulo3():
    global jogador_status
    jogador_status['capitulo'] = 3
    salvar_jogo()
    mostrar_texto("Jardim de Cinzas. Capítulo 1: Negação.\nEm breve!")

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
        mostrar_texto("[italic red]Este jogo não é recomendado para os de coração fraco.[/]")
        time.sleep(2)
        mostrar_texto("[italic red]Compreende?[/]")
        opcao = escolher(["Sim", "Não"])
        if opcao == 2:
            mostrar_texto("[bold red]Lembre-se das consequências.[/]")
            if jogador_status:
                jogador_status['sanidade'] = 0
                salvar_jogo()
            limpar_tela()
        else:
            limpar_tela()
        mostrar_texto("Jardim de Cinzas.\n")
        time.sleep(1)
        print("-=--==-=--==-=--==-")
        print("MENU PRINCIPAL")
        print("-=--==-=--==-=--==-\n1 - Iniciar Jogo\n2 - Continuar Jogo\n3 - Créditos\n4 - Sair")
        time.sleep(1)
        menu = input("apoie meu github -->> https://github.com/allanpython2/my-first-game-project-in-python\nDigite um dos números acima: ").strip()
        
        match menu:
            case '1':
                iniciar_novo_jogo()
            case '2':
                if carregar_jogo():
                    if jogador_status and 'capitulo' in jogador_status:
                        if jogador_status['capitulo'] == 1:
                            res = Preludio()
                        elif jogador_status['capitulo'] == 2:
                            capitulo2()
                        elif jogador_status['capitulo'] == 3:
                            capitulo3()
                    else:
                        mostrar_texto("Erro: save corrompido ou vazio.", rapido=True)
                else:
                    input("Erro interceptado: pressione qualquer coisa para voltar ao menu...")
                    limpar_tela()
                
            case '3':
                limpar_tela()
                mostrar_texto("Um jogo desenvolvido por: ")
                print("[red]Liminal Studios[/red]")
                time.sleep(1)
                mostrar_texto("Jardim de Cinzas.\n\nCréditos:\n\nRoteirista: Allan Oliveira\n\nProgramador: Allan Oliveira\n\nMúsica e Efeitos Sonoros: João Vitor Xavier\n\nEu, criador do jogo - Allan Duarte - dedico toda a parte de 'Agradecimentos Especiais' à minha família, que me apoiou desde a criação desse jogo. Sou eternamente grato à minha mãe, meu pai, e meu irmão mais novo.")
                input("pressione qualquer coisa para voltar pro menu principal...")
                limpar_tela()
            case '4':
                frasess = random.choice(frases)
                print(frasess)
                time.sleep(2)
                sys.exit()
            case _:
                print("Erro: digite apenas os números listados!")
# aqui é onde toda a magia vai acontecer:

menu_inicial()
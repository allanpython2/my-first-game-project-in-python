# bibliotecas pra carregar
import time
import sys
import os
import random
import json
        
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
    global jogador_status
    try:
        with open("save.json", "r") as arquivo:
            jogador_status = json.load(arquivo)
        print("[=] Ainda há esperança! Save carregado com sucesso.")
        time.sleep(0.5)
    except FileNotFoundError:
        print("[!] Mas ninguém veio. Nenhum save encontrado.")
        
# escrevendo o capitulo 2 aqui!!
def capitulo2():
    limpar_tela()
    typewriter("Jardim de Cinzas.\nCapítulo 2: Culpa.")
    typewriter(f"[Isa] Tchau {jogador_status['nome']}! Fica bem tá? Olha, como presente, vou te dar esse Baralho, tá bom?")
    print("\n[+] Baralho foi adicionado ao Inventário, dentro do status do jogador. Você pode abrir o Inventário em Lutas ou no menu principal.") 
    time.sleep(0.4)
    jogador_status['inventário'].append("Baralho")
    print("O baralho de cartas não serve só para jogar! ao invés de você lutar de mãos vazias, o baralho causa 13 de dano!")
    time.sleep(0.4)
    input("Pressione qualquer coisa para mostrar o inventário...")
    print(f"inventário: {jogador_status['inventário']}")
    input("pressione qualquer coisa para sair do inventário...")
    
# Menu Inicial
def menu_inicial():
    while True:            
        typewriter("Bem vindo ao meu jogo: Jardim de Cinzas.\n")
        time.sleep(1)
        print("-=--==-=--==-=--==-")
        print("MENU PRINCIPAL")
        print("-=--==-=--==-=--==-\n1 - Iniciar Jogo\n2 - Continuar Jogo\n3 - Créditos\n4 - Sair")
        time.sleep(1)
        menu = input("Digite um dos números acima:").strip()
        if menu == '1':
            break
        elif menu == '2':
            carregar_jogo()
            nome = jogador_status['nome']
            if jogador_status['capitulo'] == 1:
                Preludio()
            elif jogador_status['capitulo'] == 2:
                capitulo2()
            break
        elif menu == '3':
            typewriter("Jogo feito por NENSS (Não, Eu Não Sou um Studio)\nCréditos:\nRoteirista: Allan Duarte\nProgramador: Allan Duarte\n Eu, criador do jogo, dedico toda a parte de 'Agradecimentos Especiais' à minha família, que me apoiou desde a criação desse jogo. Sou eternamente grato à minha mãe, meu pai, e meu irmão mais novo.")
            input("pressione qualquer coisa para voltar pro menu principal...")
            limpar_tela()
        elif menu == '4':
            frasess = random.choice(frases)
            print(frasess)
            time.sleep(2)
            sys.exit()
        else:
            print("Erro: digite apenas os números listados!")
# executar o menu    
menu_inicial()

# perguntar o nome do jogador.
while True:
    nome = input("Digite o nome da criança.")
    
    if not nome.replace(" ", "").isalpha():
        print("Erro. A criança deve ter um nome e/ou seu nome não pode ter números.")
        continue
    
    if nome.upper() == "SUNNY":
        print("Erro. A criança sente culpa demais pra jogar.")
        time.sleep(1)
        sys.exit()
        
    confirmacao = input(f"O nome da criança é {nome}. Pressione ENTER para confirmar ou Z para digitar outro.").upper()
    if confirmacao == "":
        break
    elif confirmacao == "Z":
        continue
    else:
        print("Erro. Pressione ENTER para confirmar o nome ou Z para escolher outro.")

# sistema de luta
jogador_status = {
    "nome": nome,
    "vida": 35,
    "vida_max": 35,
    "ataque": 10,
    "inventário":[],
    "capitulo": 1,
    "tutorial_concluido": False
}

# save data em json (eu ODEIO json)
def salvar_jogo():
    with open("save.json", "w") as arquivo:
        json.dump(jogador_status, arquivo, indent=4)
    print("[+] Jogo salvo automaticamente.")

# para os engraçadinhos que provavelmente vão mexer no código do status do jogador (vida padrão é 35, eu mexi de propósito)
if jogador_status['vida'] > jogador_status['vida_max'] or jogador_status['vida_max'] > 35.1:
        limpar_tela()
        print("O jogador acorda com mais vida do que antes, repentinamente.")
        input("O jogador quer testar seus novos poderes?[S/N]")
        typewriter("O jogador não tem escolha.", atraso=0.5)
        typewriter("O jogador se beliscou! menos 1 de vida!")
        typewriter("não satisfeito, o jogador dá um soquinho no braço! menos 5 de vida!")
        typewriter("nem doeu! O jogador... Bate a cabeça na parede...")
        typewriter("MENOS 10 DE VIDA!! MAS O JOGADOR AINDA ESTÁ VIVO!")
        typewriter("O jogador desce a escada de casa rolando!! menos 10 de vida!!")
        typewriter("O jogador entra na cozinha.", atraso=0.5)
        typewriter("O jogador vê um arsenal de possíveis machucados na prateleira!")
        typewriter("O jogador encontrou uma faca.", atraso=0.5)
        input("esfaquear?")
        for c in range(1,1000):
            print(f"o jogador recebe {c} de dano!")
            time.sleep(0.005)
        input("foi o suficiente?")
        limpar_tela()
        typewriter("...", atraso=1)
        print("O jogador faleceu.")
        print("O jogador percebeu que é tarde demais pra consertar seus erros.")
        input("Se o jogador sabia das consequências de jogar desonestamente, por que ainda tentou ganhar vantagem?")
        sys.exit()
# preparando o tutorial
def Tutorial():
    limpar_tela()
    salvar_jogo()
    typewriter(f"[Isa] {nome}, antes de eu ir pro curso, preciso te ensinar a se defender pra quando você voltar pra casa.")
    time.sleep(0.4)
    typewriter("[Isa] Tá vendo aqueles bem-te-vi? Se você passar por eles, eles vão LUTAR com você. Eu sei, é meio estranho lutar com PÁSSAROS, mas é melhor prevenir do que remediar, né?")
    typewriter("[Isa] Vamos lá, lutar com eles! Não se preocupe, se eu ver que você vai CAIR, eu paro a luta e nós voltamos depois!")
    time.sleep(1)
    print("Entrando na luta...")
    time.sleep(1)
    typewriter("[!] Rápido! Um bem-te-vi feroz se aproxima! O que você faz?")
    typewriter(f"[Isa] {nome}, sempre que você entrar em uma batalha, tente ANALISAR o inimigo, assim, você pode ver quanto de VIDA ele tem! Ah, e antes que eu me esqueça, você tem {jogador_status['vida']} de VIDA!")
    print("Você analisou o inimigo.")
    # status inimigo
    time.sleep(2)
    inimigo_tutorial_vida = 10
    inimigo_tutorial_ataque = 10
    # voltando pra luta
    typewriter(f"[!] Bem-te-vi furioso! {inimigo_tutorial_vida} de VIDA. Apesar do tamanho pequeno, dá {inimigo_tutorial_ataque} de DANO!")
    jogador_status['vida'] -= inimigo_tutorial_ataque
    typewriter(f"[!] Bem-te-vi atacou {nome}! Agora, {nome} tem {jogador_status['vida']} de VIDA!")
    if jogador_status['vida'] <= 0:
        return "derrota"
    typewriter(f"[Isa] Eita, eu esqueci de te avisar, mas ANALISAR um inimigo PULA seu TURNO, e vai pro TURNO DO INIMIGO. É bom saber quando usar! Tente atacar ele de volta!\nAh, e seu ataque padrão dá {jogador_status['ataque']} de dano, mas você pode pegar armas e aumentar seu dano também!")
    inimigo_tutorial_vida -= jogador_status['ataque']
    typewriter(f"[!] Você acertou o bem-te-vi em cheio! A vida do bem-te-vi é: {inimigo_tutorial_vida}")
    # condicao de vitoria
    if inimigo_tutorial_vida <= 0:
        print(f"[Isa] Obaaa! {nome}, você matou o bem-te-vi!")
        jogador_status["tutorial_concluido"] = True
        jogador_status["capitulo"] = 2
        salvar_jogo()
        return "vitoria"
    else:
        return "derrota"
# primeira parte da história:
limpar_tela()
typewriter("Jardim de Cinzas.\nCapítulo 1: Tutorial.")
typewriter(f"[???] {nome}, acorda!! você vai se atrasar pra escola!!!")
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
typewriter(f"[Isa] Mãe, hoje não tem aula, é DOMINGO, SETE HORAS DA MANHÃ!! Deixa o {nome} dormir e depois desce pra tomar café.")
time.sleep(1)
typewriter("[Isa] Na verdade, EU estou atrasada, pro curso musical que VOCÊ tinha que me levar, lembra?")
time.sleep(2)
print("Bate um silêncio ensurdecedor no quarto. Sua mãe procura as palavras, mas nada saiu da boca dela.")
time.sleep(2)
typewriter(f"[Mãe] Na verdade, por que não deixamos o {nome} decidir se ele quer dormir ou te levar, hein?")
# interação do jogador

def Preludio():
    print("\nO que você quer?")
    acao_jogador = input("\n[1] Dormir\n[2] Ir com a Isa")
    if acao_jogador == "1":
        typewriter(f"\n[Isa] Poxa, {nome}, vamos logo!")
        time.sleep(1)
        typewriter(f"[{nome}]...Tá.")
        typewriter("Sem opções, você se arruma e sai de casa com ela.")
        return Tutorial()
    elif acao_jogador == "2":
        typewriter("[Isa] Obaa, Vamos logo!")
        return Tutorial()
    else:
        print("\n[!] Erro! Digite apenas um dos números listados!")
        return "erro"
while True:
    resultado = Preludio()
    
    if resultado == "vitoria":
        typewriter("[+] Você passou pro próximo capítulo...")
        break
    elif resultado == "derrota":
        print("-=--=- VOCÊ CAIU! -=--=-")
        game_over()
    else:
        pass
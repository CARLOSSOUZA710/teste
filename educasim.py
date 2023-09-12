import getpass
import random

credenciais = {
    'email': None,
    'senha': None,
    'nome': None,
    'idade': None,
    'ano': None,
    'genero': None
}

numero_aleatorio = random.randint(1 , 100)
numero_aleatorio2 = random.randint(1, 100)
numero_aleatorio3 = random.randint(1, 100)
numero_aleatorio4 = random.randint(1, 100)
numero_aleatorio5 = random.randint(1, 100)
numero_aleatorio6 = random.randint(1, 100)
numero_aleatorio7 = random.randint(100, 1000)
numero_aleatorio8 = random.randint(1000, 10000)

temareda = ('Aquecimento Globla', 'A importancia da ONU nos dias de hoje', 'Sistema Carcerario', 'Violencia Contra a Mulher')
temareda_aleatorio = random.choice(temareda)

def exer1ing1 ():
        print('Exercício 1:')
        print('My brother _______________ (is/am/are) a doctor.')
        print('a) is')
        print('b) am')
        print('c) are')
        resposta_exercicio1 = input('Escolha a opção correta (a, b, ou c): ')
        if resposta_exercicio1.lower() == 'a':
            print('Correto! "My brother is a doctor." (Meu irmão é um médico).')
        else:
            print('Ops, resposta incorreta. A resposta correta é "a) is".')
        
        print('Exercício 2:')
        print('Choose the correct translation for the following sentence:')
        print('"Ela está estudando agora."')
        print('a) She is studying now.')
        print('b) She studies yesterday.')
        print('c) She studied tomorrow.')
        resposta_exercicio2 = input('Escolha a opção correta (a, b, ou c): ')
        if resposta_exercicio2.lower() == 'a':
            print('Ótimo! Você escolheu a tradução correta. "She is studying now." (Ela está estudando agora).')
        else:
            print('Que pena, resposta incorreta. A resposta correta é "a) She is studying now.".')
           
        print('Exercício 3:')
        print('Choose the correct word to complete the sentence:')
        print('"I have a pet _______________ (cat/dog/elephant)."')
        print('a) cat')
        print('b) dog')
        print('c) elephant')
        resposta_exercicio3 = input('Escolha a opção correta (a, b, ou c): ')
        if resposta_exercicio3.lower() == 'a':
            print('Excelente! Você escolheu a palavra correta. "I have a pet cat." (Eu tenho um gato de estimação).')
        else:
            print('Ops, resposta incorreta. A resposta correta é "a) cat."')
def exer1soma1 ():
    
        exercicio_soma = int(input(f"Quanto é {numero_aleatorio} + {numero_aleatorio2}? "))
        resultado = numero_aleatorio + numero_aleatorio2
        if exercicio_soma == resultado:
            print('parabens voce acertou. Bora pro proximo')
        else:
            print('que pena voce errou')
        
        exercicio_soma1 = int(input(f"Quanto é {numero_aleatorio3} + {numero_aleatorio4}? "))
        resultado = numero_aleatorio3 + numero_aleatorio4
        if exercicio_soma == resultado:
            print('parabens voce acertou. Bora pro proximo')
        else:
            print('que pena voce errou')
            
        exercicio_soma2 = int(input(f"Quanto é {numero_aleatorio5} + {numero_aleatorio6}? "))
        resultado = numero_aleatorio5 + numero_aleatorio6
        if exercicio_soma == resultado:
            print('parabens voce acertou. Bora pro proximo')
        else:
            print('que pena voce errou')
        
        exercicio_soma3 = int(input(f"Quanto é {numero_aleatorio7} + {numero_aleatorio8}? "))
        resultado = numero_aleatorio7 + numero_aleatorio8
        if exercicio_soma == resultado:
            print('parabens voce acertou. Bora pro proximo')
        else:
            print('que pena voce errou')      
def exer1sub1 ():
    
        exercicio_menos = int(input(f"Quanto é {numero_aleatorio} - {numero_aleatorio2}? "))
        resultado = numero_aleatorio - numero_aleatorio2
        if resultado == resultado:
            print('parabens voce acertou. Bora pro proximo')
        else:
            print('que pena voce errou')
        
        exercicio_menos2 = int(input(f"Quanto é {numero_aleatorio3} - {numero_aleatorio4}? "))
        resultado = numero_aleatorio3 - numero_aleatorio4
        if resultado == resultado:
            print('parabens voce acertou. Bora pro proximo')
        else:
            print('que pena voce errou')
        
        exercicio_menos3 = int(input(f"Quanto é {numero_aleatorio5} - {numero_aleatorio6}? "))
        resultado = numero_aleatorio5 - numero_aleatorio6
        if resultado == resultado:
            print('parabens voce acertou. Bora pro proximo')
        else:
            print('que pena voce errou, vamos tentar de novo')
def exer1hist1 ():
    
        print('ok vamos praticar historia')
        print('Exercício 21:')
        print('Em que ano o Brasil foi oficialmente descoberto pelos portugueses?')
        print('a) 1492')
        print('b) 1500')
        print('c) 1776')
        resposta_exercicio21 = input('Escolha a opção correta (a, b, ou c): ')
        if resposta_exercicio21.lower() == 'b':
            print('Correto! O Brasil foi oficialmente descoberto pelos portugueses em 1500.')
        else:
            print('Ops, resposta incorreta. A resposta correta é "b) 1500".')
            
        print('Exercício 22:')
        print('Qual evento histórico ocorreu em 1789 na França e teve um papel importante na história mundial?')
        print('a) Guerra Civil Americana')
        print('b) Revolução Francesa')
        print('c) Revolução Industrial')
        resposta_exercicio22 = input('Escolha a opção correta (a, b, ou c): ')
        if resposta_exercicio22.lower() == 'b':
            print('Ótimo! Você escolheu a opção correta. A Revolução Francesa começou em 1789.')
        else:
            print('Que pena, resposta incorreta. A resposta correta é "b) Revolução Francesa".')
        
        print('Exercício 23:')
        print('Qual foi o período de tensão política e militar entre os Estados Unidos e a União Soviética após a Segunda Guerra Mundial?')
        print('a) Primeira Guerra Mundial')
        print('b) Guerra Fria')
        print('c) Segunda Guerra Mundial')
        resposta_exercicio23 = input('Escolha a opção correta (a, b, ou c): ')
        if resposta_exercicio23.lower() == 'b':
            print('Excelente! Você escolheu a resposta correta. A Guerra Fria foi o período de tensão após a Segunda Guerra Mundial.')
        else:
            print('Ops, resposta incorreta. A resposta correta é "b) Guerra Fria".')
           
        print('Exercício 24:')
        print('Qual foi o nome do imperador romano famoso por construir um muro na fronteira norte do Império Romano, na Grã-Bretanha?')
        print('a) Nero')
        print('b) Augusto')
        print('c) Adriano')
        resposta_exercicio24 = input('Escolha a opção correta (a, b, ou c): ')
        if resposta_exercicio24.lower() == 'c':
            print('Ótimo! Você escolheu a resposta correta. O imperador Adriano construiu o Muro de Adriano na Grã-Bretanha.')
        else:
            print('Ops, resposta incorreta. A resposta correta é "c) Adriano".')
                      
        print('Exercício 25:')
        print('Em que ano o Brasil conquistou sua independência de Portugal?')
        print('a) 1808')
        print('b) 1822')
        print('c) 1889')
        resposta_exercicio25 = input('Escolha a opção correta (a, b, ou c): ')
        if resposta_exercicio25.lower() == 'b':
            print('Excelente! Você acertou. O Brasil conquistou sua independência em 1822.')
        else:
            print('Ops, resposta incorreta. A resposta correta é "b) 1822".')
def exer2geo2 ():
    
        print('Exercício 1:')
        print('Qual é o país mais populoso do mundo?')
        print('a) Índia')
        print('b) China')
        print('c) Estados Unidos')
        resposta_exercicio1 = input('Escolha a opção correta (a, b, ou c): ')

        if resposta_exercicio1.lower() == 'b':
            print('Resposta correta! A China é o país mais populoso do mundo.')
        else:
            print('Resposta incorreta. A China é o país mais populoso do mundo.')

        
        print('Exercício 2:')
        print('Qual é a maior cordilheira do mundo?')
        print('a) Montanhas Rochosas')
        print('b) Cordilheira dos Andes')
        print('c) Montanhas do Himalaia')
        resposta_exercicio2 = input('Escolha a opção correta (a, b, ou c): ')

        if resposta_exercicio2.lower() == 'b':
            print('Resposta correta! A Cordilheira dos Andes é a maior cordilheira do mundo.')
        else:
            print('Resposta incorreta. A Cordilheira dos Andes é a maior cordilheira do mundo.')

        
        print('Exercício 3:')
        print('Qual é o maior deserto do mundo?')
        print('a) Deserto de Atacama')
        print('b) Deserto do Saara')
        print('c) Deserto de Gobi')
        resposta_exercicio3 = input('Escolha a opção correta (a, b, ou c): ')

        if resposta_exercicio3.lower() == 'b':
            print('Resposta correta! O Deserto do Saara é o maior deserto do mundo.')
        else:
            print('Resposta incorreta. O Deserto do Saara é o maior deserto do mundo.')

        
        print('Exercício 4:')
        print('Qual é a capital do Japão?')
        print('a) Kyoto')
        print('b) Tóquio')
        print('c) Osaka')
        resposta_exercicio4 = input('Escolha a opção correta (a, b, ou c): ')

        if resposta_exercicio4.lower() == 'b':
            print('Resposta correta! Tóquio é a capital do Japão.')
        else:
            print('Resposta incorreta. Tóquio é a capital do Japão.')

        
        print('Exercício 5:')
        print('Qual é o ponto mais alto da Terra, conhecido como o "teto do mundo"?')
        print('a) Montanha do Kilimanjaro')
        print('b) Monte McKinley')
        print('c) Monte Everest')
        resposta_exercicio5 = input('Escolha a opção correta (a, b, ou c): ')

        if resposta_exercicio5.lower() == 'c':
            print('Resposta correta! O Monte Everest é o ponto mais alto da Terra.')
        else:
            print('Resposta incorreta. O Monte Everest é o ponto mais alto da Terra.')
def exer2astr2 ():
    
        print('Exercício 1:')
        print('Qual é o signo do zodíaco que é representado pelo "Carneiro"?')
        print('a) Touro')
        print('b) Áries')
        print('c) Gêmeos')
        resposta_exercicio1 = input('Escolha a opção correta (a, b, ou c): ')

        if resposta_exercicio1.lower() == 'b':
            print('Resposta correta! Áries é o signo representado pelo "Carneiro".')
        else:
            print('Resposta incorreta. Áries é o signo representado pelo "Carneiro".')
        
        print('Exercício 2:')
        print('Qual é o planeta regente do signo de Peixes?')
        print('a) Vênus')
        print('b) Marte')
        print('c) Netuno')
        resposta_exercicio2 = input('Escolha a opção correta (a, b, ou c): ')

        if resposta_exercicio2.lower() == 'c':
            print('Resposta correta! Netuno é o planeta regente do signo de Peixes.')
        else:
            print('Resposta incorreta. Netuno é o planeta regente do signo de Peixes.')

        print('Exercício 3:')
        print('Quantos signos do zodíaco existem no total?')
        print('a) 10')
        print('b) 12')
        print('c) 8')
        resposta_exercicio3 = input('Escolha a opção correta (a, b, ou c): ')

        if resposta_exercicio3.lower() == 'b':
            print('Resposta correta! Existem 12 signos do zodíaco no total.')
        else:
            print('Resposta incorreta. Existem 12 signos do zodíaco no total.')

        print('Exercício 4:')
        print('Qual é o elemento associado ao signo de Leão?')
        print('a) Água')
        print('b) Fogo')
        print('c) Terra')
        resposta_exercicio4 = input('Escolha a opção correta (a, b, ou c): ')

        if resposta_exercicio4.lower() == 'b':
            print('Resposta correta! O signo de Leão é associado ao elemento Fogo.')
        else:
            print('Resposta incorreta. O signo de Leão é associado ao elemento Fogo.')

        print('Exercício 5:')
        print('Qual é o signo do zodíaco que é representado pela balança?')
        print('a) Libra')
        print('b) Virgem')
        print('c) Escorpião')
        resposta_exercicio5 = input('Escolha a opção correta (a, b, ou c): ')

        if resposta_exercicio5.lower() == 'a':
            print('Resposta correta! Libra é o signo representado pela balança.')
        else:
            print('Resposta incorreta. Libra é o signo representado pela balança.')
def exer2msc2 ():
    
        print('Ok, vamos estudar Musica!!!')
        print('Exercício 1:')
        print('Qual é o instrumento musical conhecido como "rei dos instrumentos"?')
        print('a) Guitarra')
        print('b) Violino')
        print('c) Órgão')
        resposta_exercicio1 = input('Escolha a opção correta (a, b, ou c): ')

        if resposta_exercicio1.lower() == 'c':
            print('Resposta correta! O órgão é conhecido como o "rei dos instrumentos".')
        else:
            print('Resposta incorreta. O órgão é conhecido como o "rei dos instrumentos".')

        print('Exercício 2:')
        print('Qual é o nome da técnica vocal que envolve a produção de dois tons simultaneamente?')
        print('a) Falsetto')
        print('b) Vibrato')
        print('c) Canto gutural')
        resposta_exercicio2 = input('Escolha a opção correta (a, b, ou c): ')

        if resposta_exercicio2.lower() == 'a':
            print('Resposta correta! Falsetto envolve a produção de dois tons simultaneamente.')
        else:
            print('Resposta incorreta. Falsetto envolve a produção de dois tons simultaneamente.')

        print('Exercício 3:')
        print('Qual é o nome da notação musical que representa um silêncio completo?')
        print('a) Semibreve')
        print('b) Pausa de semibreve')
        print('c) Pausa de mínima')
        resposta_exercicio3 = input('Escolha a opção correta (a, b, ou c): ')

        if resposta_exercicio3.lower() == 'b':
            print('Resposta correta! A pausa de semibreve representa um silêncio completo.')
        else:
            print('Resposta incorreta. A pausa de semibreve representa um silêncio completo.')
        
        print('Exercício 4:')
        print('Qual é o nome do gênero musical caracterizado por seu ritmo rápido, improvisação e influência afro-cubana?')
        print('a) Samba')
        print('b) Jazz')
        print('c) Reggae')
        resposta_exercicio4 = input('Escolha a opção correta (a, b, ou c): ')

        if resposta_exercicio4.lower() == 'b':
            print('Resposta correta! O jazz é caracterizado por seu ritmo rápido, improvisação e influência afro-cubana.')
        else:
            print('Resposta incorreta. O jazz é caracterizado por seu ritmo rápido, improvisação e influência afro-cubana.')

        print('Exercício 5:')
        print('Qual é o nome da técnica de produção musical que envolve a gravação de diferentes partes da música separadamente e, em seguida, combinando-as em uma mixagem final?')
        print('a) Looping')
        print('b) Sampling')
        print('c) Multitrack recording')
        resposta_exercicio5 = input('Escolha a opção correta (a, b, ou c): ')

        if resposta_exercicio5.lower() == 'c':
            print('Resposta correta! A gravação multitrack envolve a gravação separada de diferentes partes da música.')
        else:
            print('Resposta incorreta. A gravação multitrack envolve a gravação separada de diferentes partes da música.')

#Exercicios Terceirão
def exercicioredaçao ():
    print (f'Escreva um texto com o tema: {temareda_aleatorio}')
    resposta = input()
    linhas = resposta.splitlines
    numero_linhas = len(linhas)
    if numero_linhas >= 15:
        print('Parabens voce tirou 10!🎂🎉✨🎁')
    elif numero_linhas > 7:
        print ('Nada mal. NOta 7')
    elif numero_linhas <= 5:
        print('Sei que voce consegue melhorar ainda😉')
def exercicocg ():
    print('Exercício de Conhecimentos Gerais:')
    print('Exercico 1')
    print('What is the capital of France?')
    print('a) Paris')
    print('b) London')
    print('c) Berlin')
    resposta_exercicio = input('Escolha a opção correta (a, b, ou c): ')
    if resposta_exercicio.lower() == 'a':
        print('Correto! Paris is the capital of France. (Paris é a capital da França).')
    else:
        print('Ops, resposta incorreta. A resposta correta é "a) Paris".')

    print('Exercicio 2')
    print('What is the largest planet in our solar system?')
    print('a) Earth')
    print('b) Jupiter')
    print('c) Mars')
    resposta_exercicio = input('Escolha a opção correta (a, b, ou c): ')
    if resposta_exercicio.lower() == 'b':
        print('Correto! Jupiter is the largest planet in our solar system. (Júpiter é o maior planeta do nosso sistema solar).')
    else:
        print('Ops, resposta incorreta. A resposta correta é "b) Jupiter".')
    
    print('Exercício 3')
    print('Which gas do plants absorb from the atmosphere during photosynthesis?')
    print('a) Oxygen')
    print('b) Nitrogen')
    print('c) Carbon dioxide')
    resposta_exercicio = input('Escolha a opção correta (a, b, ou c): ')
    if resposta_exercicio.lower() == 'c':
        print('Ótimo! Plants absorb carbon dioxide from the atmosphere during photosynthesis. (As plantas absorvem dióxido de carbono da atmosfera durante a fotossíntese).')
    else:
        print('Que pena, resposta incorreta. A resposta correta é "c) Carbon dioxide".')

    print('Exercício 4')
    print('Who wrote the famous play "Romeo and Juliet"?')
    print('a) William Shakespeare')
    print('b) Charles Dickens')
    print('c) Jane Austen')
    resposta_exercicio = input('Escolha a opção correta (a, b, ou c): ')
    if resposta_exercicio.lower() == 'a':
        print('Correto! William Shakespeare wrote the famous play "Romeo and Juliet." (William Shakespeare escreveu a famosa peça "Romeu e Julieta").')
    else:
        print('Ops, resposta incorreta. A resposta correta é "a) William Shakespeare".')

    print('Exercício 5')
    print('What is the chemical symbol for gold?')
    print('a) Go')
    print('b) Au')
    print('c) Ag')
    resposta_exercicio = input('Escolha a opção correta (a, b, ou c): ')
    if resposta_exercicio.lower() == 'b':
        print('Excelente! The chemical symbol for gold is "Au." (O símbolo químico do ouro é "Au").')
    else:
        print('Ops, resposta incorreta. A resposta correta é "b) Au".')
def exercicioleg():
    print('Exercício de Legislação:')
    print('Exercicio 1')
    print('What is the highest court in the United States?')
    print('a) Supreme Court')
    print('b) Federal Court')
    print('c) District Court')
    resposta_exercicio = input('Escolha a opção correta (a, b, ou c): ')
    if resposta_exercicio.lower() == 'a':
        print('Ótimo! The Supreme Court is the highest court in the United States. (A Suprema Corte é o tribunal mais alto nos Estados Unidos).')
    else:
        print('Que pena, resposta incorreta. A resposta correta é "a) Supreme Court".')

    print('Exercício 2')
    print('What is the highest court in the United Kingdom?')
    print('a) Supreme Court')
    print('b) High Court')
    print('c) Court of Appeal')
    resposta_exercicio = input('Escolha a opção correta (a, b, ou c): ')
    if resposta_exercicio.lower() == 'a':
        print('Correto! The Supreme Court is the highest court in the United Kingdom. (A Suprema Corte é o tribunal mais alto no Reino Unido).')
    else:
        print('Ops, resposta incorreta. A resposta correta é "a) Supreme Court".')

    print('Exercício 3')
    print('Which document outlines the fundamental rights and freedoms of citizens in the United States?')
    print('a) Bill of Rights')
    print('b) Declaration of Independence')
    print('c) Constitution')
    resposta_exercicio = input('Escolha a opção correta (a, b, ou c): ')
    if resposta_exercicio.lower() == 'a':
        print('Ótimo! The Bill of Rights outlines the fundamental rights and freedoms of citizens in the United States. (A Declaração de Direitos estabelece os direitos fundamentais e liberdades dos cidadãos nos Estados Unidos).')
    else:
        print('Que pena, resposta incorreta. A resposta correta é "a) Bill of Rights".')

    print('Exercício 4')
    print('What is the highest court in Australia?')
    print('a) Supreme Court of Australia')
    print('b) High Court of Australia')
    print('c) Federal Court of Australia')
    resposta_exercicio = input('Escolha a opção correta (a, b, ou c): ')
    if resposta_exercicio.lower() == 'b':
        print('Correto! The High Court of Australia is the highest court in Australia. (O Tribunal Superior da Austrália é o tribunal mais alto na Austrália).')
    else:
        print('Ops, resposta incorreta. A resposta correta é "b) High Court of Australia".')

    print('Exercício 5')
    print('In which year did the United Nations officially come into existence?')
    print('a) 1945')
    print('b) 1950')
    print('c) 1930')
    resposta_exercicio = input('Escolha a opção correta (a, b, ou c): ')
    if resposta_exercicio.lower() == 'a':
        print('Excelente! The United Nations officially came into existence in 1945. (As Nações Unidas foram oficialmente estabelecidas em 1945).')
    else:
        print('Ops, resposta incorreta. A resposta correta é "a) 1945".')

cadastro_concluido = False


def cadastro():
    email = input('Cadastre seu email: ')
    senha = input('Cadastre sua senha: ')
    print('Que legal te ver por aqui!! Vamos continuar seu cadastro.')
    nome = input('Qual seu nome: ')
    print('Estamos quase lá.')
    idade = int(input(f'Qual sua idade, {nome}? '))
    print('Como você se identifica?')
    print('a) Masculino')
    print('b) Feminino')
    print('c) Outro')
    while True:
        genero = input('a, b ou c? ')
        if genero not in ('a', 'b', 'c'):
            print('Opção inválida. Tente de novo!')
        else:
            break
    print('Em qual ano do ensino médio você está?')
    print('a) Primeiro')
    print('b) Segundo')
    print('c) Terceirão')
    ano = input('a, b ou c? ')
    if ano not in ('a', 'b', 'c'):
            print('Opção inválida. Tente de novo!')
            ano = input('a, b ou c? ')
    else:
            print(f'OK. Cadastro concluído, {nome}!')
            credenciais['email'] = email
            credenciais['senha'] = senha
            credenciais['nome'] = nome
            credenciais['idade'] = idade
            credenciais['genero'] = genero
            credenciais['ano'] = ano
            return email, senha, nome, idade, genero, ano


def fazer_login():
    tentativas = 3
    while tentativas > 0:
        loginemail = input('Digite seu email: ')
        loginsenha = getpass.getpass('Digite sua senha: ')

        if (
            loginemail == credenciais['email']
            and loginsenha == credenciais['senha']
        ):
            print(f'Olá, você está logado como {credenciais["email"]}')
            return True
        else:
            print('Credenciais inválidas. Tente novamente.')
            tentativas -= 1

    print('Você excedeu o número máximo de tentativas. Saindo...')
    return False


while not cadastro_concluido:
    cadastro_info = cadastro()
    if cadastro():
        cadastro_concluido = True
        email, senha, nome, idade, genero, ano = cadastro_info
    else:
        print('Falha ao cadastrar. Tente novamente.')

if fazer_login():
    print('Vamos começar a estudar!')      
        
    if ano.lower() == 'a':
        while True:
            print('Escolha a materia que deseja estudar!')
            print('Ingles/Matematica/Historia')
            materia = input()
            
            if materia.lower() == 'ingles':
                exer1ing1()
            
            elif materia.lower() == 'matematica':
                exer1soma1()
                exer1sub1()

            elif materia.lower() == 'historia':
                exer1hist1()

            print("Deseja escolher outra matéria? (S para sim, qualquer outra tecla para sair)")
            continuar = input()
            if continuar.lower() != 's':
                break
    
    elif ano.lower() == 'b':
        while True:
            print('Escolha a materia que deseja estudar!')
            print('Geografia/Astrologia/Musica')
            materia = input()
            
            if materia.lower() == 'geografia':
                exer2geo2()
            
            elif materia.lower() == 'astrologia':
                exer2astr2()

            elif materia.lower() == 'musica':
                exer2msc2()

            print("Deseja escolher outra matéria? (S para sim, qualquer outra tecla para sair)")
            continuar = input()
            if continuar.lower() != 's':
                break
    elif ano.lower == 'c':
        while True:
            print('Terceirão ja em?! Como passou rapido.')
            print('Esta na hora de começar a se preparar para o vestibular!')
            print('Sobre oque vamos estudar hoje? ')
            print('a) Conhecimentos gerais')
            print('b) Legislaçao')
            print('c) Redação')
            materia =  input()

            if materia.lower() == 'a':
                exercicocg()
            
            elif materia.lower() == 'b':
                exercicioleg()

            elif materia.lower() == 'c':
                exercicioredaçao()

            else:
                print('Opção invalida')

            print("Deseja escolher outra matéria? (S para sim, qualquer outra tecla para sair)")
            continuar = input()
            if continuar.lower() != 's':
                break     

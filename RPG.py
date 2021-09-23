import keyboard
import time
import random
from bullshit import cria_bullshit, traduz_bullshit

# PROSSEGUIR COM A HISTÓRIA
# FAZER SISTEMA DE DUNGEONS COMECAR FLORESTA
# DESCREVER PERIFERIA E BEBIDAS
# INCLUIR CRIANÇAS E BRUTAMONTES E ETC
# MOEDAS OURO/PRATA/BRONZE
# FAZER STATS E ATAQUES
# FAZER LUTAS E INIMIGOS
# COLOCAR VERIFICAÇÃO DE ERROS PROS INPUTS DE AVANÇAR/SALVAR/STATS

class Player:
    def __init__(self, classe, nome):
        self.classe = classe # classe do jogador
        self.level = 1
        self.nome = nome   # nome do jogador
        self.xp = 0        # relativo à experiência do jogador
        self.itens = []    # itens sob posse do jogador
        self.grana = 10    # dinheiro do jogador
        self.fase = 0      # fase do jogo em que o jogador se encontra
        # VARIAVEIS DOS SONHOS/SECUNDARIA
        self.solidao = False
        self.win = False
        
    def ataque(self, inimigo):
        # ataque básico e primário
        print(f"{self.nome} atacou {inimigo.nome}")
        inimigo.hp -= int(self.forca * 2  - inimigo.dure)
        if inimigo.hp >= 0:
            inimigo.hp = 0

    def upar(self):
        xp_preciso = 3*(self.level**3)//4
        if self.xp >= xp_preciso:
            self.level += 1
            self.xp -= xp_preciso
            print(f"{self.nome} upou para o nível {self.level}")

    def imprime_stats(self):
        print(f'\nNome: {self.nome}')
        print(f'Classe: {self.classe}')
        print(f'Level: {self.level}')
        print(f'Experiência: {self.xp}')
        print(f'Religião: {self.religiao}')
        print(f'Divindade: {self.deus}')
        print(f'HP: {self.hp}')
        print(f'Força: {self.forca}')
        print(f'Dureza: {self.dure}')
        print(f'Inteligência: {self.inte}')
        print(f'Persistência: {self.persi}')
        print(f'Loucura: {self.louc}')
        input("\nAperte ENTER para sair")

    def sonhar(self):
        sonho_prob = random.randint(1, 4)
        if sonho_prob == 1:
            input(f"Você é um {P1.classe} que acaba de chegar em uma terra estrangeira.")
            input("As pessoas e as casas são diferentes e você se sente um pouco deslocado.")
            print("\nVilarejo")
            print("[121] Taverna")
            print("[122] Explorar")
            print("[123] Estalagem")
            print("[124] Stats")
            escolha_vila = int(input("\nEscolha o que deseja fazer: "))
            if escolha_vila == 124:
                self.imprime_stats()
            else:
                input("Você caminha até seu destino, mas de repente encontra um cara mais estrangeiro dos que os estrangeiros do vilarejo, ele parecia vir de muito")
                input("longe. O sujeito se aproxima de você, é um cara alto e forte, vestido em trapos que de alguma forma lhe parce familiar.")
                input("Estrangeiro: Você viu um anjo por aí?")
                self.resposta = input("Responda o rapaz: ")
                input("O estrangeiro subitamente desaparece.")
                input("Você acorda.")
        elif sonho_prob == 2:
            if self.solidao:
                input("Após longos anos de solidão, você está novamente diante da porta daquele ama.")
            else:
                input("Você está diante da porta daquele ama.")
            print("\n[1]Bater")
            print("[2]Ir embora")
            escolha_porta_ama = int(input("O que deseja fazer? "))
            if escolha_porta_ama == 1:
                input("???: Quem bate?")
                print("[1]Sou eu")
                print("[2]É você")
                escolha_fala_ama = int(input("\nEscolha o que dizer: "))
                if escolha_fala_ama == 1:
                    input("\n???: Não há espaço aqui para mim e você.")
                    input("A porta se fecha.")
                    self.solidao = True
                    input("Você acorda.")
                elif escolha_fala_ama == 2:
                    input("A porta se abre.")
                    input("Você acorda.")
            if escolha_porta_ama == 2:
                input("Você se afasta da porta com um peso em seu coração.")
                input("Você acorda.")
        elif sonho_prob == 3:
            input("É noite e você caminha por um enorme deserto. Você não avista nada no horizonte além de mais areia.")
            input("Você sente frio.")
            caminhada_deserto = True
            while caminhada_deserto:
                print("\n[1]Andar")
                input("\nEscolha o que vai fazer: ")
                input("Você continua andando...")
                anjo_prob = random.randint(1, 3)
                if anjo_prob == 2:
                    caminhada_deserto = False
                    input("De repente, uma figura angelical desce dos céus e para ao seu lado. Gentilmente, ele o envolve em suas asas calorosas.")
                    input("Você não sente mais frio.")
                    input("Você acorda.")
            
            
class Berserker(Player):
    def __init__(self, classe, nome):
        super().__init__(classe, nome)
        self.hp = random.randint(30, 35)     # relativo à saúde do jogador
        self.inte = random.randint(5, 7)     # relativo à inteligência do jogador
        self.persi = random.randint(10, 13)    # relativo à persistência do jogador
        self.forca = random.randint(10, 15)  # relativo à força bruta do jogador
        self.dure = random.randint(8, 12)    # relativo à resistência, dureza do jogador
        self.louc = random.randint(10, 15)   # inversamente relativo à sanidade do jogador
        self.velo = random.randint(5, 7)   # relativo à agilidade do jogador
        self.religiao = 'Ateu'
        self.deus = 'Nenhum'
        Traje1 = Equipavel(1, 'Manta Trácia', 'Uma manta tradicional do continente trácio. Fora entregue a você pelo seu pai, quando partiu de sua terra natal. Ele disse que faz bastante frio longe de lá.', None, True)
        Espada1 = Equipavel(2, 'Sabre Trácio', 'Um clássico sabre trácio, curvo e afiado em apenas um lado.', None, True)
        self.itens = [Traje1, Espada1]
        
    def carnificina(self, inimigo):
        # ataque sangrento e brutal realizado pelo berserker
        print(f"{self.nome} trucidou {inimigo.nome}")
        inimigo.hp -= int(self.forca + self.louc  - inimigo.dure)

        
class Paladino(Player):
    def __init__(self, classe, nome):
        super().__init__(classe, nome)
        crencas = ['Nanismo', 'Mouro', 'Sheenaismo', 'Magnólio', 'Local']
        deuses = [['Yahel Salvador', 'Nosso Lorde', 'São Azhel'], ['Nosso Lorde'], ['Krishna', 'Shiva'], ['Kari', 'Kibroth Hattavah', 'Guru Gok'], ['Forseti', 'Bodão', 'Bahamut', 'Avandra']]
        self.hp = random.randint(30, 40)     # relativo à saúde do jogador
        self.inte = random.randint(10, 12)     # relativo à inteligência do jogador
        self.persi = random.randint(8, 10)  # relativo à persistência do jogador
        self.forca = random.randint(5, 10)  # relativo à força bruta do jogador
        self.dure = random.randint(5, 10)    # relativo à resistência, dureza do jogador
        self.louc = random.randint(0, 10)   # inversamente relativo à sanidade do jogador
        self.velo = random.randint(5, 10)   # relativo à agilidade do jogador
        selecao = random.randint(0, 4)
        self.religiao = crencas[selecao]
        self.deus = random.choice(deuses[selecao])
        Traje1 = Equipavel(1, 'Manta Trácia', 'Uma manta tradicional do continente trácio. Fora entregue a você pelo seu pai, quando partiu de sua terra natal. Ele disse que faz bastante frio longe de casa.', None, True)
        Espada1 = Equipavel(2, 'Sabre Trácio', 'Um clássico sabre trácio, curvo e afiado em apenas um lado.', None, True)
        self.itens = [Traje1, Espada1]

    def orar(self):
        print(f"{self.nome} rezou para {self.deus}")

class Cowboy(Player):
    def __init__(self, classe, nome):
        super().__init__(classe, nome)
        crencas = ['Ateu', 'Magnólio']
        deuses = ['Nenhum', 'Yosep']
        selecao = random.randint(0, 1)
        self.religiao = crencas[selecao]
        self.deus = deuses[selecao]
        self.hp = random.randint(25, 30)     # relativo à saúde do jogador
        self.inte = random.randint(8, 10)     # relativo à inteligência do jogador
        self.persi = random.randint(5, 10)  # relativo à persistência do jogador
        self.forca = random.randint(8, 10)  # relativo à força bruta do jogador
        self.dure = random.randint(9, 11)    # relativo à resistência, dureza do jogador
        self.louc = random.randint(5, 10)   # inversamente relativo à sanidade do jogador
        self.velo = random.randint(5, 10)   # relativo à agilidade do jogador
        (self, ide, nome, descricao, foto, equip)
        Traje1 = Equipavel(3, 'Jaqueta de Couro', 'Uma jaqueta feita de couro de gado. Tradicionalmente usada pelos trabalhadores do campo na Trácia.', None, True)
        Espada1 = Equipavel(4, 'Faca de Caça', 'Faca especializada na caça de animais e em trabalhos rurais.', None, True)
        Bonus1 = Equipavel(11, 'Laço', 'Corda usada pelos criadores de gado, equinos e camelos na região trácia.', None, True)
        self.itens = [Traje1, Espada1, Bonus1]


    '''def orar(self):
        print(f"{self.nome} rezou para {self.deus}")'''


class Ladrão(Player):
    def __init__(self, classe, nome):
        super().__init__(classe, nome)
        crencas = ['Ateu', 'Magnólio']
        deuses = ['Nenhum', 'Dimas Valverde']
        selecao = random.randint(0, 1)
        self.religiao = crencas[selecao]
        self.deus = deuses[selecao]
        self.hp = random.randint(25, 30)     # relativo à saúde do jogador
        self.inte = random.randint(6, 8)     # relativo à inteligência do jogador
        self.persi = random.randint(5, 10)  # relativo à persistência do jogador
        self.forca = random.randint(9, 11)  # relativo à força bruta do jogador
        self.dure = random.randint(9, 11)    # relativo à resistência, dureza do jogador
        self.louc = random.randint(10, 12)   # inversamente relativo à sanidade do jogador
        random.randint(12, 15)              # inversamente relativo à sanidade do jogador
        Traje1 = Equipavel(1, 'Manta Trácia', 'Uma manta tradicional do continente trácio. Fora entregue a você pelo seu pai, quando partiu de sua terra natal. Ele disse que faz bastante frio longe de casa.', None, True)
        Espada1 = Equipavel(4, 'Faca de Caça', 'Faca especializada na caça de animais e em trabalhos rurais.', None, True)
        Bonus1 = Equipavel(9, 'Chave Mestra', 'Aparelho capaz de abrir fechaduras. Geralmente usado por ladrões.', None, True)
        self.itens = [Traje1, Espada1, Bonus1]

    def correr(self, inimigo):
        if (self.persi + self.inte)/2 > (inimigo.persi + inimigo.inte)/2
            print(f"{self.nome} fugiu da batalha")
        else:
            print(f"{self.nome} falhou em fugir")
        
class Enemy:
    def __init__(self, classe, nome, hp, inte, persi, forca, dure, louc, xp):
        self.classe = classe # classe do inimigo
        self.nome = nome   # nome do inimigo
        self.hp = hp       # relativo à saúde do inimigo
        self.inte = inte   # relativo à inteligência do inimigo
        self.persi = persi # relativo à persistência do inimigo
        self.forca = forca # relativo à força bruta do inimigo
        self.dure = dure   # relativo à resistência, dureza do inimigo
        self.louc = louc   # inversamente relativo à sanidade do inimigo
        self.xp = xp       # experiencia que o inimigo dá ao ser derrotado


    def ataque(self, inimigo):
        # ataque básico e primário
        print(f"{self.nome} atacou {inimigo.nome}")
        inimigo.hp -= int(self.forca * 2  - inimigo.dure)
        if inimigo.hp < 0:
            inimigo.hp = 0


class Bebado(Enemy):
    def __init__(self, classe, nome, hp, inte, persi, forca, dure, louc, xp):
        super().__init__(classe, nome, hp, inte, persi, forca, dure, louc, xp)

    def ataque_bebado(self, inimigo):
        print(f"{self.nome} ataca {inimigo.nome} mas o efeito da bebida enfraquece o ataque")
        inimigo.hp -= int(self.louc + self.forca/2 - inimigo.dure)
        if inimigo.hp < 0:
            inimigo.hp = 0


class Lobo(Enemy):
    def __init__(self, classe, nome, hp, inte, persi, forca, dure, louc, xp):
        super().__init__(classe, nome, hp, inte, persi, forca, dure, louc, xp)
        self.hp = random.randint(15, 30)     # relativo à saúde do jogador
        self.inte = random.randint(0, 8)     # relativo à inteligência do jogador
        self.persi = random.randint(0, 8)   # relativo à persistência do jogador
        self.forca = random.randint(5, 8)    # relativo à força bruta do jogador
        self.dure = random.randint(5, 8)     # relativo à resistência, dureza do jogador
        self.louc = random.randint(0, 10)    # inversamente relativo à sanidade do jogador
    
    def morder(self, inimigo):
        print(f"{self.nome} abocanha {inimigo.nome}")
        inimigo.hp -= int(self.forca * 2  - inimigo.dure)
        if inimigo.hp < 0:
            inimigo.hp = 0

    
class Item:
        def __init__(self, ide, nome, descricao, foto):
            self.id = ide           # ID de identificação do item
            self.nome = nome        # nome do item
            self.desc = descricao   # descrição do item
            self.foto = foto        # foto do item (opcional)


class Consumivel(Item):
    def __init__(self, ide, nome, descricao, foto, quant):
        self.quant = quant   # a quantidade de itens que o jogador possui
        super().__init__(ide, nome, descricao, foto=None)

class Equipavel(Item):
    def __init__(self, ide, nome, descricao, foto, equip):
        self.equip = equip   # verifica se o item está equipado
        super().__init__(ide, nome, descricao, foto=None)

class Outro(Item):
    def __init__(self, ide, nome, descricao, foto):
        super().__init__(ide, nome, descricao, foto=None)


def batalha(P1, E1):
    input(f"\n{E1.nome} HP: {E1.hp}")
    input(f"{P1.nome} HP: {P1.hp}")
    print("\nPressione SPACE para atacar\n")
    if P1.classe == "Paladino":
        print("\nPressione O para rezar\n")
    lock = False
    lock_o = False
    while P1.hp > 0 and E1.hp > 0:
        if P1.classe == "Paladino":
            if keyboard.is_pressed('o') and not lock_o:
                P1.orar()
                print(f"{E1.nome} HP: {E1.hp}")
                if E1.classe == "Bêbado":
                    E1.ataque_bebado(P1)
                elif E1.classe == "Lobo":
                    E1.morder(P1)
                print(f"{P1.nome} HP: {P1.hp}")
                print("Pressione SPACE para atacar\n")
                print("\nPressione O para rezar\n")
                lock = True
        if keyboard.is_pressed('space') and not lock:
            P1.ataque(E1)
            if E1.classe == "Bêbado":
                E1.ataque_bebado(P1)
            elif E1.classe == "Lobo":
                E1.morder(P1)
            print(f"{E1.nome} HP: {E1.hp}")
            print(f"{P1.nome} HP: {P1.hp}")
            print("Pressione SPACE para atacar\n")
            lock = True
        elif not keyboard.is_pressed('space') and lock:
            lock = False
    if P1.hp == 0:
        input("Você está morto.")
        input("Vermes mastigam as vísceras magras da casca vazia de um homem.")
        input("E mesmo em sua derradeira podridão, tudo que essa carne exala é desejo")
        input("Boa noite, amigo.")
    else:
        print(f"{P1.nome} derrotou {E1.nome}")
        P1.xp += E1.xp
        P1.upar()


def mercado(P1):
    input("Você caminha por entre a feira, um amontoado de barracas de comércio nas quais adultos negociam e crianças brincam.")
    input("Você encontra algumas coisas que podem ser úteis.")
    na_feira = True
    while na_feira:
        if P1.classe == "Paladino":
            print("\n[1] Espada de Prata")
        elif P1.classe == "Berserker":
            print("\n[1] Espada Longa")
        elif P1.classe == "Ladrão" or P1.classe == "Cowboy":
            print("\n[1] Faca de Combate")
        print("[2] Ataduras")
        print("[3] Armadura")
        print("[4] Perguntar")
        print("[5] Sair")
        escolha_loja = int(input("\nEscolha o que deseja fazer/comprar: "))
        if escolha_loja == 1 and P1.classe == "Paladino":
            Espada2 = Equipavel(7, 'Espada de Prata', 'Uma bela espada cujo fio é feito de prata. Costumava ser usada por nobres.', None, False)
            P1.itens.append(Espada2)
            print(f"Você comprou {Espada2.nome}")
            input("\nVendedor: Eu comprei essa espada na mão de um cavaleiro que havia se endividado. É bem enfeitada e eficiente, mas eu acho que uma de aço")
            input("seria mais resistente.")
        elif escolha_loja == 1 and P1.classe == "Berserker":
            Espada2 = Equipavel(6, 'Espada Longa', 'Espada de aço segurada pelas duas mãos devido a seu grande porte. Perfeita para berserkers musculosos.', None, False)
            P1.itens.append(Espada2)
            print(f"Você comprou {Espada2.nome}")
            input("\nFerreiro: Forjei essa espada ontem, não me lembro de ter feito algo tão bom há muito tempo. Faça bom uso dela, rapaz.")
        elif escolha_loja == 1 and (P1.classe == "Ladrão" or P1.classe == "Cowboy"):
            Espada2 = Equipavel(8, 'Faca de Combate', 'Faca especializada no combate. Afiada e eficiente.', None, False)
            P1.itens.append(Espada2)
            print(f"Você comprou {Espada2.nome}")
        elif escolha_loja == 2:
            for item in P1.itens:
                if item.id == 4:
                    item.quant += 1
            Atadura = Consumivel(10, 'Ataduras', 'Faixa de tecido que é usada para tratar ferimentos.', None, 1)
            P1.itens.append(Atadura)
            print(f"Você comprou 1 {Atadura.nome}")
        elif escolha_loja == 3:
            Armadura_Saxa = Equipavel(5, 'Armadura Saxã', 'Peitoral e capacete da armadura que é usada pelos cavaleiros saxões. Pesada, mas bastante eficiente.', None, False)
            P1.itens.append(Armadura_Saxa)
            print(f"Você comprou {Armadura_Saxa.nome}")
            input("\nVendedor: Essa é parte da armadura completa dos cavaleiros reais do Reino da Saxônia. Eu acho seu formato particularmente engraçado.")
            input("\nVendedor: Minha filha disse que parece um peixinho, hehe.")
        elif escolha_loja == 4:
            input("Você pergunta ao vendedor sobre aquilo.")
            input('\nVendedor: Hum. Converso com muitas pessoas por aqui e nunca ouvi falar de nenhum "ancho".')
        elif escolha_loja == 5:
            na_feira = False


def missao_1(P1):
    P1.fase = 2
    estalagem_dica = False
    missao = True
    while missao:
        print("\nKomtur, a bela rosa da Saxônia")
        print("\n[1] Mercado")
        print("[2] Explorar")
        print("[3] Castelo")
        print("[4] Floresta")
        print("[5] Arena")
        print("[6] Estalagem")
        print("[7] Stats")
        escolha_missao = int(input("\nEscolha o que deseja fazer: "))
        if escolha_missao == 1:
            mercado(P1)
        if escolha_missao == 2:
            explorar_prob = random.randint(1, 4)
            if explorar_prob == 1:
                input("Você caminha pelo submundo de Komtur e encontra uma taverna. Você escuta risadas e o som leve de um piano ao fundo. Certamente")
                input("todo tipo de marginal se reunia ali.")
                print("\n[1] Entrar")
                print("[2] Ir embora")
                escolha_entrar = int(input("Escolha o que fazer: "))
                if escolha_entrar == 1:
                    input("Você decide entrar. Estranhamente o chão era limpo, ou ao menos mais limpo que o da outra taverna. O espaço era também muito maior")
                    input("que o daquela da outra cidade. Pessoas se reuniam nas mesas espalhadas pelo ambiente e alguns homens se sentavam em frente ao balcão,")
                    input("onde eram servidas as bebidas. Havia uma escadaria que levava a um segundo andar, onde algumas moças gargalhavam e acenavam de lá de")
                    input("cima. Eram meretrices. O pianista também se encontrava ali.")
                    taverna = True
                    irsa_pista = False
                    while taverna:
                        print("\n[1] Bebida")
                        print("[2] Meretrix")
                        print("[3] Pedir informação")
                        print("[4] Sair")
                        escolha_taverna = int(input("\nEscolha o que deseja fazer: "))
                        if escolha_taverna == 1:
                            # EDITAR BEBIDAS
                            input("Você adentra numa taverna fétida. Olhos pairam sob sua feição. Você escuta umas risadinhas ao fundo, mas não presta muita atenção.")
                            input("Repousa em um banco a frente do balcão e o bartender lhe oferece bebida.")
                            print("\n[1]Cerveja|200 moedas de ouro")
                            print("[2]Vinho doce|600 moedas de ouro")
                            print("[3]Hidromel|300 moedas de ouro")
                        elif escolha_taverna == 2:
                            # UMA LINHA INTEIRA NO CMD É ATE A PALAVRA PIANO
                            input("Você sobe o jogo de escadas até o andar de cima, você consegue ouvir bem o piano daqui. As moças olham para você e você vai em")
                            input("direção a elas.")
                            print("\n[1] Serviço|5 prata")
                            print("[2] Andar de baixo")
                            if irsa_pista:
                                print("[3] Perguntar sobre o caso")
                            escolha_meret = int(input("\nMeretrix: Posso te ajudar, mocinho?"))
                            if escolha_meret == 1:
                                input("A companhia da moça conforta sua carne, mas seu espírito continua em agonia. Não é como antes. Você sente frio.")
                            elif escolha_meret == 2:
                                sair()
                            elif escolha_meret == 3 and irsa_pista:
                                input("Você pergunta se alguma delas viu algo relacionado aos crimes na rua onde trabalham.")
                                input("\nMeretrix: Oh, sim, a Irsa comentou de ter avistado uma figura estranha nessa noite, converse com ela, ela está em frente")
                                input("àquele cômodo.")
                                input("Você vai até o lugar indicado e encontra a meretrix chamada Irsa encostada na porta do cômodo. Era uma mulher jovem e muito")
                                input("bela, seus lábios eram bem vermelhos e, seus cabelos, castanhos e bem cacheados. Não se vestia tão bem quanto as outras, mas")
                                input("na realidade, nem precisava.")
                                input("\nIrsa: Oi, garotão, então você quer um pouco de diversão?")
                                input("\nVocê pergunta a ela sobre o caso.")
                                input("\nIrsa: O quê?")
                                input("\nIrsa: Ah, sim, a rua ali de trás.")
                                input("\nIrsa: Escute aqui, você devia ter cuidado com o que está se metendo.")
                                #luta(irsa)
                                input("\nIrsa: Nossa, pelo visto essa sua espada não é só de enfeite. Mas foi bom testar pra ver se você tá esperto. Olha, eu vi um sujeito")
                                input("encapuzado vindo da direção em que o corpo de um nobre foi encontrado no dia seguinte. Estava muito escuro e eu não o vi direito.")
                                input("\nIrsa: Mas eu lembro de vê-lo virar no beco que leva à estalagem. Você deveria ir lá verificar e conversar com o dono")
                                estalagem_dica = True
                        elif escolha_taverna == 3:
                            input("Você se reune com os homens em um banco a frente do balcão e chama o bartender que prontamente atende ao seu chamado. Era um homem em")
                            input("seus 40 ou 50. Era bem magro, baixo e careca. Seu olhar parecia meio abatido, mas mesmo assim estampava um largo sorriso em seu rosto.")
                            input("Você encosta perto dele e pergunta baixinho se ele sabe algo sobre o assassinato dos nobres.")
                            input("\nBartender: Veja bem, se fosse um daqueles cavaleiros esnobes eu diria que não sei de nada.")
                            input("\nBartender: Nada.")
                            input("\nBartender: Mas você não parece entender bem como funcionam as coisas por aqui, e além do mais parece ser um bom rapaz.")
                            input("\nBartender: Escute garoto, como dono dessa taverna eu aprendi que as pessoas não saem por aí falando de crimes que testemunharam.")
                            input("\nBartender: Ao menos não de graça.")
                            input("\nUm sorriso sombrio se abre no rosto do homem.")
                            print("\n[1] Entregar")
                            print("[2] Sair")
                            pagar_1 = int(input("\nQuatro moedas de ouro, é tudo que eu lhe peço."))
                            if pagar_1 == 1:
                                input("\nBartender: Isso mesmo, garoto. Muito bem. Mas eu de fato não presenciei nenhum assassinato e não sei muito sobre esses casos, mas")
                                input("soube que alguns deles ocorreram na Rua das Meretrices. Pergunte a elas se viram algo.")
                                input("Você é um idiota.")
                                irsa_pista = True
                        elif escolha_taverna == 4:
                            taverna = False
            elif explorar_prob == 2 and not criancas:
                criancas_sidequest()
                criancas = True
            elif explorar_prob == 3:
                perguntar_civis
            elif explorar_prob == 4:
                luta_arruaceiros()
        elif escolha_missao == 6:
            if estalagem_dica:
                input("Você caminha pelo submundo de Komtur e encontra em uma taverna. Você escuta risadas e o som leve de um piano ao fundo. Certamente")
                input("Você vai até a estalagem para dar prosseguimento à investigação.")
                input("Um amontoado de cômodos fétido e sujo, habitado por pessoas, ratos e baratas.")
                input("Você vai de encontro a um homem que se sentava em frente a uma das casas e pergunta se ele podia lhe ajudar com esse caso.")
                input("\nBartender: Hehe. Nos encontramos novamente, não é, bom rapaz?")
                input('\nBartender: Sim, não sei se você sabe mas sou dono desse simples cortiço também. Sou o que chamam de "empreendedor".')
                input("\nBartender: O que desejas agora, doce criatura? Descobriu mais sobre o caso?")
                input("\nVocê pergunta a ele se algum dos moradores voltou para casa tarde na noite do assassinato.")
                input("\nBartender: Ah sim, então é isso. É realmente uma pena que meus humildes inquilinos estejam sob suspeita. Mas veja rapaz, esse")
                input("serviço também terá um custo.")
                input("\nBartender: Um passarinho me disse que você está a serviço direto da coroa. E seria muito gratificante que a ajuda que lhe foi")
                input("dada pelo Sr. Malfatti chegasse aos ouvidos de Sua Majestade, não é mesmo?")
                print("\n[1] Com certeza")
                print("[2] Não sou garoto de recados")
                pagar_2 = int(input("Escolha o que dizer: "))
                if pagar_2 == 1:
                    input("\nSr. Malfatti: Muito bem, rapaz. Pois então, o único que costuma chegar tarde da noite por aqui é o morador da casa número 8.")
                    input("\nSr. Malfatti: Não me lembro dessa noite em específico, mas estou certo de que acontece em todas.")
                    input("\nSr. Malfatti: Acho que ele está em casa, pode ir lá vê-lo.")
                    input("\nVocê sobe um jogo de escadas até o cômodo número 8 e bate na porta, mas não obtém resposta.")
                    print("\n[1] Arrombar")
                    # if P1.classe = "Ladrão" and P1.itens.id == chave_mestra.id: [2] Abrir cadeado
                    escolha_porta = input("\nEscolha o que fazer: ")
                    if escolha_porta == 1:
                        input("Você arromba a porta do cômodo e percebe que o suspeito não se encontra mais lá. Porém uma das janelas do quarto estava aberta.")
                        input("\nSr. Malfatti: Aaaah minha porta!!")
                    input("\nPela janela você avista um vulto que corre pelas vielas da periferia. Você pula a janela e começa a correr atrás da figura. Após")
                    input("percorrerem a cidade inteira sem que você chegasse sequer próximo do meliante, ele entra na floresta, sumindo na escuridão. Você o")
                    input("segue e entra lá também.")
                    input("Você nem vê sinal da figura, mas segue procurando pela masmorra de madeira, que parece estar mais escura que o habitual.")
                    #elif escolha_porta == 2:
                    #luta(lobo)3x[pode ser reduzido com maior agilidade]
                    #luta(lobisomem[lobo gigante])
                    #luta(morador casa número 8)
                #if pagar_2 == 2:
            else:
                cria_bullshit(P1.nome, P1.religiao, P1.deus, P1.level, [P1.hp, P1.inte, P1.persi, P1.forca, P1.dure, P1.louc, P1.velo], P1.fase, P1.classe)
        elif escolha_missao == 7:
            P1.imprime_stats()
                

def novo_jogo():
    nome = input("Digite seu nome: ")
    print('Paladino', '\nBerserker', '\nLadrão', '\nCowboy')
    classe = input("Escolha uma classe entre essas: ")
    if classe == 'Paladino':
        P1 = Paladino(classe, nome)
    elif classe == 'Berserker':
        P1 = Berserker(classe, nome)
    elif classe == 'Ladrão':
        P1 = Ladrão(classe, nome)
    elif classe == 'Cowboy':
        P1 = Cowboy(classe, nome)
    else:
        print("Classe inválida!")
    return P1


def jogo():
    print("\nNAS PROFUNDEZAS DA LOUCURA\n")
    print("[1]NEW GAME")
    print("[2]CONTINUE")
    opcao = input("\nEscolha uma opção: ")
    if opcao == '1':
        P1 = novo_jogo()
        input(f"Você é um {P1.classe} que acaba de chegar em uma terra estrangeira.")
        input("As pessoas e as casas são diferentes e você se sente um pouco deslocado.")
    elif opcao == '2':
        dados = traduz_bullshit()
        classe = dados[6]
        nome = dados[0]
        if classe == 'Paladino':
            P1 = Paladino(classe, nome)
        elif classe == 'Berserker':
            P1 = Berserker(classe, nome)
        elif classe == 'Ladrão':
            P1 = Ladrão(classe, nome)
        elif classe == 'Cowboy':
            P1 = Cowboy(classe, nome)
        P1.religiao = dados[1]
        P1.deus = dados[2]
        P1.level = int(dados[3])
        P1.hp = int(dados[4][0])
        P1.inte = int(dados[4][1])
        P1.persi = int(dados[4][2])
        P1.forca = int(dados[4][3])
        P1.dure = int(dados[4][4])
        P1.louc = int(dados[4][5])
        P1.velo = int(dados[4][6])
        P1.fase = int(dados[5])
    jogo = True
    while jogo:
        P1.fase = 1
        if P1.fase == 0:
            escolha_vila = 0
            while escolha_vila != 1:
                print("\nVilarejo")
                print("\n[1] Taverna")
                print("[2] Explorar")
                print("[3] Estalagem")
                print("[4] Stats")
                escolha_vila = int(input("\nEscolha o que deseja fazer: "))
                if escolha_vila == 2:
                    explorar()
                elif escolha_vila == 3:
                    input("Você vai até um casarão mal acabado e sujo que serve de habitação para moradores e viajantes. O aluguel é cobrado por noite e")
                    input("estrangeiros devem pagar antecipado.")
                    print("[1]Passar a noite|3 m. prata")
                    print("[2]Sair")
                    escolha_est_vila = int(input("Escolha o que fazer: "))
                    if escolha_est_vila == 1:
                        cria_bullshit(P1.nome, P1.religiao, P1.deus, P1.level, [P1.hp, P1.inte, P1.persi, P1.forca, P1.dure, P1.louc, P1.velo], P1.fase, P1.classe)
                        print("Jogo salvo com sucesso.")
                        sonhar()
                        print("\n[1]Sim")
                        print("[2]Não")
                        escolha_fechar = int(input("Deseja continuar jogando? "))
                        if escolha_fechar == 2:
                            exit()
                elif escolha_vila == 4:
                    P1.imprime_stats()
            input("Você adentra numa taverna fétida. Olhos pairam sob sua feição. Você escuta umas risadinhas ao fundo, mas não presta muita atenção.")
            input("Repousa em um banco a frente do balcão e o bartender lhe oferece bebida.")
            print("\n[1]Cerveja|200 moedas de ouro")
            print("[2]Vinho doce|600 moedas de ouro")
            print("[3]Hidromel|300 moedas de ouro")
            bebida = int(input("Escolha: "))
            if bebida == 1 or bebida == 3:
                input("\nO homem forte e troncudo retira de um barril um líquido ralo cuja cor era semelhante a de urina. Deposita o líquido em uma caneca de")
                input("madeira e a coloca no balcão enquanto ergue a mão, pegando o dinheiro do pagamento.")
                print("\n[1]Beber")
                input("Escolha: ")
                if bebida == 1:
                    input("\nVocê toma um gole de sua bebida, o gosto é aguado e amargo.")
                elif bebida == 3:
                    input("\nVocê toma um gole de sua bebida, tem gosto de vinho doce e barato.")
            elif bebida == 2:
                input("\nO homem forte e troncudo retira de uma gaveta atrás do balcão uma garrafa de um líquido forte da cor de sangue e uma taça empoeirada,")
                input("que ele desempoeira com um trapo velho, a preenche com a bebida e a coloca no balcão enquanto ergue a mão, pegando o dinheiro do")
                input("pagamento.")
                print("\n[1]Beber")
                input("Escolha: ")
                input("\nVocê toma um gole de sua bebida, não é o melhor vinho que você já experimentou")
                input("mas dá pro gasto.")
            input("Enquanto bebia, um homem estranho, aparentemente alcoolizado, acaba derramando bebida em suas vestes. Você se limpa e volta a")
            input("apreciar sua bebida. Acidentes acontecem.")
            input("Porém, você logo escuta o desembainhar de uma espada atrás de você.")
            input("Ele queria confusão.")
            input("\nBêbado: O que um covarde como você faz em meu país? Suma da miha vista.")
            Sir_JamesIII = Bebado("Bêbado", "Bêbado", 20, 2, 12, 5, 4, 15, 1)
            batalha(P1, Sir_JamesIII)
            input("Após derrotar o bêbado, as pessoas ao redor parecem abismadas, como se você tivesse cometido um crime. O bartender com feições de medo o")
            input("expulsa do estabelecimento sem que você sequer acabasse sua bebida.")
            input("Você parte da vila e segue em direção a uma floresta.")
            for i in range(3):
                input("Era imensa. ")
                escolha = input("\nDigite A para continuar andando, B para ver seus stats e S para salvar: ")
                escolha = escolha.upper()
                while escolha != 'A':
                    if escolha == 'B':
                        P1.imprime_stats()
                        escolha = input("\nDigite A para continuar andando, B para ver seus stats e S para salvar: ")
                        escolha = escolha.upper()
                    elif escolha == 'S':
                        cria_bullshit(P1.nome, P1.religiao, P1.deus, P1.level, [P1.hp, P1.inte, P1.persi, P1.forca, P1.dure, P1.louc, P1.velo], P1.fase, P1.classe)
                        print("Jogo salvo com sucesso.")
                        escolha = input("\nDigite A para continuar andando, B para ver seus stats e S para salvar: ")
                        escolha = escolha.upper()
                opcao = random.randint(1, 2)
                if opcao == 1:
                    lobo_floresta = Lobo("Lobo", "Lobo", 0, 0, 0, 0, 0, 0, 14)
                    batalha(P1, lobo_floresta)
            input("Ao chegar no fim do imenso labirinto de àrvores, você avista uma enorme construção ao horizonte. Um castelo. Era incrível como ele")
            input("podia ser visto mesmo você estando bem longe. Ali provavelmente é um lugar grande e importante. Você decide ir naquela direção.")
            input("Ao se aproximar da cidade que se formava em torno do castelo, você encontra uma placa com os seguintes dizeres:")
            P1.fase = 1
        elif P1.fase == 1:
            em_komtur = True
            while em_komtur:
                print("\nKomtur, a bela rosa da Saxônia")
                print("\n[1] Mercado")
                print("[2] Explorar")
                print("[3] Castelo")
                print("[4] Floresta")
                print("[5] Arena")
                print("[6] Estalagem")
                print("[7] Stats")
                escolha_komtur = int(input("\nEscolha o que deseja fazer: "))
                if escolha_komtur == 1:
                    mercado(P1)
                elif escolha_komtur == 2:
                    explorar_prob = random.randint(1, 8)
                    if explorar_prob == 1 or explorar_prob == 2:
                        input("Enquanto caminha pelas ruas da cidade, você pensa em fazer algo.")
                        input("\nVocê pergunta a um cidadão sobre aquilo.")
                        input("\nSaxão: Anjo? Desculpe, mas nunca ouvi falar nisso.")
                    elif explorar_prob == 3:
                        #criancas_sidequest()
                        criancas = True
                    elif explorar_prob == 4:
                        input("Ao caminhar pelo centro da cidade você avista uma estrutura que se destaca. Era coberta por muretas que também cercavam o jardim e")
                        input("a torre do sino ao seu lado e se abriam na direção da porta, permitindo a passagem. Sua beleza era celestial, possuia dois andares")
                        input("e janelas de vidro que pareciam convidá-lo a entrar de forma incessante. O símbolo de uma espécie de roda pairava sob o topo do")
                        input("templo.")
                        input("Ao entrar você percebe que se trata do templo de Forseti, o deus local do vento.")
                        input("\n[1] Rezar")
                        input("[2] Ir embora")
                    elif explorar_prob == 5 or explorar_prob == 6:
                        input("Enquanto você caminha pelo centro da cidade, percebe que alguém está o seguindo. Você tenta despistar o perseguidor de início, mas")
                        input("ele se aproxima cada vez mais, então você se vira e percebe não um, mas uma dúzia de soldados armados atrás de você. Com rapidez,")
                        input("você desembainha a sua espada e se prepara para um provável ataque.")
                        input("\nSoldado: Parece que é ele, capitão!")
                        #(luta soldados)
                        P1.win = True
                        if not P1.win:
                            input("Após ser derrotado pelo exército, você é amarrado e levado para o castelo, onde o carregam por enormes salões e corredores até")
                            input("de pele castanha e vestido em trapos.  chegar aos aposentos do que parecia ser o rei daquele nação.")
                            input("\nCapitão: Trouxemos o criminoso, Sua Majestade. Este homem segue exatamente a descrição das testemunhas. Um estrangeiro de")
                            input("grande porte, pele morena e vestido em trapos.")
                            input("\nRei: Hum. Então foi esse cara que bateu no Ezekiel.")
                            input("\nEra um homem em seus trinta anos, uma manta real cobria seu torço e uma bermuda")
                            input("havaiana suas coxas. Era um sujeito bastante excêntrico, de fato.")
                            input("\nRei: Vocês podem se retirar.")
                            input("\nOs soldados se retiraram.")
                            input("\nRei: Então guri, você agrediu um cara em um vilarejo. Pois bem, esse cara é o Conde de Waldrand tchê. Você deu azar, guri e")
                            input("agora eu vou ter que te punir tlgd.")
                            input("\nRei: Mas bah, me disseram que você sentou o relho nos meus soldados, você deve ser triforte, né? É o que estrangeiros")
                            input('chamariam de "berserker".')
                            input("\nRei: Voltando, como punição pelo que tu fez, tenho um serviço para você tchê, apesar de ser um castigo, você será muito")
                            input("bem pago por esse trabalho.")
                            print("\n[1] Aceitar")
                            print("[2] Recusar")
                            aceitar_missao = int(input("Rei: Então guri, você aceita?"))
                            if aceitar_missao == 1:
                                print("\nMISSÃO 1\n")
                                input("\nRei: Então piá, seguinte: vários nobres importantes vêm sendo mortos nos últimos dias tchê. Quero que você vá até o")
                                input("submundo da cidade, encontre e elimine os assassinos e mandantes desses crimes. Essa missão é perfeita pra tu, eu pensei em")
                                input("mandar o exército, mas ia chamar muita atenção tlgd.")
                                missao_1(P1)
                        else:
                            input("Após derrotá-los, você supõe pelas vestes e símbolos deles que são cavaleiros enviados por nobres. Você se pergunta por que")
                            input("alguém assim estaria atrás de você.")
                    elif explorar_prob == 7 or explorar_prob == 8:
                        input("Você entra na cidade e explora seus arredores. Você nunca esteve em um lugar assim. Muitas casas e muitas pessoas. O fluxo nas ruas")
                        input("era constante, você se sentia claustrofóbico. Porém, para sua surpresa, poucos o olham com desconfiança, diferente daquele vilarejo,")
                        input("aqui eles estão mais acostumados a rostos estrangeiros.")
                        input("A arquitetura da cidade era inédita aos seus olhos, diferente da cidade anterior, essa era repleta de casarões enfeitados com")
                        input("estátuas de quimeras e leões, além das casinhas populares de madeira e ao centro um enorme e estranho castelo, coberto por")
                        input("gigantescas muralhas.")
                if escolha_komtur == 3:
                    if P1.win:
                        input("Você caminha até o castelo real, no centro da cidade e vai até a corte real, onde um sujeito bastante excêntrico se senta no trono")
                        input("\nRei: Então guri, você agrediu um cara em um vilarejo. Pois bem, esse cara é o Conde de Waldrand tchê. Você deu azar, guri e")
                        input("agora eu vou ter que te punir tlgd.")
                        input("\nRei: Mas bah, me disseram que você sentou o relho nos meus soldados, você deve ser triforte, né? É o que estrangeiros")
                        input('chamariam de "berserker".')
                        input("\nRei: Voltando, como punição pelo que tu fez, tenho um serviço para você tchê, apesar de ser um castigo, você será muito")
                        input("bem pago por esse trabalho.")
                        print("\n[1] Aceitar")
                        print("[2] Recusar")
                        aceitar_missao = int(input("Rei: Então guri, você aceita?"))
                        if aceitar_missao == 1:
                            print("\nMISSÃO 1\n")
                            input("\nRei: Então piá, seguinte: vários nobres importantes vêm sendo mortos nos últimos dias tchê. Quero que você vá até o")
                            input("submundo da cidade, encontre e elimine os assassinos e mandantes desses crimes. Essa missão é perfeita pra tu, eu pensei em")
                            input("mandar o exército, mas ia chamar muita atenção tlgd.")
                            missao_1(P1)
                    else:
                        input("Você caminha até o castelo real, no centro da cidade. Ele foi construído em uma espécie de morro ou colina, de forma que era bem")
                        input("difícil de invadir e fazia com que ele pudesse ser visto da cidade inteira. A imensidão e esplendor daquele edifício o esmagam e")
                        input("o fascinam. Era muito diferente do resto da cidade, como se clamasse a soberania dos nobres.")
                elif escolha_komtur == 6:
                    cria_bullshit(P1.nome, P1.religiao, P1.deus, P1.level, [P1.hp, P1.inte, P1.persi, P1.forca, P1.dure, P1.louc, P1.velo], P1.fase, P1.classe)
                    print("Jogo salvo com sucesso.")
                elif escolha_komtur == 7:
                    P1.imprime_stats()
        elif P1.fase == 2:
            missao_1(P1)


jogo()

import random

# ACENTO

def criptografa_cesar(nome):
    codigo = ''
    # Criptografa uma palavra usando cifra de César e tabela ascii
    for letra in nome:
        asc = ord(letra)
        if 65 <= asc <= 90 or 97 <= asc <= 122:
            x = asc - 32
            y = asc - 30
            z = asc - 28
            codigo += str(chr(x))
            codigo += str(chr(y))
            codigo += str(chr(z))
        elif letra == ' ' :
            codigo += 'xxx'
        elif letra == '.' :
            codigo += 'yyy'
    codigo += 'z'
    return codigo


def descript_cesar(codigo):
    descript = ''
    # Descriptografa um código que está em cifra de César
    cont = 3
    for letra in codigo:
        if cont % 3==0:
            if letra == 'x':
                descript += ' '
            elif letra == 'y':
                descript += '.'
            else:
                asc = ord(letra)
                x = asc + 32
                descript += str(chr(x))
        cont += 1
    return descript


def criptografa_polibio(numeros):
    # Criptografa uma lista de números usando o diagrama de Políbio
    codigo = ''
    chave = {4:'11', 7:'12', 1:'13',
             8:'21', 6:'22', 9:'23',
             2:'31', 5:'32', 3:'33',
             0:'41'}
    for numero in numeros:
        for alg in str(numero):
            codigo += chave[int(alg)]
            codigo += ','
        codigo += '.'
    return codigo


def descript_polibio(codigo):
    # Descriptografa um código que está criptografado com diagrama de Políbio
    descript = []
    chave = {'11':4, '12':7, '13':1,
             '21':8, '22':6, '23':9,
             '31':2, '32':5, '33':3,
             '41':0}
    numeros = codigo.split('.')
    for numero in numeros[:-1]:
        algs = numero.split(',')
        stat = ''
        for alg in algs[:-1]:
            stat += str(chave[alg])
        descript.append(stat)
    return descript


def cria_bullshit(nome, religiao, deus, level, stats, fase, classe):
    # Criptografa o nome, religião e divindade usando cifra de César
    codigo = criptografa_cesar(nome)
    codigo += criptografa_cesar(religiao)
    codigo += criptografa_cesar(deus)
    # Criptografa o level multiplicando ele por uma chave aleatória
    chave = random.randint(1000, 9999)
    level = level * chave
    codigo += str(level)
    codigo += str(chave) + 'z'
    # Criptografa os stats usando o diagrama de Políbio
    codigo += criptografa_polibio(stats) + 'z'
    codigo += str(fase) + 'z'
    codigo += str(classe) + 'z'
    save = open('save.txt', 'w')
    save.write(codigo)
    save.close()

def traduz_bullshit():
    save = open('save.txt', 'r')
    texto = save.read()
    save.close()
    codigo = texto.split('z')
    # Descriptografa o nome, religião e divindade usando cifra de César
    descript = []
    descript.append(descript_cesar(codigo[0]))
    descript.append(descript_cesar(codigo[1]))
    descript.append(descript_cesar(codigo[2]))
    # Descriptografa o level o dividindo pela chave
    level = codigo[3]
    chave = int(level[-4:])
    level = int(level[:-4])
    level = int(level) // chave
    descript.append(level)
    # Descriptografa os stats usando o diagrama de Políbio
    descript.append(descript_polibio(codigo[4]))
    descript.append(codigo[5])
    descript.append(codigo[6])
    return descript

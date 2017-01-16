#-*- coding:utf-8 -*-

from random import shuffle

#Função que manipula as instancias
def manipula_inst(num_inst):
    arq = open('db/binpack1.txt','r').readlines()
    count = 0
    lista_it = []

    if(num_inst == 1):
        for linha in arq[2:]:
            if(linha == " u120_01 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 2):
        for linha in arq[124:]:
            if(linha == " u120_02 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 3):
        for linha in arq[246:]:
            if(linha == " u120_03 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 4):
        for linha in arq[368:]:
            if(linha == " u120_04 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 5):
        for linha in arq[490:]:
            if(linha == " u120_05 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 6):
        for linha in arq[612:]:
            if(linha == " u120_06 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 7):
        for linha in arq[734:]:
            if(linha == " u120_07 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 8):
        for linha in arq[856:]:
            if(linha == " u120_08 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 9):
        for linha in arq[978:]:
            if(linha == " u120_09 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 10):
        for linha in arq[1100:]:
            if(linha == " u120_10 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 11):
        for linha in arq[1222:]:
            if(linha == " u120_11 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 12):
        for linha in arq[1344:]:
            if(linha == " u120_12 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 13):
        for linha in arq[1466:]:
            if(linha == " u120_13 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 14):
        for linha in arq[1588:]:
            if(linha == " u120_14 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 15):
        for linha in arq[1710:]:
            if(linha == " u120_15 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 16):
        for linha in arq[1832:]:
            if(linha == " u120_16 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 17):
        for linha in arq[1954:]:
            if(linha == " u120_17 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 18):
        for linha in arq[2076:]:
            if(linha == " u120_18 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 19):
        for linha in arq[2198:]:
            if(linha == " u120_19 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    elif(num_inst == 20):
        for linha in arq[2320:]:
            if(linha == " u120_20 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

    else:
        print("Número não reconhecido, será lido a primeira instância\n\n\n")
        for linha in arq[2:]:
            if(linha == " u120_01 \n"):
                break

            lista_it.append(int(linha.rstrip()))
            count = count + 1

        return lista_it

#Função que cria a lista restrita de candidatos
def gera_lrestrito(lista,alpha):
    lista_restrit = []
    for elemento in lista:
        if(min(lista) <= elemento and elemento <= min(lista) + alpha * (max(lista) - min(lista))):
            lista_restrit.append(elemento)
        else:
            continue
    return lista_restrit

#Método Construtivo
def constroi(lista_itens, alpha):
    mochilas = {}

    while(lista_itens):
        i = 0

        lista_restrito = []
        lista_restrito = gera_lrestrito(lista_itens, alpha)

        shuffle(lista_restrito)

        #print(lista_restrito)
        #print(lista_itens)

        if(len(mochilas.keys()) == 0):
            mochilas[0] = []
            mochilas[0].append(lista_restrito[i])

            lista_itens.remove(lista_restrito[i])
            lista_restrito.remove(lista_restrito[0])
        else:
            for chave in range(len(mochilas.keys())):
                if(sum(mochilas[chave]) + lista_restrito[i] <= capacidade):

                    mochilas[chave].append(lista_restrito[i])

                    lista_itens.remove(lista_restrito[i])
                    lista_restrito.remove(lista_restrito[0])
                    break
                elif(mochilas.__contains__(chave+1)):
                    continue
                else:
                    mochilas[chave + 1] = []
                    mochilas[chave + 1].append(lista_restrito[i])

                    lista_itens.remove(lista_restrito[i])
                    lista_restrito.remove(lista_restrito[0])
    return mochilas

#Busca Local


if __name__ == '__main__':

    #lista_res = []
    capacidade = 150

    #lista de itens a serem alocados nas mochilas, entre com números de 1 a 20
    lista_ite = manipula_inst(1)

    #lista_ite = [33, 79, 27, 57, 44, 84, 86, 92, 46, 38, 85, 33, 82]
    #print(lista_ite)
    #print(gera_lrestrito(lista_itens, 0.8))

    mochilas = constroi(lista_ite, .8)

    for chave in mochilas.keys():
        print("Mochila[",chave,"]"," => ",mochilas[chave], "\t\t|| Peso => ", sum(mochilas[chave]))